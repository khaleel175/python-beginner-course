'''words = {
    "aasman": "sky",
    "kursi" : "chair",
    "haath" : "hand"
}
word = input("enter a word from the dictionary: ")

print(words[word])
'''
words = {
    "aasman": "sky",
    "kursi": "chair",
    "haath": "hand"
}

# Convert to lower case to handle case-insensitive input
word = input("Enter a word (Hindi or English): ").lower()

# Check if input is a Hindi word (key)
if word in words:
    print(f"The English word for '{word}' is '{words[word]}'.")

# Check if input is an English word (value)
elif word in words.values():
    # Find the Hindi word by English value
    for hindi, english in words.items():
        if english == word:
            print(f"The Hindi word for '{word}' is '{hindi}'.")
            break
else:
    print("Word not found in the dictionary.")
