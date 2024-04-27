# TextToSpeech
additionally POS tagging and NER added to the project using spacy and textblob libs

This project combines text-to-speech (TTS) technology with Natural Language Processing (NLP) techniques to read text from various sources, including user input and PDF files. It leverages sentiment analysis, Part-of-Speech (POS) tagging, and Named Entity Recognition (NER) to provide a deeper understanding of the text content.

#Introduction
Text-to-speech (TTS) technology allows computers to convert text into spoken words. When combined with Natural Language Processing (NLP), it can offer enhanced capabilities such as sentiment analysis, POS tagging, and NER. This project aims to provide a comprehensive text-to-speech solution with NLP features.

#Features
Text Reading: Read text aloud from user input or PDF files.
Sentiment Analysis: Analyze the sentiment of the text (positive, negative, or neutral) using TextBlob.
Speech Speed Adjustment: Adjust the speech speed based on the detected sentiment.
POS Tagging: Perform Part-of-Speech (POS) tagging using the spaCy library to categorize words in the text.
Named Entity Recognition (NER): Identify named entities such as persons, organizations, and locations in the text using spaCy.


#Dependencies
PyPDF2
pyttsx3
textblob
spaCy
en_core_web_sm (spaCy English language model)
