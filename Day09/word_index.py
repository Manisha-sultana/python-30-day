text = [
    "Python is easy",
    "I am learning Python",
    "Python is powerful"
]

word_lines = {}

for line_number, line in enumerate(text, start=1):
    for word in line.split():
        if word not in word_lines:
            word_lines[word] = []

        word_lines[word].append(line_number)

print(word_lines)