
def load_words(filename):
    """
    Loads sorted words list from a file.

    Args:
        filename: The path to the file containing the words.  Each word is 
                  expected to be on a separate line.

    Returns:
        A sorted list of strings, where each string is a word read from the file.
    """
    with open(filename, 'r') as f:
        return sorted([word.strip().lower() for word in f])


def linear_search(sorted_words, word):
    """
    Performs a linear search on a list of words to find the index of a specific word.

    Args:
        sorted_words: A list of strings (words).  While the list name suggests it's sorted,
                      linear search works on unsorted lists as well, though it's generally
                      less efficient for sorted data.
        word: The string (word) to search for.

    Returns:
        The index of the word in the list if found. Returns -1 if the word is not found.
    """
    for i in range(len(sorted_words)):
        if sorted_words[i] == word:
            return i
    return -1


def linear_search_prefix(sorted_words, prefix):
    """
    Performs a linear search on a sorted list of words to find the 
    start and end indices (inclusive) of the range of words that start with a 
    given prefix.

    Args:
        sorted_words: A sorted list of strings (words).
        prefix: The prefix string to search for.

    Returns:
        A tuple containing the start and end indices (inclusive) of the range 
        of words starting with the prefix. Returns (-1, -1) if no words 
        with the given prefix are found.
    """
    # Part 1 - Implement!
    start, end = -1, -1
    for i in range(len(sorted_words)): # for i, word in enumerate(sorted_words):
        if sorted_words[i].startswith(prefix):
            if start == -1:
                start = i
            end = i
        elif start != -1:
            break
            
    return (start,end)


def binary_search(sorted_words, word):
    """
    Performs a binary search on a sorted list of words to find the index of a specific word.

    Args:
        sorted_words: A sorted list of strings (words).
        word: The string (word) to search for.

    Returns:
        The index of the word in the sorted list if found.  Returns -1 if the word is not found.
    """
    low = 0
    high = len(sorted_words) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_words[mid] == word:
            return mid
        elif sorted_words[mid] < word:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_prefix(sorted_words, prefix):
    """
    Given a sorted list of words and a prefix, returns the start and end indices
    (inclusive) of the sublist of words that start with that prefix using 
    a modified binary search approach.

    Args:
        sorted_words: A sorted list of strings (words).
        prefix: The prefix string to search for.

    Returns:
        A tuple containing the start and end indices (inclusive) of the range 
        of words that start with the given prefix. Returns (-1, -1) if no words 
        with the prefix are found.
    """
    # Part 2 - Implement!
  
    def find_start():
        low, high = 0, len(sorted_words)-1
        while low < high:
            mid = (low + high) // 2
            if sorted_words[mid] >= prefix:
                high = mid
            else:
                low = mid + 1
        if sorted_words[low].startswith(prefix):
            return low
        else:
            return -1

    def find_end(start):
        low, high = start, len(sorted_words) - 1
        while low < high:
            mid = (low + high + 1) // 2
            if sorted_words[mid].startswith(prefix):
                low = mid
            else:
                high = mid - 1
        if sorted_words[low].startswith(prefix):
            return low 
        else:
            return -1

    start = find_start()
    if start == -1:
        return -1, -1
    end = find_end(start)
    return start, end
    


def main():
    # Load a list of ~300k words.
    # Feel free to use a shorter list for debugging!
    word_list = load_words('words.txt')

    prefix = input('Enter prefix to find all words starting with it: ')

    
    # Choose which algorithm to use:

    while True:
        print("Choose search method:")
        print("1. Linear Search")
        print("2. Binary Search")
        choice = input("Enter 1 or 2: ")

        if choice == '1':
            print("Using Linear Search")
            start, end = linear_search_prefix(word_list, prefix)
            break
        elif choice == '2':
            print("Using Binary Search")
            start, end = binary_search_prefix(word_list, prefix)
            break
        else:
            print("Not a valid number. Please enter 1 or 2.\n")

    print(f'Result: ({start}, {end})')

    if start == -1:
        print(f'{prefix} is not a prefix of any word!')
        return
    
    print(f"There are {(end-start)+1} words with the prefix: {prefix}")

    valid_range = word_list[start:end+1]
    print(f'These are all of the valid words starting with {prefix}: \n {valid_range}')


main()