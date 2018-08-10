fname_input = 'questions-words.txt'
fname_output = 'family.txt'

with open(fname_input, 'rt') as data_file, open(fname_output, 'wt') as out_file:
    target = False
    for line in data_file:
        if target is True:
            if line.startswith(': '):
                break
            print(line.strip(), file=out_file)

        elif line.startswith(': family'):
            target = True
