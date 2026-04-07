# Multiline string (paragraph)
paragraph = """  Python is a powerful programming language.
It is widely used for web development, data science, artificial intelligence,
and many more applications. This Python course is beginner friendly.  """

# Remove extra whitespaces from start and end
paragraph = paragraph.strip()

# Length of paragraph
length = len(paragraph)
print("Length of paragraph:", length)

# First and last characters
print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

# First 50 characters (preview)
print("Preview (first 50 chars):", paragraph[:50])

# Replace "Python" with "PYTHON"
replaced_paragraph = paragraph.replace("Python", "PYTHON")
print("\nAfter replacement:\n", replaced_paragraph)

# Convert to lowercase
lower_paragraph = paragraph.lower()
print("\nLowercase version:\n", lower_paragraph)

# Split into words
words = paragraph.split()
print("\nList of words:\n", words)

# Check if "course" exists
if "course" in paragraph:
    print("\nThe word 'course' is found in the paragraph.")
else:
    print("\nThe word 'course' is NOT found.")

# Final message using format()
word_count = len(words)
final_message = "The course description is {} characters long and has {} words.".format(length, word_count)
print("\n" + final_message)