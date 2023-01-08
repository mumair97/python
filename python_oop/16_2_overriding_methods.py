class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return '"{}" by {}'.format(self.title, self.author)
    
class PaperBook(Book):
    def __init__(self, title, author, numPages):
        Book.__init__(self, title, author)
        self.numpages = numPages

class EBook(Book):
    def __init__(self, title, author, size):
        Book.__init__(self, title, author)
        self.size = size
        
class Library:
    def __init__(self):
        self.books = []
    def addBook(self, book):
        self.books.append(book)
    def getNumBooks(self):
        return len(self.books)
    
myBook =  EBook('The Odyssey', 'Homer', 2)
myPaperBook = PaperBook('The Odyssey', 'Homer', 200)

# print(myBook)
# print(myBook.size)

# print(myPaperBook)
# print(myPaperBook.numpages)

aadl = Library()
aadl.addBook(myBook) # add book 1
aadl.addBook(myPaperBook) # add book 2
print(aadl.getNumBooks()) # 2 (books in the library we have)
