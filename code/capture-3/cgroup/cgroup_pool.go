package main

import (
	"github.com/containerd/cgroups"
	"github.com/opencontainers/runtime-spec/specs-go"
	"log"
	"os"
	"strconv"
	"sync"
	"time"
)

type CGroupPool struct {
	pool  []*cgroups.Cgroup
	mutex sync.Mutex
}

func NewCGroupPool(n int) (*CGroupPool, error) {
	instance := &CGroupPool{
		pool: make([]*cgroups.Cgroup, 0, n),
	}

	prefix := "/test_" + strconv.FormatInt(time.Now().UnixNano(), 10) + "_"
	for i := 0; i < n; i++ {
		control, err := cgroups.New(
			cgroups.V1,
			cgroups.StaticPath(prefix+strconv.Itoa(i)),
			&specs.LinuxResources{CPU: &specs.LinuxCPU{}},
		)
		if err != nil {
			log.Println("NewCGroupPool error:", err)
			return nil, err
		}
		instance.pool = append(instance.pool, &control)
	}

	return instance, nil
}

func (pool *CGroupPool) Get() *cgroups.Cgroup {
	pool.mutex.Lock()
	defer pool.mutex.Unlock()

	n := len(pool.pool)
	if n == 0 {
		return nil
	}

	c := pool.pool[n-1]
	pool.pool = pool.pool[0 : n-1]
	return c
}

func (pool *CGroupPool) GiveBack(c *cgroups.Cgroup) {
	pool.mutex.Lock()
	defer pool.mutex.Unlock()
	pool.pool = append(pool.pool, c)
}

func (pool *CGroupPool) GetAndUpdate() *cgroups.Cgroup {
	c := pool.Get()
	var cpuShares uint64 = 1000
	var memLimit int64 = 1e6

	_ = (*c).Update(&specs.LinuxResources{
		CPU: &specs.LinuxCPU{
			Shares: &cpuShares,
		},
		Memory: &specs.LinuxMemory{
			Limit: &memLimit,
		},
	})
	return c
}

func (pool *CGroupPool) Clear() {
	for i := 0; i < len(pool.pool); i++ {
		_ = (*(pool.pool[i])).Delete()
	}
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

	// 初始化缓存池
	pool, err := NewCGroupPool(N)
	if err != nil {
		log.Fatal(err)
	}

	// 模拟申请和释放操作
	wg := &sync.WaitGroup{}
	wg.Add(N)
	for i := 0; i < N; i++ {
		go func() {
			// TODO 计时
			pool.GetAndUpdate()
			wg.Done()
		}()
	}
	wg.Wait()
}
