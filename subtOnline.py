import os
import hashlib
"""
We will be using subDB for downloading subtitles
Need to learn implementing GET and POST protocols of HTTP
"""

#this hash function receives the name of the file and returns the hash code
def get_hash(name):
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()

def main():
	get_hash('matrix.mp4')

main()

