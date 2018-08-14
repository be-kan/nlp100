import redis


def main():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    keys = r.scan_iter()
    count = 0

    for key in keys:
        v = r.get(key)
        if v == b'Japan':
            count += 1

    print(count)


if __name__ == '__main__':
    main()
