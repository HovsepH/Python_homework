from collections import Counter

def count_words_in_chunk(start, end, file_path, result_queue):
    word_count = Counter()
    with open(file_path, 'r') as file:
        file.seek(start)
        for line in file.read(end - start).splitlines():
            words = line.split()
            word_count.update(words)
    result_queue.put(word_count)

def aggregate_results(result_queue):
    total_count = Counter()
    while not result_queue.empty():
        word_count = result_queue.get()
        total_count.update(word_count)
    return total_count