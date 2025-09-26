## Import necessary libraries
import pandas as pd


## Book Class
class Book:
    def __init__(self, book_id, title, author, genre, pages, published_year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.published_year = published_year
        self.current_year = 2025

    def get_age(self):
        age = self.current_year - self.published_year
        return age

    def is_long(self):
        if self.pages > 300:
            return True
        else:
            return False

    def summary(self):
        return (f"Book ID {self.book_id}: {self.title} by {self.author} has {self.pages} pages. "
                f"It was first published in {self.published_year} "
                f"and belongs to the {self.genre} genre.")
    
class Library:
    def __init__(self, data: pd.DataFrame):
        self.data = data.copy()
        self.size = len(self.data)
        self.authors = self.data['author'].unique()

    def add_book(self, book):
        if book.book_id in self.data['book_id'].values:
            return f"Error: book_id {book.book_id} is already in the library."
        else:
            new_entry = {
                'book_id': book.book_id,
                'title': book.title,
                'author': book.author,
                'pages': book.pages,
                'published_year': book.published_year,
                'genre': book.genre
            }
            self.data = pd.concat([self.data, pd.DataFrame([new_entry])], ignore_index=True)
            self.size = len(self.data)
            self.authors = self.data['author'].unique()

    def remove_book(self, book_id: str):
        if book_id not in self.data['book_id'].values:
            return f"Error: book_id {book_id} is not in the library."
        else:
            self.data = self.data[self.data['book_id'] != book_id]
            self.size = len(self.data)
            self.authors = self.data['author'].unique()
        
    def get_books_by_author(self, author: str):
        author_books = self.data[self.data['author'] == author]
        if author_books.empty:
            return f"No books found by author {author}."
        else: 
            return author_books

    def get_genre_count(self):
        return self.data['genre'].value_counts()

    def get_book_summary(self, book_id):
        book = self.data[self.data['book_id'] == book_id]
        if book.empty:
            return "No matching book in the library"
        book = book.iloc[0]
        return (f"Book ID {book.book_id}: {book.title} by {book.author} has {book.pages} pages. "
            f"It was first published in {book.published_year} and belongs to the genre {book.genre}.")

    def __str__(self):
        if self.data.empty:
            return "The library is empty."
        oldest_book = self.data.loc[self.data['published_year'].idxmin()]
        return (f"There are {self.size} books in the library by {self.authors} unique authors. "
            f"The oldest book in the library is {oldest_book.title} by {oldest_book.author} published in {oldest_book.published_year}.")

        

