## Import libraries
import pandas as pd
from digital_library import Book, Library

## Read in data (this code reads data directly from GitHub)
url = 'https://raw.githubusercontent.com/Stat386-Fall-2025/Data/refs/heads/master/library_books.csv'
data = pd.read_csv(url)

## Test book class
book = Book('100', 'NewBook', 'NewAuthor', 'Mystery', 270, 2010)
print(book.get_age())
print(book.is_long())
print(book.summary()) 

## Test library class 
library = Library(data)
book = Book('100', 'NewBook', 'NewAuthor', 'Mystery', 270, 2010)
print(library.add_book(book))
print(library.remove_book('101'))
print(library.get_books_by_author('AnotherAuthor'))
print(library.get_genre_count())
print(library.get_book_summary('101'))