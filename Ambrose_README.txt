Ambrose Readme
-	This is assuming no amendments have been made to code

01.	Downloading Python on Kali Linux (you shouldnt be needing this)
-	sudo apt update -y
-	sudo apt install python3 -y
-	python --version

02.	Getting Python3-PIP on Kali Linux (dk if this works)
-	sudo apt install python3-wheel -y
-	sudo apt install ca-certificates -y
-	sudo apt install python3-pip

03.	Python3-pip installation format on Kali Linux
-	pip install <dependency_name>	-> pip install pydub OR pip3 install pydub

04.	For the Audio Transcribe:
-	Install the following Python libraries: pydub, googletrans, speech_recognition, ffmpeg

	Audio Transcribe: Parts you can edit
	-	Line 08:	Output File Name[e.g. '/new_file.txt' -> '/another_audio_transcribe.txt']
	-	Line 68:	Input File		
		[input file acts with respect to where 
		THIS FILE is (e.g. samples/song.mp3 means that THIS FILE is in the same location as the sample folder), 
		else just use a full path (e.g. 'C:/Users/User/AppData/Local/Tesseract-OCR/tesseract.exe' )]

	-	Line 69:	Output Folder	[refer to above ^, same verbiage]
	-	Line 70:	Input Language	[Google Language Codes are in https://readthedocs.org/projects/py-googletrans/downloads/pdf/latest/ under googletrans.LANGUAGES]
	-	Line 71:	Output Language [refer to above ^, same verbiage]
	
05.	For the Image Transcribe:
-	Install the following Python libraries:	pytesseract
	-	This library is a little tricky: you need to actually install it in your com first
	-	Using Windows, you can ust get the Installer here: https://github.com/UB-Mannheim/tesseract/wiki
	-	[Untested] you can just install everything using Linux with this command: 
		sudo apt-get update && sudo apt-get install tesseract-ocr
	
	Image Transcribe: Parts you can edit
	-	Line 08:	Tesseract-OCR path	[just follow the format, only edit text inside the '...']
	-	Line 12:	...Image.open('Your/Image/File'), lang = 'language_code'...
	get language code from https://www.kaggle.com/code/dhorvay/pytesseract-function-parameters under 'lang'
	also accepts vertical arrangements
	-	Line 14: 	Output Text filename

06.	LIMITATIONS	(meaning it should work in this scenario no problem):
-	Audio:	One speaker at a time, unobstructed by noise/music, clear voice	-> a speech
-	Image:	Greyscale, one type of language format (chinese_text and chinese_vertical_text are DIFFERENT), (chinese_text and latin_text are DIFFERENT)