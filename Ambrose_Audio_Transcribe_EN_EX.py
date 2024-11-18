#pip install deep_translate

from pydub import AudioSegment
from deep_translator import GoogleTranslator
import speech_recognition as sr
import os

def split_and_transcribe_audio(input_file, output_folder, input_language, chunk_length_ms=60000):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)
    recognizer = sr.Recognizer()

    # Calculate the number of chunks
    num_chunks = len(audio) // chunk_length_ms
    
    # Split the audio into chunks and transcribe each chunk
    for i in range(num_chunks):
        start_time = i * chunk_length_ms
        end_time = (i + 1) * chunk_length_ms
        chunk = audio[start_time:end_time]
        
        # Save the chunk to a file
        chunk_file = f"{output_folder}/chunk_{i + 1}.wav"
        chunk.export(chunk_file, format="wav")
        
        # Transcribe the chunk then translate it
        translate_transcribe(chunk_file, recognizer, i, input_language)
        
    if len(audio) % chunk_length_ms >= 10000:
        #print(len(audio) % chunk_length_ms)
        last_chunk = audio[num_chunks * chunk_length_ms:]

        # Save the chunk to a file
        chunk_file = f"{output_folder}/chunk_{num_chunks + 1}.wav"
        last_chunk.export(chunk_file, format="wav")
        
        # Transcribe the last chunk
        translate_transcribe(chunk_file, recognizer, num_chunks, input_language)
        
    # Delete the chunks
    for i in range(num_chunks + 1):
        chunk_file = f"{output_folder}/chunk_{i + 1}.wav"
        if os.path.exists(chunk_file):
            os.remove(chunk_file)
            print(f"Deleted chunk {i + 1}")

def translate_transcribe(input_audio, input_recognizer, i, input_language):
    file_location = output_folder + '/new_file.txt'
    with sr.AudioFile(input_audio) as source:
        audio_data = input_recognizer.record(source)
        try:
            transcription = input_recognizer.recognize_google(audio_data, language = input_language, show_all = False)
            translated = GoogleTranslator(source='auto', target='english').translate(text=transcription)
            print('Minute', i, '\n', transcription, '\n', translated)
            text_value = f"\n Minute {i} \n {transcription} \n {translated}"
            with open(file_location, 'a', encoding='utf-8') as file:
                file.write(text_value)
        except sr.UnknownValueError:
            print(f"Chunk {i + 1}: Could not understand audio")
        except sr.RequestError as e:
            print(f"Chunk {i + 1}: Could not request results from Google Speech Recognition service; {e}")
    #   Bad Case 1: UnboundLocalValue: transcription less than 1 second long, but more than 0 so it passes into this function
    #   then Translator cannot catch a value because theres nothing to catch (same applies for BadAudio)

#   input file acts with respect to where THIS FILE is (e.g. samples/song.mp3 means that THIS FILE is in the same location as the sample folder)
#   same syntax applies for output folder too
input_file = "/home/saitama/AmProse/samples_audio/godzila.mp3"
output_folder = "/home/saitama/AmProse/samples_audio"

#   Google Language Codes are in https://readthedocs.org/projects/py-googletrans/downloads/pdf/latest/ under googletrans.LANGUAGES
input_language = "ja"
split_and_transcribe_audio(input_file, output_folder, input_language)