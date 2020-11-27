package docker_bench

import (
	"context"
	"fmt"
	"github.com/docker/docker/api/types"
	"github.com/docker/docker/api/types/container"
	"github.com/docker/docker/api/types/mount"
	"github.com/docker/docker/client"
	"github.com/fre_code/utils"
	"io/ioutil"
	"log"
	"os"
	"path"
	"sync"
)

func NewDockerClient(dockerHost string) *client.Client {
	cli, err := client.NewClient(dockerHost, "1.40", nil, nil)
	if err != nil {
		log.Fatal(err)
	}
	return cli
}

func Clear(cli *client.Client) {
	containerList, err := cli.ContainerList(context.Background(), types.ContainerListOptions{
		All: true,
	})
	if err != nil {
		log.Fatal("clear:", err)
	}
	wg := sync.WaitGroup{}
	wg.Add(len(containerList))
	for _, c := range containerList {
		go func(cId string) {
			_ = cli.ContainerRemove(context.Background(), cId, types.ContainerRemoveOptions{
				RemoveVolumes: true,
				Force:         true,
			})
			wg.Done()
		}(c.ID)
	}
	wg.Wait()
	log.Printf("clear %d old container(s)\n", len(containerList))
}

func CreateContainer(cli *client.Client, id int, networkMode string) (string, error) {
	createResponse, err := cli.ContainerCreate(
		context.Background(),
		&container.Config{
			Image:        "wait:latest",
			Shell:        []string{"/bin/sh", "/bin/bash"},
			AttachStdin:  true,
			AttachStdout: true,
			AttachStderr: true,
			Tty:          true,
			OpenStdin:    true,
		},
		&container.HostConfig{
			Privileged:      false,
			PublishAllPorts: true,
			Mounts:          []mount.Mount{{Type: "bind", Source: "/etc/localtime", Target: "/etc/localtime", ReadOnly: true}},
			NetworkMode:     container.NetworkMode(networkMode),
		},
		nil,
		fmt.Sprintf("test-%d-%d", id, utils.GetCurrentMicroTimestamp()),
	)
	if err != nil {
		log.Printf("createContainer[%d] error: %+v\n", id, err)
		return "", err
	}
	return createResponse.ID, nil
}

func StartContainer(cli *client.Client, containerId string) error {
	err := cli.ContainerStart(context.Background(), containerId, types.ContainerStartOptions{})
	if err != nil {
		log.Printf("startContainer[%s] error: %+v\n", containerId, err)
		return err
	}
	return nil
}

func ReadContainerLog(cli *client.Client, containerId string) (string, error) {
	reader, err := cli.ContainerLogs(context.Background(), containerId, types.ContainerLogsOptions{ShowStdout: true, ShowStderr: false})
	if err != nil {
		log.Printf("readContainerLog[%s] error: %+v\n", containerId, err)
		return "", err
	}
	defer reader.Close()

	containerLog, err := ioutil.ReadAll(reader)
	if err != nil {
		log.Printf("readContainerLog[%s] error: %+v\n", containerId, err)
		return "", err
	}
	return string(containerLog), nil
}

func SaveToFile(content string, prefix, fileName string) {

	if err := Mkdir(prefix); err != nil {
		return
	}

	fullName := path.Join(prefix, fileName)

	file, err := os.OpenFile(fullName, os.O_WRONLY|os.O_CREATE, 0666)
	if err != nil {
		log.Fatalf("OpenFile %s error: %+v\n", fullName, err)
	}

	if _, err := file.Write([]byte(content)); err != nil {
		log.Println("Write error:", err)
	}

	_ = file.Close()
	log.Printf("save data to %s ok\n", fullName)
}

func Mkdir(prefix string) error {
	exist, err := PathExists(prefix)
	if err != nil {
		log.Println("SaveToFile err:", err)
		return err
	}

	if !exist {
		if err := os.Mkdir(prefix, os.ModePerm); err != nil {
			log.Println("Mkdir err:", err)
			return err
		}
	}

	return nil
}

func PathExists(prefix string) (bool, error) {
	_, err := os.Stat(prefix)
	if err == nil {
		return true, nil
	}

	if os.IsNotExist(err) {
		return false, nil
	}
	return false, err
}
