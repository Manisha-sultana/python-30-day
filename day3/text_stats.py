text = input("Enter a sentence: ")

clean_text = text.strip()
words = clean_text.split()

print("Original text:", text)
print("Total characters:", len(clean_text))
print("Total words:", len(words))
print("Uppercase:", clean_text.upper())
print("Lowercase:", clean_text.lower())i 