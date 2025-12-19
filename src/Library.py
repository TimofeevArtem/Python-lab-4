import random
class Item:
    def __init__(self, id, title, year):
        self.title = title

        self.year = year
        self.id = id

        self.in_library = True

    def take_item(self):
        try:
            if self.in_library:

                self.in_library = False
                print(f"{self.title} был(а) взят(а) из библиотеки")


                return 0
            else:
                print(f"{self.title} не оказалось в этой библиотеке")



                return 1
        except Exception as e:
            print(f"Ошибка в __init__: {e}")
            return -1

    def return_item(self):
        try:
            if self.in_library:
                print(f"{self.title} уже в библиотеке")

                return 0
            else:
                print(f"{self.title} был(а) возвращен(а) в библиотеку")

                self.in_library = True
                return 1
            
        except Exception as e:
            print(f"Ошибка в return_item: {e}")
            return -1

class Book(Item):
    def __init__(self, title, author, year, genre, isbn):
        try:
            super().__init__(isbn, title, year)
            self.author = author


            self.genre = genre
            self.isbn = isbn

        except Exception as e:
            print(f"Ошибка в __init__: {e}")

    def __repr__(self):
        return f"Book: {self.title}, {self.author}, {self.year}, {self.genre}, {self.isbn}"

class Magazine(Item):
    def __init__(self, title, year, theme, isbn):
        try:
            super().__init__(isbn, title, year)

            self.theme = theme
            self.isbn = isbn
        except Exception as e:
            print(f"Ошибка в __init__: {e}")
        
    def __repr__(self):
        return f"Magazine: {self.title}, {self.year}, {self.theme}, {self.isbn}"




class BookCollection:
    def __init__(self):
        self.items = []
    
    def __getitem__(self, key):
        try:
            if isinstance(key, slice):

                return self.items[key.start:key.stop:key.step]
            else:

                return self.items[key]
        except Exception as e:
            print(f"Ошибка в __getitim__: {e}")
    
    def __iter__(self):
        return iter(self.items)
    
    def __len__(self):
        return len(self.items)
    

    def add_item(self, item):
        try:
            self.items.append(item)
            print(f"{item.title} добавлен(а) в коллекцию")
            return 0
        except Exception as e:
            print(f"Ошибка в add_item: {e}")
            return -1
    

    def remove_item(self, item):
        try:
            if item in self.items:
                self.items.remove(item)

                print(f"{item.title} удален(а) из коллекции")
                return 0
            
            else:
                print(f"{item.title} не найден(а) в коллекции")
                return 1
            

        except Exception as e:
            print(f"Ошибка в remove_item: {e}")
            return -1

class IndexDict:
    def __init__(self):
        self.isbn_dict = {}
        self.author_dict = {}
        self.year_dict = {}
    


    def __getitem__(self, key):
        try:
            if key in self.isbn_dict:
                return [self.isbn_dict[key]]
            
            elif key in self.author_dict:
                return self.author_dict[key]
            

            elif key in self.year_dict:
                return self.year_dict[key]
            else:

                return []
            

        except Exception as e:
            print(f"Ошибка в __getitem__: {e}")
            return []
    
    def __len__(self):
        return len(self.isbn_dict)
    

    def update_index(self, item):
        try:
                
            if isinstance(item, Book):
                self.isbn_dict[item.isbn] = item
                


                if item.author not in self.author_dict:

                    self.author_dict[item.author] = []
                self.author_dict[item.author].append(item)


                
                if item.year not in self.year_dict:
                    self.year_dict[item.year] = []




                self.year_dict[item.year].append(item)

                print(f"Индексы обновлены для книги: {item.title}")



            elif isinstance(item, Magazine):
                self.isbn_dict[item.isbn] = item
                if item.year not in self.year_dict:
                    self.year_dict[item.year] = []
                self.year_dict[item.year].append(item)
                print(f"Индексы обновлены для журнала: {item.title}")

            return 0
        except Exception as e:
            print(f"Ошибка в update_index: {e}")
            return -1



    def remove_index(self, item):
        try:     
            if item.isbn in self.isbn_dict:
                del self.isbn_dict[item.isbn]
            
            if isinstance(item, Book) and item.author in self.author_dict:
                if item in self.author_dict[item.author]:
                    self.author_dict[item.author].remove(item)


                    if not self.author_dict[item.author]:
                        del self.author_dict[item.author]
            

            
            if item.year in self.year_dict:
                if item in self.year_dict[item.year]:
                    self.year_dict[item.year].remove(item)
                    if not self.year_dict[item.year]:
                        del self.year_dict[item.year]
            print(f"{item.title} удален(а) из индексов")


            return 0
    
        except Exception as e:
            print(f"Ошибка в remove_index: {e}")
            return -1

class Library:
    def __init__(self):
        self.books = BookCollection()
        self.index = IndexDict()
    
    def add_book(self, book):
        try:
            res = self.books.add_item(book)
            if res == 0:
                self.index.update_index(book)
            return res
        

        except Exception as e:
            print(f"Ошибка в add_book: {e}")
            return -1
    
    def remove_book(self, book):
        try:    
            if book in self.books:
                self.index.remove_index(book)
                return self.books.remove_item(book)
            else:
                print(f"{book.title} не найден(а) в библиотеке")

                return 1
            


        except Exception as e:
            print(f"Ошибка в remove_book: {e}")

            return -1
    
    def search_author(self, author):
        try:
            return self.index[author]
        except Exception as e:
            print(f"Ошибка в search_author: {e}")

            return []
    
    def search_year(self, year):
        try:
            return self.index[year]
        except Exception as e:
            print(f"Ошибка в search_year: {e}")
            return []
    
    def search_isbn(self, isbn):
        try:
            res = self.index[isbn]
            if res:
                return res[0]
            else:
                return None
        except Exception as e:

            print(f"Ошибка в search_isbn: {e}")
            return None
        
def run_simulation_library(steps: int = 20, seed: int | None = None) -> None:
    if seed is not None:
        random.seed(seed)
    
    library = Library()
    event_types = ["add", "remove", "search_author", "take", "return"]
    authors = []
    
    for i in range(steps):
        event = random.choice(event_types)
        if event == "add":
            author = f"Author{random.randint(1, 100)}"
            title = f"Book{random.randint(1, 100)}"
            year = random.randint(2000, 2024)
            genre = f"Genre{random.randint(1, 10)}"
            isbn = f"{random.randint(100, 999)}"
            book = Book(title, author, year, genre, isbn)
            library.add_book(book)
            authors.append(author)
            print(f"Шаг {i+1}: Добавлена книга {title}")
            


        elif event == "remove" and len(library.books) > 0:
            books_list = list(library.books)
            if books_list:
                book = random.choice(books_list)
                library.remove_book(book)


                print(f"Шаг {i+1}: Удалена книга {book.title}")
                
        elif event == "search_author":
            if authors:
                author = random.choice(authors)

                res = library.search_author(author)
                print(f"Шаг {i+1}: Поиск автора {author} - найдено {len(res)} книг")
                

        elif event == "take" and len(library.books) > 0:
            books_list = list(library.books)
            if books_list:
                book = random.choice(books_list)
                book.take_item()
                print(f"Шаг {i+1}: Взята книга {book.title}")
        elif event == "return":
            taken_books = [x for x in library.books if not x.in_library]

            if taken_books:
                book = random.choice(taken_books)


                book.return_item()
                print(f"Шаг {i+1}: Возвращена книга {book.title}")