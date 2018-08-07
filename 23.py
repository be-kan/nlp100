import gzip
import json
import re

fname = 'jawiki-country.json.gz'


def extract_UK():
    with gzip.open(fname, 'rt') as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']

    raise ValueError('イギリスの記事が見つからない')


# 正規表現のコンパイル
pattern = re.compile(r'''^(={2,})\s*(.+?)\s*\1.*$''', re.MULTILINE)
result = pattern.findall(extract_UK())

for line in result:
    level = len(line[0]) - 1
    print('{indent}{sect}({level})'.format(
        indent='\t' * (level - 1), sect=line[1], level=level))
