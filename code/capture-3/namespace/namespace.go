package main

import "os"

/**
 * namespace 创建性能测试
 *
 */
import (
	"context"
	"fmt"
	"log"
	"strconv"
	"sync"
	"syscall"
	"time"
)

var namespaces = []uintptr{syscall.CLONE_NEWUSER, syscall.CLONE_NEWNS, syscall.CLONE_NEWUTS, syscall.CLONE_NEWIPC, syscall.CLONE_NEWNET}

func doStartProcess(namespace int) *os.Process {
	// 创建子进程
	sys := &syscall.SysProcAttr{Cloneflags: syscall.CLONE_NEWPID}
	if namespace != -1 {
		sys.Cloneflags = sys.Cloneflags | namespaces[namespace]
	}
	process, err := os.StartProcess("/go/src/wait", []string{}, &os.ProcAttr{
		Sys: sys,
	})
	if err != nil {
		fmt.Println("StartProcess:", err)
	}
	return process
}

func newProcess(ctx context.Context, wgCreate, wgWait *sync.WaitGroup, namespace int) {
	// 开始计时
	start := time.Now()

	process := doStartProcess(namespace)

	// 打印创建的时间
	fmt.Println(time.Now().Sub(start).Milliseconds())

	// 创建完成
	wgCreate.Done()

	// 等待超时以后发终止信号
	<-ctx.Done()
	if err := process.Signal(syscall.SIGINT); err != nil {
		fmt.Println("Signal error:", err)
	}
	// 清理子进程
	if _, err := process.Wait(); err != nil {
		log.Println("Wait error:", err)
	}
	// 结束
	wgWait.Done()
}

var N = 1
var namespace = -1
var timeout = 15

// 并发数，启用的namespace，超时时间
func initArgs() {
	if len(os.Args) > 3 {
		if n, err := strconv.Atoi(os.Args[1]); err != nil {
			log.Fatal(err)
		} else {
			N = n
		}

		if n, err := strconv.Atoi(os.Args[2]); err != nil {
			log.Fatal(err)
		} else {
			namespace = n
		}

		if n, err := strconv.Atoi(os.Args[3]); err != nil {
			log.Fatal(err)
		} else {
			timeout = n
		}
	}
}

func main() {
	initArgs()

	ctx, _ := context.WithTimeout(context.Background(), time.Duration(timeout)*time.Second)

	wgCreate := sync.WaitGroup{}
	wgCreate.Add(N)

	wgWait := sync.WaitGroup{}
	wgWait.Add(N)

	for i := 0; i < N; i++ {
		go newProcess(ctx, &wgCreate, &wgWait, namespace)
	}
	wgCreate.Wait()
	fmt.Printf("create %d process ok, wait process exit!\n", N)
	wgWait.Wait()
}
