## Import necessary libraries
import pandas as pd


## Book Class
class Book:
    def get_age(book_id, title, author, pages, published_year, genre):
        current_year = 2025
        age = current_year - published_year
        return age

    def is_long(book_id, title, author, pages, published_year, genre):
        if pages > 300:
            return True
        else:
            return False

    def summary(book_id, title, author, pages, published_year, genre):
        return (f"Book ID {book_id}: {title} by {author} has {pages} pages. It was first published in {published_year} "
                f"and belongs to the {genre} genre.")
    
# Confused and checking this push
    
class Library:
    pass


        

