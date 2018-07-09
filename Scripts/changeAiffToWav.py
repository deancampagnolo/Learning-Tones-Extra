import os
os.system("ls")
#os.system("ffmpeg -i Piano.ff.A0.aiff A0.wav")
HEADER = "Piano.ff."
EXTENSION = ".aiff"
DESIRED_EXTENSION = ".mp3"
ITERATIONS = 88
notes = ["A","Ab","B","Bb","C","D","Db","E","Eb","F","G","Gb"];

for letter in notes:
	#if(os.path.isfile(HEADER + letter +"0" + EXTENSION)):
	#	os.system("ffmpeg -i " + HEADER + letter + "0" + EXTENSION +
	#	" "+  )
	for i in range(0,9):
		os.system("ffmpeg -ss 00:00:00.05 -t 00:00:05.00 -i "
		 + HEADER + letter + str(i) + EXTENSION +
                " "+  letter.lower() + str(i) + DESIRED_EXTENSION)	
		

		
