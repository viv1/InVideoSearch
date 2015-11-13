from subprocess import call

#utility func1 to input keyword from user
def inputKeyword():

	return raw_input("Enter key to search in the video: ")

#utility func2 to search for keyword in subtitle file
#returns the list of times where keyword is present
def SearchOccurences(key):
	time=[]
	with open("/home/vivek/Downloads/matrix1999.srt") as subfile:
		data=subfile.read()
		#Preprocess data
		data=data.lower()	#convert all to lower(Case insensitive search)
		# convert 're to are, etc.
		#search for keyword
		mc=re.findall(r'(\d+:\d+:\d+,\d+) --> (\d+:\d+:\d+,\d+)([\r\n.\w\s]+)',data)
		#start time=mc[5][0] and end time=mc[5][1] and sub= mc[5][2]
		for i in xrange(1300):
			if "neo" in mc[i][2]:
				print mc[i][2]
		#for word in re.findall('\w+', data):
		#	print word


	return time

#utility func3 to start video
def startVid(time):

	call(["vlc", "--start-time",time,"/home/vivek/Downloads/matrix1999.mp4"])
	
#starts video at 720 secs

if __name__ == '__main__':
	keyToSearch=inputKeyword()
	timesList=SearchOccurences(keyToSearch)
	for i in timesList:
		startVid(i)
		nextK=raw_input()
		if nextK is "N":
			continue
		else:
			break

