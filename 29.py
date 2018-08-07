import gzip
import json
import re
import urllib.parse, urllib.request
fname = 'jawiki-country.json.gz'


def extract_UK():
    with gzip.open(fname, 'rt') as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']

    raise ValueError('イギリスの記事が見つからない')


def remove_markup(target):
    pattern = re.compile(r'''(\'{2,5})(.*?)(\1)''', re.MULTILINE)
    target = pattern.sub(r'\2', target)

    pattern = re.compile(r'''\[\[(?:[^|]*?\|)?([^|]*?)\]\]''', re.MULTILINE)
    target = pattern.sub(r'\1', target)

    pattern = re.compile(r'''\{\{lang(?:[^|]*?\|)*?([^|]*?)\}\}''', re.MULTILINE)
    target = pattern.sub(r'\1', target)

    pattern = re.compile(r'''\[http:\/\/(?:[^\s]*?\s)?([^]]*?)\]''', re.MULTILINE)
    target = pattern.sub(r'\1', target)

    pattern = re.compile(r'''<\/?[br|ref][^>]*?>''', re.MULTILINE)
    target = pattern.sub('', target)

    return target


pattern = re.compile(r'''^\{\{基礎情報.*?$(.*?)^\}\}$''', re.MULTILINE + re.DOTALL)
contents = pattern.findall(extract_UK())

pattern = re.compile(r'''^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|((?=\n$)))''', re.MULTILINE + re.DOTALL)
fields = pattern.findall(contents[0])

result = {}
for field in fields:
    result[field[0]] = remove_markup(field[1])

fname_flag = result['国旗画像']
url = 'https://www.mediawiki.org/w/api.php?' \
    + 'action=query' \
    + '&titles=File:' + urllib.parse.quote(fname_flag) \
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&iiprop=url'

request = urllib.request.Request(url, headers={'User-Agent': 'NLP100_Python(@segavvy)'})
connection = urllib.request.urlopen(request)

data = json.loads(connection.read().decode())

url = data['query']['pages'].popitem()[1]['imageinfo'][0]['url']
print(url)
