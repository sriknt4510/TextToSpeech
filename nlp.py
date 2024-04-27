import PyPDF2
import pyttsx3
import time
from textblob import TextBlob 
import spacy

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Load the English language model for spaCy
nlp = spacy.load("en_core_web_sm")

def analyze_sentiment(text):
   
    blob = TextBlob(text)

    
    polarity = blob.sentiment.polarity

    # Determine the emotion based on polarity
    if polarity < 0:
        emotion = "negative"
    elif polarity > 0:
        emotion = "positive"
    else:
        emotion = "neutral"

    return emotion

def adjust_speed(emotion):
    
    if emotion == "positive":
        engine.setProperty('rate', 140) 
    elif emotion == "negative":
        engine.setProperty('rate', 125) 
    else:
        engine.setProperty('rate', 135)  

def myfun():
  
    with open('Text-To-Speech-main\Once upon a time.pdf', 'rb') as file:
        # Create a PdfReader object
        pdfReader = PyPDF2.PdfReader(file)

        # Initialize start time
        start_time = time.time()

        # Loop through each page and read it
        for page in pdfReader.pages:
            text = page.extract_text()

            # Perform sentiment analysis
            emotion = analyze_sentiment(text)

            # Adjust speech speed based on emotion
            adjust_speed(emotion)

            # Perform POS tagging and NER using spaCy
            doc = nlp(text)
            pos_tags = [(token.text, token.pos_) for token in doc]
            entities = [(ent.text, ent.label_) for ent in doc.ents]

            # Read the text aloud
            engine.say(text)
            engine.runAndWait()

            
            print("POS tags:", pos_tags)
            print("")
            #print("Named entities:", entities)
            print("")

          
            print("Recognized emotion:", emotion)

            
            if time.time() - start_time >= 60:
                print("Timeout reached. Exiting PDF reading...")
                return

def text():
    # Get input text from the user
    read = input("Enter the text : ")

    # Perform sentiment analysis
    emotion = analyze_sentiment(read)

    # Adjust speech speed based on emotion
    adjust_speed(emotion)

    # Perform POS tagging and NER using spaCy
    doc = nlp(read)
    pos_tags = [(token.text, token.pos_) for token in doc]
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Read the text aloud
    engine.say(read)
    engine.runAndWait()

    
    print("POS tags:", pos_tags)
    print("")
    #print("Named entities:", entities)
    print("")

    # Prompt user to recognize the emotion
    print("Recognized emotion:", emotion)

print("Enter Your Choice")
choice = int(input("1: Read From Text\n2: Read From PDF\n"))

if choice == 1:
    text()
else:
    myfun()
