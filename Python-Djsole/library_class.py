class library:
    def __init__(self):
        self.books = []
    def add_books(self,title,author,year):
        self.books.append({"title":title,"author":author,"year":year})
    def list_books(self):
        for book in self.books:
            #  print("Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
             print(f"Title:{book['title']},Author:{book['author']},year : {book['year']}")
obj_library = library()
obj_library.add_books("the holy prophet",'Ahmed ali',2023)


obj_library.list_books()













