#!/usr/bin/python
import struct
from Crypto.Cipher import AES
import sys

KEY = b'iwp2390x-e]57kx&#@*(ca,sfkf!eu+$'
IV = b'fiw;opdd40382,*&'
OUT = '%s.aes'

def encrypt(settings):
    """Encrypt Optus Sagemcom F@st 3864 AES 56 CBC encrypted configuration file."""
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    with open(settings, 'rb') as infile:
        filebytes = infile.read()

    with open(OUT % settings, 'wb') as outfile:
        # first 4 bytes of the file is the length of the final clear text minus the padding
        cleartext_length = len(filebytes)
	print(cleartext_length)
        # encryption is padded to 16 bytes
        padding_length = 16 - (cleartext_length % 16)
	print(padding_length)
        cleartext_length = struct.pack(">I", cleartext_length)
        outfile.write(cleartext_length)
        outfile.write(cipher.encrypt(filebytes + b'\0' * padding_length))

if __name__ == '__main__':
    try:
        encrypt(sys.argv[1])
    except IndexError:
        print("usage: %s <settings file>" % sys.argv[0])
        sys.exit(2)
