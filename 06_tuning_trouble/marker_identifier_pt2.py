num_distinct_chars = 14

with open('input.txt', 'r') as comm_stream:
    marker_found = False
    buffer_chars = comm_stream.read(num_distinct_chars - 1)

    for char_ptr, char in enumerate(comm_stream.read()):
        test_chars = buffer_chars + char

        for char_ptr_1, char_1 in enumerate(buffer_chars):
            if char_1 in test_chars[char_ptr_1 + 1:]:
                break
            elif char_ptr_1 == len(buffer_chars) - 1:
                marker_found = True
                break
        
        if marker_found:
            print(char_ptr + num_distinct_chars)
            break

        buffer_chars = test_chars[1:]

        