num_distinct_chars = 14

with open('input.txt', 'r') as comm_stream:
    buffer_chars = comm_stream.read(num_distinct_chars - 1)

    for char_ptr, char in enumerate(comm_stream.read()):
        test_chars = buffer_chars + char
        
        if len(set(test_chars)) == num_distinct_chars:
            print(char_ptr + num_distinct_chars)
            break

        buffer_chars = test_chars[1:]

        