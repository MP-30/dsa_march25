import multiprocessing
import math
import time

def gpu_stress():
    try:
        import cupy as cp
        print("GPU stress started using CuPy...")
        while True:
            a = cp.random.rand(10000, 10000)
            b = cp.dot(a, a)
            del a, b
            cp._default_memory_pool.free_all_blocks()
    except ImportError as e:
        print("CuPy failed:", e)

def cpu_stress():
    while True:
        math.sqrt(math.pi ** 5.3)

if __name__ == "__main__":
    print("Starting CPU and GPU stress test. Press Ctrl+C to stop.")
    
    num_cores = multiprocessing.cpu_count()
    processes = []

    for _ in range(num_cores):
        p = multiprocessing.Process(target=cpu_stress)
        p.start()
        processes.append(p)

    gpu_proc = multiprocessing.Process(target=gpu_stress)
    gpu_proc.start()
    processes.append(gpu_proc)

    for p in processes:
        p.join()
