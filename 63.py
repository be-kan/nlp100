import json
import redis


def main():
    r = redis.StrictRedis(host='localhost', port=6379, db=1)
    r.flushdb()

    with open('artist.json', 'r', encoding='utf8') as fin:
        for line in fin:
            jsd = json.loads(line)
            if 'tags' in jsd:
                r.set(jsd['name'], json.dumps(jsd['tags']))

    r.save()

    name = '桑田佳祐'
    v = r.get(name)
    if v is not None:
        print('*' + name)
        tags = json.loads(v.decode())
        for tag in tags:
            print("{}\t{}".format(tag['value'], tag['count']))


if __name__ == '__main__':
    main()
