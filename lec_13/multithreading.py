import helpers
import threading
import queue
import threading

def process_file_processes(file_path):
    with open(file_path, 'r') as file:
        file_size = len(file.read())
    
    result_queue = queue.Queue()
    num_threads = 4
    chunk_size = file_size // num_threads
    
    threads = []
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else file_size
        thread = threading.Thread(target=helpers.count_words_in_chunk, args=(start, end, file_path, result_queue))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    final_counts = helpers.aggregate_results(result_queue)
    
    return final_counts
