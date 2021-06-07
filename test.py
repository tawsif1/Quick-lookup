import sys
from collections import deque
#creating a hard coded database
class Book:
  def __init__(self,title, author, language,key):
    self.title = title
    self.author = author
    self.language = language
    self.key = key
      
books =[]

books.append( Book('Akash', 'author1','lang1',1) )
books.append( Book('Deependra', 'author2','lang2',2) )
books.append( Book('Reaper', 'author3','lang3',3) )
books.append( Book('Reaper2', 'author4','lang4',4) )

 
# a function to fetch the book from data base
memory = deque()
cache = {}
hit = 0
N = 3

def get_book_info(isbn):
    for b in books:
        if isbn == b.key:
            print(f'from db: {b.key}')
            return b

#function using cache to find the books
def quick_lookup(isbn):
    if(isbn in cache):
        print(f'from cache: {cache[isbn].key}')
        memory.remove(isbn)
        memory.append(isbn)
        return cache[isbn]

    else:
        global hit
        hit += 1
        book = get_book_info(isbn)

        if (hit <= N):
            memory.append(isbn)
            cache[isbn] = book
        else:
            cache.pop(memory.popleft(), None)
            cache[isbn] = book 
            memory.append(isbn)

        return book


if __name__=='__main__':
    quick_lookup(1)
    quick_lookup(1)
    quick_lookup(2)
    quick_lookup(3)
    quick_lookup(1)
    quick_lookup(4)
    quick_lookup(1)
  

