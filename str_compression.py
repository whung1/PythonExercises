"""
Given a string, compress it based on how many instances of it reoccurs
"""

def str_compress(cur_str):
    if not cur_str:
        return ""
    current_char = ""
    current_count = 0
    compressed_str = ""
    for i in range(len(cur_str)):
        if current_char != cur_str[i]:
            compressed_str += current_char + (str(current_count) if current_count > 1 else "")
            current_char = cur_str[i]
            current_count = 0
        current_count += 1
    compressed_str += current_char + (str(current_count) if current_count > 1 else "")
    return compressed_str

if __name__ == "__main__":
    """
    Example:
    Input: 'aaaaabbbdddccclop'
    Output: 'a5b3d3c3lop'
    """

    print(str_compress('aaaaabbbdddccclop'))
