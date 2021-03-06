import os.path
from subprocess import call
import re
import sys
import subprocess
from subtOnline import *

# To do:
"""	Need to make python 3 compatible
1. print statements
2. input statements
3. requests calls

Make these changes in other files too.	
"""

replacement_patterns = [
(r'won\'t', 'will not'),
(r'can\'t', 'cannot'),
(r'i\'m', 'i am'),
(r'ain\'t', 'is not'),
(r'(\w+)\'ll', '\g<1> will'),
(r'(\w+)n\'t', '\g<1> not'),
(r'(\w+)\'ve', '\g<1> have'),
(r'(\w+)\'s', '\g<1> is'),
(r'(\w+)\'re', '\g<1> are'),
(r'(\w+)\'d', '\g<1> would')
]


#REPLACEMENT
class RegexpReplacer(object):
	def __init__(self, patterns=replacement_patterns):
		self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]

	def replace(self, text):
		s = text
		for (pattern, repl) in self.patterns:
			s = re.sub(pattern, repl, s)
		return s


#utility func to input keyword from user
def inputKeyword():
	return raw_input("Enter key to search in the video: ")

#utility func to search for keyword in subtitle file
#returns the list of times where keyword is present
def SearchOccurences(key,dict):
	time=[]
	print len(dict)
	#start time=dict[5][0] and end time=dict[5][1] and sub= dict[5][2]
	for i in xrange(len(dict)):
		if key in dict[i][2]:
			time.append(dict[i][0])
			#print dict[i][0]

	return time 	#in hh:mm:ss,ms format


#utility func to preprocess subtitle file
def preProcess(fileName):
	with open(fileName) as subfile:
		data=subfile.read()
		#Preprocess data
		data=data.lower()	#convert all to lower(Case insensitive search)
	
		# convert 're to are, etc.
		replacer=RegexpReplacer()
		data=replacer.replace(data)

		#search for keyword
		dict=re.findall(r'(\d+:\d+:\d+,\d+) --> (\d+:\d+:\d+,\d+)([\r\n.\,\w\s]+)',data)
		return dict

#utility func to start video
def startVid(time,SubfileName):
	Times=re.findall(r'(\d+):(\d+):(\d+),(\d+)',time)
	
	startTime=3600*int(Times[0][0])+60*int(Times[0][1])+int(Times[0][2])-1	# starts vid 1 sec earlier

	#Vidprocess=call(["vlc", "--start-time",str(startTime),"/home/vivek/Downloads/matrix1999.mp4", "&"])
	Vidprocess = subprocess.Popen(["vlc", "--start-time",str(startTime),"--sub-file",SubfileName,sys.argv[1:][0], "&"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	return Vidprocess
	


def main():

	dict=[]	#Dictionary to store start time, end time and subtitle texts

	#Video formats

	vidFormats=[".avi", ".mp4"]
	
	if len(sys.argv)>1:
		MoviefileName=str(sys.argv[1:][0])	#passing movie name as argument
	else:
		MoviefileName=""
		while not MoviefileName:
			MoviefileName=raw_input("Please enter movie name: ")

	for i in vidFormats:
		SubfileName=MoviefileName.replace(i,".srt")
		
	if not os.path.isfile(SubfileName):		
		resp=raw_input("need to get online. Should we?(Y/N)")
		if(resp is "Y"):

			"""
			Calling functions from subtOnline module
			"""
			movieHash=getHash(MoviefileName)	#get Movie Hash
			subText=getSub(movieHash)			#get Subtitle from Hash
			createSubFile(subText,SubfileName)	#create subtitle file

		else:
			sys.exit("Exiting program since no source of Subtitle")

	else:
		pass
		#print "file already in local"	
	#Find subfileName in the directory
	"""
	Currently subfile name should be same as movie name
	Better ways to implement:
		1.ask the user for subfile name
		2.use subtitle finder API and download subfile
		3.ofcourse, keep the existing implementation too

	Priority 1>3>2
	"""
	dict=preProcess(SubfileName)
	keyToSearch=inputKeyword()

	procId=0	#process id initialization

	timesList=SearchOccurences(keyToSearch,dict)
	#print timesList
	for i in timesList:
		if procId:
			procId.kill()
		procId=startVid(i,SubfileName)
		nextK=raw_input("Enter N to go to next scene with key: ")
	 	if nextK is "N":
	 		continue
	 	else:
	 		if procId:
				procId.kill()
	 		break

if __name__ == '__main__':
	main()
