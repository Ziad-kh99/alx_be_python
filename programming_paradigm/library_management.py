class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False 

    def __str__(self):
        return f'Book: {self.title}\nAuthor: {self.author}\nChecked out: {self._is_checked_out}'
    
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        is_exist = False 
        _book = None
        for book in self._books:
            if book.title == title:
                _book = book
                is_exist = True
                break 
        
        if is_exist:
            _book._is_checked_out = True 
        else:
            print('This book doesn\'t exist')
        
    def return_book(self, title):
        is_exist = False 
        _book = None
        for book in self._books:
            if book.title == title:
                _book = book
                is_exist = True
                break 

        if is_exist:
            _book._is_checked_out = False
        else:
            print('This book doesn\'t exist')

    def return_book(self):
        pass

    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(book)

    


    

