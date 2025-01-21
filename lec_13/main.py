import time
import  multithreading
import multiprocess

if __name__ == '__main__':
    start_time = time.time()
    file_path = "large_file.txt"
    word_counts = multithreading.process_file_processes(file_path)
    print(f"Word counts: {word_counts}")
    end_time = time.time()
    time_spent = end_time - start_time
    print(f"Time spent: {time_spent:.2f} seconds")

    start_time = time.time()
    word_counts = multiprocess.process_file_processes(file_path)
    end_time = time.time()
    time_spent = end_time - start_time
    print(f"Word counts: {word_counts}")
    print(f"Time spent: {time_spent:.2f} seconds")
