# Built-in
import binascii
import os


if __name__ == '__main__':
    print(binascii.b2a_hex(os.urandom(5)).decode('ascii'))
