## Import libraries
import pandas as pd
from digital_library import Book, Library

## Read in data (this code reads data directly from GitHub)
url = 'https://raw.githubusercontent.com/Stat386-Fall-2025/Data/refs/heads/master/library_books.csv'
data = pd.read_csv(url)