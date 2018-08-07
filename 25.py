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


pattern = re.compile(r'''^\{\{基礎情報.*?$(.*?)^\}\}$''', re.MULTILINE + re.DOTALL)
contents = pattern.findall(extract_UK())
pattern = re.compile(r'''^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|((?=\n$)))''', re.MULTILINE + re.DOTALL)

fields = pattern.findall(contents[0])

result = {}
keys_test = []
for field in fields:
    result[field[0]] = field[1]
    keys_test.append(field[0])

for item in sorted(result.items(), key=lambda field: keys_test.index(field[0])):
    print(item)
