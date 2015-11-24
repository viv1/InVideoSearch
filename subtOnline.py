"""
We are using subDB for downloading subtitles
GET and POST protocols of HTTP are cool and python requests rocks!!
"""
import os
import hashlib
import requests

def getHash(name):
	with open(name,'rb') as f:
		readsize=64*1024
		size=os.path.getsize(name)
		data=f.read(readsize)
		f.seek(-readsize,os.SEEK_END)
		data +=f.read(readsize)
	return hashlib.md5(data).hexdigest()


def getSub(movieHash):
	headers={
		'User-Agent':'SubDB/1.0 ()',
	}
	re=requests.get('http://api.thesubdb.com/?action=download&hash='+movieHash+'&language=en',headers=headers)
	return re.text


def createSubFile(subText):
	with open('matrix.srt','w') as f:
		f.write(subText.encode('utf-8'))
		"""
		If you want to remove non ascii characters, use:
		"""
		#f.write(subText.encode('ascii', 'ignore').decode('ascii'))


def main():
	name='matrix.mp4'
	movieHash=getHash(name)
	subText=getSub(movieHash)
	createSubFile(subText)
	#print movieHash


main()