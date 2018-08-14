import redis


def enumKeys():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    v = r.get('The Silhouettes').decode()
    print(v)
    v = r.get('The Wanderers').decode()
    print(v)
    v = r.get('桑田佳祐').decode()
    print(v)


def main():
    enumKeys()


if __name__ == '__main__':
    main()
