import argparse
import random
from math import gcd


def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def generate_prime():
    for x in range(random.randint(10**8 + 1, 10**9), 10**10):
        if is_prime(x):
            return x
    return 10**9 + 7


def extended_euclid(e, m):
    if e == 0:
        return 0, 1
    (d1, y1) = extended_euclid(m % e, e)
    return y1 - (m // e) * d1, d1


def generate_ed(m):
    e = random.randint(2, m)
    while gcd(e, m) != 1:
        e = random.randint(2, m)
    (d, y) = extended_euclid(e, m)
    d = (d % m + m) % m
    return e, d


def generate_keys():
    p = generate_prime()
    q = generate_prime()
    assert (is_prime(p))
    assert (is_prime(q))
    n = p * q
    m = (p - 1) * (q - 1)
    e, d = generate_ed(m)
    assert (e * d % m == 1)
    return (e, n), (d, n)


def pow_mod(x, power, n):
    if power == 0:
        return 1
    if power % 2 == 1:
        return x * pow_mod(x, power - 1, n) % n
    t = pow_mod(x, power // 2, n)
    return t * t % n


def encrypt(e, n, input, output):
    text = input.read()
    res = ""
    for c in text:
        res += str(pow_mod(ord(c), e, n)) + "\n"
    output.write(res)


def decrypt(d, n, input, output):
    res = ""
    for line in input.readlines():
        line = line.rstrip()
        res += chr(pow_mod(int(line), d, n))
    output.write(res)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    prog='RSA algorithm',
                    description='Generates public/private keys + encodes/decodes text')

    parser.add_argument('-a', '--action', choices=['generate', 'encrypt', 'decrypt'], help='Choose type of action')
    parser.add_argument('-k', '--key', type=str, help='key )for encoding/decoding')
    parser.add_argument('-i', '--input', type=argparse.FileType('r'), help='input file')
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), help='output file')

    args = parser.parse_args()

    if args.action == 'generate':
        keys = generate_keys()
        print("public key:", keys[0][0], ",", keys[0][1])
        print("private key:", keys[1][0], ",", keys[1][1])
    elif args.action == 'encrypt':
        if args.key is None:
            print("arguments should contain public key")
            exit(0)
        key = args.key.strip()
        numbers = key.split(",")
        if len(numbers) != 2:
            print("wrong public key")
            exit(0)
        e = int(numbers[0])
        n = int(numbers[1])
        if e is None or n is None:
            print("wrong public key")
        if args.input is None or args.output is None:
            print("arguments should contain input and output file")
        encrypt(e, n, args.input, args.output)
    else:
        if args.key is None:
            print("arguments should contain public key")
            exit(0)
        key = args.key.strip()
        numbers = key.split(",")
        if len(numbers) != 2:
            print("wrong public key")
            exit(0)
        d = int(numbers[0])
        n = int(numbers[1])
        if d is None or n is None:
            print("wrong public key")
        if args.input is None or args.output is None:
            print("arguments should contain input and output file")
        decrypt(d, n, args.input, args.output)

