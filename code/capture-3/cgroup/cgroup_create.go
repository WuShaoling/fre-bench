package main

import (
	"fmt"
	"github.com/containerd/cgroups"
	"github.com/opencontainers/runtime-spec/specs-go"
	"log"
	"os"
	"strconv"
	"sync"
	"time"
)

func createCGroup(i int, wg *sync.WaitGroup) {
	begin := time.Now().UnixNano() / 1e6

	shares := uint64(100)
	control, err := cgroups.New(
		cgroups.V1,
		cgroups.StaticPath("/test_"+strconv.FormatInt(begin, 10)+"_"+strconv.Itoa(i)),
		&specs.LinuxResources{CPU: &specs.LinuxCPU{Shares: &shares}},
	)
	if err != nil {
		log.Fatal(err)
	}

	end := time.Now().UnixNano() / 1e6
	fmt.Println(end - begin)

	_ = control.Delete()
	wg.Done()
}

func main() {
	N := 1
	if len(os.Args) > 1 {
		if n, err := strconv.Atoi(os.Args[1]); err != nil {
			log.Fatal(err)
		} else {
			N = n
		}
	}

	wg := &sync.WaitGroup{}
	wg.Add(N)
	for i := 0; i < N; i++ {
		go createCGroup(i, wg)
	}
	wg.Wait()
}
