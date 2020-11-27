package main

import (
	"context"
	"flag"
	"fmt"
	"github.com/docker/docker/api/types"
	"github.com/docker/docker/client"
	"log"
	"strconv"
	"strings"
	"sync"
	"time"
)

var (
	count          int
	waitRunning    int
	parallel       bool
	dockerHost     string
	prefixPath     string
	networkMode    string
	startTimestamp []int64
)

func init() {
	flag.IntVar(&count, "n", 2, "启动的容器数量")
	flag.BoolVar(&parallel, "p", false, "是否并发创建")
	flag.StringVar(&dockerHost, "h", "tcp://192.168.2.12:20375", "Docker server地址")
	flag.StringVar(&prefixPath, "o", "result", "输出结果的路径")
	flag.IntVar(&waitRunning, "t", 300, "等待获取状态超时时间")
	flag.StringVar(&networkMode, "network", "bridge", "网络模式")
}

func main() {
	flag.Parse()
	fmt.Printf("count=%d, host=%s, parallel=%+v\n", count, dockerHost, parallel)
	startTimestamp = make([]int64, count)

	// 清理旧的容器
	cli := docker_bench.NewDockerClient(dockerHost)
	docker_bench.Clear(cli)

	log.Println("start run new container")
	if parallel { // 并发创建
		wg := sync.WaitGroup{}
		wg.Add(count)
		for i := 0; i < count; i++ {
			go func(idx int) {
				doCreateContainer(cli, idx, &wg)
			}(i)
		}
		wg.Wait()
	} else { // 顺序创建
		for i := 0; i < count; i++ {
			doCreateContainer(cli, i, nil)
		}
	}

	log.Println("run container ok, start fetch data")
	// 到此所有容器调用启动完成，开始收集数据
	for i := 0; i < waitRunning; i++ {
		containerList, err := cli.ContainerList(context.Background(), types.ContainerListOptions{All: true})
		if err != nil {
			fmt.Println("Get ContainerList error:", err)
		} else {
			notRunningCount := 0
			for _, container := range containerList {
				if container.State != "running" {
					notRunningCount++
				}
			}
			if notRunningCount == 0 {
				collectData(cli, containerList)
				return
			} else {
				log.Printf("%d container(s) is(are) not running\n", notRunningCount)
			}
		}
		time.Sleep(time.Second * 1)
	}
	fmt.Println("done")
}

func doCreateContainer(cli *client.Client, id int, wg *sync.WaitGroup) {
	defer func() {
		if wg != nil {
			wg.Done()
		}
	}()
	startTimestamp[id] = time.Now().UnixNano()

	// 创建容器
	containerId, err := docker_bench.CreateContainer(cli, id, networkMode)
	if err != nil {
		return
	}

	if err := docker_bench.StartContainer(cli, containerId); err != nil {
		return
	}

	log.Printf("create container %d ok\n", id)
}

func collectData(cli *client.Client, containerList []types.Container) {
	resultChan := make(chan string, len(containerList))

	for _, container := range containerList {
		go func(c types.Container) {
			getEndTime(cli, &c, resultChan)
		}(container)
	}

	resultData := "index, start, end, duration\n"
	for i := 0; i < len(containerList); i++ {
		select {
		case line := <-resultChan:
			resultData += line
		}
	}

	resultFileName := "docker-"
	//if parallel {
	//	resultFileName += "parallel-"
	//}
	resultFileName += strconv.Itoa(count) + ".csv"
	docker_bench.SaveToFile(resultData, prefixPath, resultFileName)
}

func getEndTime(cli *client.Client, container *types.Container, resultChan chan<- string) {
	// 获取 index
	name := container.Names[0]
	arr := strings.Split(name, "-")
	index, err := strconv.Atoi(arr[1])
	if err != nil {
		log.Printf("collectData[%s] parse index error: %+v\n", container.Names[0], err)
		resultChan <- "-1, -1, -1, -1"
		return
	}

	// 获取输出的时间
	containerLog, err := docker_bench.ReadContainerLog(cli, container.ID)
	if err != nil {
		resultChan <- fmt.Sprintf("%d, %d, %d, %d\n", index, startTimestamp[index], -1, -1)
		return
	}
	containerLog = strings.ReplaceAll(containerLog, "\n", "")
	containerLog = strings.ReplaceAll(containerLog, "\r", "")

	// 格式化输出的时间
	endTimeStamp, err := strconv.ParseInt(containerLog, 10, 64)
	if err != nil {
		log.Printf("collectData[%s] parse end time error: %+v\n", container.Names[0], err)
		resultChan <- fmt.Sprintf("%d, %d, %s, %d\n", index, startTimestamp[index], containerLog, -1)
		return
	}

	startStr := strconv.FormatInt(startTimestamp[index], 10)[6:]
	containerLog = containerLog[6:]
	content := fmt.Sprintf("%d, %s, %s, %d\n", index, startStr, containerLog, (int)(endTimeStamp/1e6-startTimestamp[index]/1e6))
	fmt.Printf(content)
	resultChan <- content
}
