Ambrose Readme
-	This is assuming no amendments have been made to code

01.	Downloading Python on Kali Linux (prolly alr installed)
-	sudo apt update -y
-	sudo apt install python3 -y
-	python --version

02.	Getting Python3-PIP on Kali Linux (prolly alr installed)
-	sudo apt install python3-wheel -y
-	sudo apt install ca-certificates -y
-	sudo apt install python3-pip

03.	Python3-pip installation format on Kali Linux
-	pip install <dependency_name>	-> pip install pydub OR pip3 install pydub

04.	For the Audio Transcribe:
-	pip3 install 
	-	pydub 
	-	-U deep-translator 
	-	speech_recognition 
	-	ffmpeg (shouldnt be necessary if you install pydub first)

	
05.	For the Image Transcribe:
-	Install the following Python libraries:	pytesseract
	-	you can just install everything using Linux with this command: 
		sudo apt-get update && sudo apt-get install tesseract-ocr
	
	Image Transcribe: Parts you can edit
	-	Line 08:	Tesseract-OCR path	[just follow the format, only edit text inside the '...']
	-	Line 12:	...Image.open('Your/Image/File'), lang = 'language_code'...
	get language code from https://www.kaggle.com/code/dhorvay/pytesseract-function-parameters under 'lang'
	also accepts vertical arrangements
	-	Line 14: 	Output Text filename

06.	LIMITATIONS	(meaning it should work in this scenario no problem):
-	Audio:	One speaker at a time, unobstructed by noise/music, clear voice	-> a speech
-	Audiometric: Using Netflix Godzilla Minus One trailer, the algo got 8/12 right (60%)
-	Image:	Greyscale, one type of language format (chinese_text and chinese_vertical_text are DIFFERENT), (chinese_text and latin_text are DIFFERENT)
