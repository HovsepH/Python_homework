import multiprocessing
import helpers

def process_file_processes(file_path):
    with open(file_path, 'r') as file:
        file_size = len(file.read())
    
    result_queue = multiprocessing.Queue()
    num_processes = 4
    chunk_size = file_size // num_processes
    
    processes = []
    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_processes - 1 else file_size
        process = multiprocessing.Process(target=helpers.count_words_in_chunk, args=(start, end, file_path, result_queue))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()

    final_counts = helpers.aggregate_results(result_queue)
    
    return final_counts
