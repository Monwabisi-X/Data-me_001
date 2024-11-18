# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    # Implement this
    return lst[::-1]

def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    # Implement this
    element_count = 0
    for i in lst:
        if i == element:
            element_count += 1
    
    return element_count

def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    # Implement this
    keys_list = []
    for key, value_ in dct.items():
        if dct[key] == value:
            keys_list.append(key)

    return keys_list

def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    # Implement this
    lst3 = sorted(lst1 + lst2)
    return lst3

def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    # Implement this
    count_rep = 0
    for i in range(0, len(numbers)-1):
        if numbers[i] == numbers[i + 1]:
            count_rep += 1
    if count_rep == len(numbers)-1:
        return None
    else:
        max_ = max(numbers)
        numbers.remove(max_)
        return max(numbers)

def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    # Implement this
    count_rep = 0
    if len(str1) == len(str2):
        for i in str1:
            if i in str2:
                count_rep += 1
        if count_rep == len(str1):
            return True
        else: return False
    else: return False

def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    # Implement this
    flat_list = []
    for i in nested_list:
        for n in i:
            flat_list.append(n)
    
    return flat_list

def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    # Implement this
    lst1 = []
    for i in lst:
        if i not in lst1:
            lst1.append(i)
    return lst1

def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    # Implement this
    common = []
    for i in lst1:
        if i in lst2:
            common.append(i)

    return common