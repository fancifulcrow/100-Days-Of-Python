from gtts import gTTS # Google Text-to-Speech Python library
from PyPDF2 import PdfReader # A PDF reader Python library

# Story from https://www.gutenberg.org/
reader = PdfReader("pdf/Project Gutenberg - Grimm Fairytales.pdf")

# Read every page
text = ""
for page_no in range(len(reader.pages)):
    text += reader.pages[page_no].extract_text()

# Passing the text to gTTS
audio = gTTS(text=text, lang="en", slow="False")

# saving audio in an mp3 file
audio.save("Grimm Fairytales.mp3")
