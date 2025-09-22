# Lab 4: Object-Oriented Programming and Pandas

When you accept the assignment in GitHub Classroom, a repository named `oop_lab` will be automatically generated for you under the "Stat386-Fall-2025" organization.
* Your personal repository for this homework can be found at `https://github.com/Stat386-fall-2025/oop_lab-your_user_name`.
* Clone the repository locally
   * Open your terminal and navigate to the directory where you want to download the repository.
   * Run `git clone [your repository URL]` to clone the repository onto your local machine.
   * The cloning process will create a new directory named `oop_lab-your_user_name`. Ensure that you perform all your work inside this directory.
   * As you work on the assignment, remember to commit your changes periodically. You can easily do this using Visual Studio Code (VS Code).
   * If you've cloned the repository correctly and are working within the created directory, the remote link to your GitHub repository should already be configured
* Do Not change the names of the files, functions, methods, or Classes.
* Once you have completed the lab, please add an entry to the textbox in the canvas assignment stating that you are finished with the lab.

### Instructions 
#### Objective: 
The goal of this assignment is to merge foundational concepts from object-oriented programming with the utility of the Pandas library. By the end, you should be able to create classes that can effectively interact with and manipulate Pandas data structures.

#### Problem Statement:  
You are a data analyst at a digital library. Your task is to design a system that can process, manipulate, and analyze data regarding different books available in the library.

#### Files and Functions
* For Tasks 1 and 2, write the code for the Classes in the provided `digital_library.py`.  
* For Task 3, use the file `test_library.py` to write code that shows that your classes work as expected. 
   * *Note: Formal unit tests are NOT required.  I'm just expecting you to run python code with your classes and methods to demonstrate that they are working as expected*
* **Do not** change the names of the files, functions, methods, or Classes.
* You are free to include other `.py` or `.ipynb` files with more of your work. However, ensure that `digital_library.py` contains the final code for each Class and `test_library.py` contains the code to test your classes. 

### Data
The data for this lab is `library_books.csv` found in the "Data" folder of the class GitHub [Data Repository](https://github.com/Stat386-Fall-2025/Data/tree/master).  This data is a simplified and cleaned subset from [Zenodo](https://zenodo.org/record/4265096).  It has the following columns:
1. `book_id`: Unique identifier for each book (should be a string)
2. `title`: Title of the book.
3. `author`: Author of the book.
4. `genre`: Genre of the book (e.g., Fiction, Non-Fiction, Mystery, Sci-Fi).
5. `pages`: Number of pages in the book.
6. `published_year`: The year the book was published.

**Note: The data is only necessary for Task 3.  It is not necessarily needed in the writing of the Classes**



---
### Task 1: Create a `Book` class
#### Attributes:
- `book_id` 
- `title`
- `author`
- `genre`
- `pages`
- `published_year`

#### Methods:
- `get_age()`: Should return the age of the book based on the current year.
- `is_long()`: Should return `True` if the book has more than 300 pages; otherwise, `False`.
- `summary()`: Should return a string with the format: "Book ID `book_id`: `title` by `author` has `pages` pages. It was first published in `published_year` and belongs to the `genre` genre."

#### Instantiating the Object:
- When an object of the `Book` class is instantiated, each of the attributes should be specified separately.  For example:
  ```
  book = Book('100', 'NewBook', 'NewAuthor', 'Mystery', 270, 2010)
  ```
- Make sure that the code for your classes, attributes, and functions assume this form for object instantiation

---
### Task 2: Create a `Library` class
#### Attributes:
- `data`: A pandas DataFrame loaded from the provided CSV file.
- `size`: Number of books in the library.
- `authors`: Number of unique authors in the library.

#### Methods:
- `add_book(book)`: Takes an instance of `Book` and adds it to the DataFrame. All `Library` attributes should be updated accordingly.
   * If the book already exists in library the method should return the string "Error: book_id `book_id` is already in the library."
- `remove_book(book_id)`: Takes a `book_id` (of type `str`) and removes the corresponding book from the DataFrame. All `Library` attributes should be updated accordingly.  
   * If the `book_id` is not in the library, the method should return the string: "Error: `book_id` is not in the library."
- `get_books_by_author(author)`: Takes an author's name (of type `str`) and returns a DataFrame containing all books by that author.
   * If `author` is not in the library, the method should return the string: "No books by `author` in library"
- `get_genre_count()`: Should return a series with the count of books in each genre.
- `get_book_summary(book_id)`: Takes a `book_id` (of type `str`) and returns a string with the format:  
   * "Book ID `book_id`: `title` by `author` has `pages` pages. It was first published in `published_year` and belongs to the `genre` genre."  
   * If the `book_id` is not in the library, it should return "No matching book in the library."
- `__str__()`: Should return a string representing the library. When a `Library` object is printed (e.g. `print(my_library)`), the string "There are `size` books in the library by `authors` unique authors. The oldest book in the library is `title` by `author` published in `published_year`." should be output.

#### Instantiating the Object:
- An object of the `Library` class should be instantiated only with a *Pandas* DataFrame.  That is, ensure that you load `library_books.csv` into a Pandas DataFrame *before* passing it to `Library`.  For example:
  ```
  df = pd.read_csv('library_books.csv')
  library = Library(df)
  ```
- Make sure that the code for your classes, attributes, and functions assume this form for object instantiation

#### Additional Notes:
- Please ensure to update the `size` and `authors` attributes of the `Library` class appropriately whenever a book is added or removed.

---
### Task 3:  Test your Classes
In the `test_library.py` file write python code that:
* Creates instances of the `Book` class
* Initializes a `Library` using [`library_books.csv`](https://github.com/Stat386-Fall-2025/Data/tree/master)
* Tests all methods of both classes to ensure they work as expected
  For example, if you are testing the `summary` method for the Book class:
  ```
  book1 = Book('100', 'NewBook', 'NewAuthor', 'Mystery', 270, 2010)
   print(book1.summary()) 
   # Should print:
   # "Book ID 100: NewBook by NewAuthor has 270 pages. It was first published in 2010 and belongs to the Mystery genre."
  ```
* Ensure that your code is well-commented and that both files are free of syntax errors and run without issues
