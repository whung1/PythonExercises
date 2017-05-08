"""
Given a list of sorted, increasing numbers in a sequence of +1 from n to m, one is missing. 

Return the missing number in this sequence in O(log n)
"""


def get_missing_num_in_sequence(arr):
    """
    Binary search modified implementation to find missing sequence number.
    
    :param arr:  
    :return: 
    """
    start = arr[0]
    start_index = 0
    end = arr[-1]
    end_index = len(arr) - 1
    while end_index-start_index != 1 and start-end != 1:  # can only end when the number between is the missing sequence
        temp_index = int((start_index + end_index) / 2)
        temp = arr[temp_index]
        supposed = start + (temp_index - start_index)
        if temp <= supposed:  # left side will confirm all correct sequences
            start = temp
            start_index = temp_index
        if temp > supposed:  # right side will confirm all mismatched sequences
            end = temp
            end_index = temp_index
    return start+1

if __name__ == '__main__':
    print(get_missing_num_in_sequence([6, 7, 8, 9, 10, 12, 13, 14]))
    print(get_missing_num_in_sequence([6, 7, 8, 9, 10, 11, 12, 14]))
    print(get_missing_num_in_sequence([6, 7, 9, 10, 11, 12, 13, 14]))
    print(get_missing_num_in_sequence([1, 3, 4, 5, 6, 7, 8, 9]))
