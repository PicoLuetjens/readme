from gtts import gTTS
import sys
from PyPDF2 import PdfReader
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, help="the filepath to the input file(.pdf)", required=True)
parser.add_argument("-l", "--language", type=str, help="the language of the input file options: en-uk/en-us/de/nl/...", required=True)
# parser.add_argument("-s", "--speaker", type=str, help="the gender of the speaker options: male/female", required=True)
parser.add_argument("-o", "--output", type=str, help="the filepath to the output file(.mp3)" ,required=True)
parsed_arguments = parser.parse_args()

reader = PdfReader(parsed_arguments.input)

convert_text = ""

for page in reader.pages:
    page_text = page.extract_text()
    convert_text+=page_text

language = parsed_arguments.language

myObj = gTTS(text=convert_text, lang=language, slow=False)
myObj.save(parsed_arguments.output)
