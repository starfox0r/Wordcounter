import collections
from PyPDF2 import PdfReader

# Open the PDF file
pdf_file = open('test.pdf', 'rb')

# Read the PDF file with PdfReader
pdf = PdfReader(pdf_file)

# Extract text from each page and combine into a single string
text = ''
for page in pdf.pages:
    text += page.extract_text()

# Split the text into individual words and count the occurrences of each word
word_counts = collections.Counter(text.split())

# Get the top 50 words
top_words = word_counts.most_common(50)

# Print the summary
total_words = sum(word_counts.values())
print(f'Total words: {total_words}\n')
print('Top 50 words:')
for word, count in top_words:
    print(f'{word}: {count} ({count/total_words:.2%} of total)')
