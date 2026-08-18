import os
import time
import threading
import argparse

def write_data(file_path, data_size_gb, chunk_size_mb=1024):
    start_time = time.time()
    total_bytes_to_write = int(data_size_gb * 1024 * 1024 * 1024)
    bytes_written = 0
    try:
        with open(file_path, 'wb') as f:
            while bytes_written < total_bytes_to_write:
                chunk_size_bytes = min(chunk_size_mb * 1024 * 1024, total_bytes_to_write - bytes_written)
                data = os.urandom(chunk_size_bytes)
                f.write(data)
                bytes_written += len(data)
        end_time = time.time()
        duration = end_time - start_time
        speed_gbps = (data_size_gb * 8) / duration if duration > 0 else 0
        print(f"Write: Wrote {data_size_gb:.2f} GB to {file_path} in {duration:.2f} seconds ({speed_gbps:.2f} Gbps)")
    except Exception as e:
        print(f"Write error: {e}")

def read_data(file_path, data_size_gb, chunk_size_mb=1024):
    start_time = time.time()
    total_bytes_to_read = int(data_size_gb * 1024 * 1024 * 1024)
    bytes_read = 0
    try:
        with open(file_path, 'rb') as f:
            while bytes_read < total_bytes_to_read:
                chunk_size_bytes = min(chunk_size_mb * 1024 * 1024, total_bytes_to_read - bytes_read)
                data = f.read(chunk_size_bytes)
                if not data:
                    break
                bytes_read += len(data)
        end_time = time.time()
        duration = end_time - start_time
        speed_gbps = (data_size_gb * 8) / duration if duration > 0 else 0
        print(f"Read: Read {data_size_gb:.2f} GB from {file_path} in {duration:.2f} seconds ({speed_gbps:.2f} Gbps)")
    except FileNotFoundError:
        print(f"Read error: File not found: {file_path}")
    except Exception as e:
        print(f"Read error: {e}")

def delete_files(base_file_name, thread_count):
    for j in range((thread_count + 1) // 2):  # write threads
        try:
            os.remove(base_file_name + f"_{j}")
            print(f"Deleted {base_file_name}_{j}")
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error deleting file {base_file_name}_{j}: {e}")

def drop_caches():
    print("Dropping OS caches to force real disk reads...")
    os.system("sync")
    os.system("echo 3 | sudo tee /proc/sys/vm/drop_caches > /dev/null")

def main():
    parser = argparse.ArgumentParser(description="Perform heavy read and write operations on an SSD.")
    parser.add_argument("--write_file", type=str, default="write_test.bin", help="Path to the write test file.")
    parser.add_argument("--read_file", type=str, default="write_test.bin", help="Path to the read test file.")
    parser.add_argument("--iterations", type=int, default=1, help="Number of read/write iterations.")
    parser.add_argument("--threads", type=int, default=2, help="Number of threads to use for concurrent operations.")
    parser.add_argument("--size_gb", type=float, default=1.0, help="Size of data to read and write in GB.")
    parser.add_argument("--chunk_size_mb", type=int, default=1024, help="Size of each read/write chunk in MB.")

    args = parser.parse_args()

    if args.threads < 1:
        print("Number of threads must be at least 1.")
        return

    for i in range(args.iterations):
        print(f"\n--- Iteration {i + 1} ---")
        write_threads = []
        read_threads = []

        # Start write threads
        for j in range(args.threads // 2 + args.threads % 2):
            thread = threading.Thread(target=write_data, args=(args.write_file + f"_{j}", args.size_gb, args.chunk_size_mb))
            write_threads.append(thread)
            thread.start()

        # Wait for all write threads to complete
        for thread in write_threads:
            thread.join()

        # Drop caches before read
        drop_caches()

        # Start read threads
        for j in range(args.threads // 2):
            thread = threading.Thread(target=read_data, args=(args.read_file + f"_{j}", args.size_gb, args.chunk_size_mb))
            read_threads.append(thread)
            thread.start()

        # Wait for all read threads to complete
        for thread in read_threads:
            thread.join()

        # Clean up
        delete_files(args.write_file, args.threads)

if __name__ == "__main__":
    main()
