import bz2
input_file_name = 'enwiki-20150112-400-r100-10576.txt.bz2'
output_file_name = 'corpus80.txt'

with bz2.open(input_file_name, 'rt') as data_file, open(output_file_name, mode='wt') as out_file:
    for line in data_file:
        tokens = []
        for chunk in line.split(' '):
            token = chunk.strip().strip('.,!?;:()[]\'"')
            if len(token) > 0:
                tokens.append(token)

        print(*tokens, sep=' ', end='\n', file = out_file)
