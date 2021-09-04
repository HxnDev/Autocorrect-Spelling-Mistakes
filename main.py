from textblob import TextBlob       # Install using "pip install textblob"

incorrect = input("Enter the incorrect spellings = ")

temp = TextBlob(incorrect)
corrected = str(temp.correct())

if incorrect != corrected:
    print("The correct spellings are = ", corrected)
else:
    print("The spellings are correct.")
