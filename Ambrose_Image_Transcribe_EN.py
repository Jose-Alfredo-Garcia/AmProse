#   BASED ON THIS FROM https://stackoverflow.com/questions/57866592/how-to-print-tesseract-result-in-chinese-characters
#   Lang Codes and Doc are in this website: https://www.kaggle.com/code/dhorvay/pytesseract-function-parameters under 'lang'
#   lang = 'lat'[Latin], 'chi_sim_vert'[Chinese Simplified Vertical], 'chi_tra_vert'[Chinese Traditional Vertical], 'jpn_vert'[Japanese Vertical]
import pytesseract
from PIL import Image
from googletrans import Translator

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\FrankieG\Documents\LEARNING\Python Projects\Ambrose_Project\Tesseract-OCR\tesseract.exe'
translator = Translator()

# EDIT THIS ACCORDING TO DESIRED LANGUAGE
text = pytesseract.image_to_string(Image.open("samples_image/japan_basic.png"), lang = "jpn")
translated_text = translator.translate(text, dest='en').text
with open('samples_image/output_text.txt', 'w', encoding='utf-8') as file:
    file.write(text)
    file.write(translated_text)