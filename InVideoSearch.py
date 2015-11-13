from subprocess import call
import re
import sys


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
def startVid(time):
	Times=re.findall(r'(\d+):(\d+):(\d+),(\d+)',time)
	
	startTime=3600*int(Times[0][0])+60*int(Times[0][1])+int(Times[0][2])-2	# starts vid 2 sec earlier

	call(["vlc", "--start-time",str(startTime),"/home/vivek/Downloads/matrix1999.mp4"])
	
#starts video at 720 secs


def main():

	dict=[]	#Dictionary to store start time, end time and subtitle texts

	fileName=str(sys.argv[1:][0])	#passing subtitle name as argument
	dict=preProcess(fileName)
	keyToSearch=inputKeyword()

	timesList=SearchOccurences(keyToSearch,dict)
	print timesList
	for i in timesList:
		startVid(i)
		nextK=raw_input()
	 	# if nextK is "N":
	 	# 	continue
	 	# else:
	 	# 	break

if __name__ == '__main__':
	main()