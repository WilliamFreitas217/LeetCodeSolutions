def invert_string_list(s: list):
    index_left = 0
    index_right = len(s) - 1
    while index_left < index_right:
        s[index_left], s[index_right] = s[index_right], s[index_left]
        index_left += 1
        index_right -= 1
    return s
