def reverse_generator(sequence):
    seq_list = list(sequence)
    for i in range(len(seq_list) - 1, -1, -1):
        yield seq_list[i]