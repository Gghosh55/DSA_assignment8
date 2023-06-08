def compress(chars):
    write = 0
    read = 0
    count = 1
    current_char = chars[0]

    for read in range(1, len(chars)):
        if chars[read] == current_char:
            count += 1
        else:
            chars[write] = current_char
            write += 1
            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    chars[write] = digit
                    write += 1
            count = 1
            current_char = chars[read]

    chars[write] = current_char
    write += 1
    if count > 1:
        count_str = str(count)
        for digit in count_str:
            chars[write] = digit
            write += 1

    return write

chars = ["a","a","b","b","c","c","c"]
print(compress(chars))
print(chars)