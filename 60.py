import json
import redis


def enumKv():
    with open('artist.json', 'r', encoding='utf8') as fin:
        for line in fin:
            jsd = json.loads(line)
            if 'area' in jsd:
                yield jsd['name'], jsd['area']


def register():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.flushdb()
    for k, v in enumKv():
        r.set(k, v)
    r.save()


def main():
    register()


if __name__ == '__main__':
    main()
