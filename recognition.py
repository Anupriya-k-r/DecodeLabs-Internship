from textblob import TextBlob

print(" Basic Text Recognition ")

text = input("Enter a sentence: ")

blob = TextBlob(text)

print("\nAnalysis Result")
print("Words:", blob.words)
print("Sentences:", len(blob.sentences))
print("Corrected Text:", blob.correct())

polarity = blob.sentiment.polarity

if polarity > 0:
    print("Sentiment: Positive 😊")
elif polarity < 0:
    print("Sentiment: Negative 😔")
else:
    print("Sentiment: Neutral 😐")
