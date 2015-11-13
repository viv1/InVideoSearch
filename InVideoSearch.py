from subprocess import call
import re

dict=[]	#Dictionary to store start time, end time and subtitle texts

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


#utility func1 to input keyword from user
def inputKeyword():
	return raw_input("Enter key to search in the video: ")

#utility func to search for keyword in subtitle file
#returns the list of times where keyword is present
def SearchOccurences(key):
	time=[]
	
	#start time=mc[5][0] and end time=mc[5][1] and sub= mc[5][2]
	for i in xrange(len(dict)):
		if key in dict[i][2]:
			print dict[i][2]
	#for word in re.findall('\w+', data):
	#	print word


	return time

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

#utility func3 to start video
def startVid(time):

	call(["vlc", "--start-time",time,"/home/vivek/Downloads/matrix1999.mp4"])
	
#starts video at 720 secs

#REPLACEMENT
class RegexpReplacer(object):
	def __init__(self, patterns=replacement_patterns):
		self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]

	def replace(self, text):
		s = text
		for (pattern, repl) in self.patterns:
			s = re.sub(pattern, repl, s)
		return s

def main():

	fileName="/home/vivek/Downloads/matrix1999.srt"
	preProcess(fileName)
	keyToSearch=inputKeyword()

	timesList=SearchOccurences(keyToSearch)
	for i in timesList:
		startVid(i)
		nextK=raw_input()
		if nextK is "N":
			continue
		else:
			break

if __name__ == '__main__':
	main()