# PrefixWordSearch

To run the program, run this command:
python search.py

This program helps you find all of the words with a given prefix. This could be helpful for word games such as Scrabble, whenever you have a complex prefix or simply have trouble forming a word, you can find all words that exist with that given prefix, if there are any. Also for educational purposes only, you can see that it has the option to use either Linear Search or Binary Search. We are working with an input file that contains a sorted list of all words from the English dictionary. So which is better for this case?

If you said Binary Search, you are correct! Here's why: Binary search is much faster than linear search (especially for large datasets) as long as the data is sorted, which is the case for this program. Linear search checks every element one-by-one from start to end, giving it a time-complexity of O(n), whilst binary search repeatedly splits the search space in half, giving it a time-complexity of O(log n), much faster than O(n) in the long run.