class Book:
  def __init__(self,title,author,isbn):
    self.title = title
    self.author = author
    self.isbn = isbn
    self.available  = True

  def __str__(self):
    status = "available " if self.available  else "Not available "
    return f"{self.title} by {self.author} [ISBN:{self.isbn}] - [{status}]"

class Member:
  def __init__(self,name,member_id):
    self.name = name
    self.member_id = member_id
    self.borrowed_books = []

  def __str__(self):
    return f"{self.name} (ID: {self.member_id})"


class Library:
  def __init__(self):
    self.books = []
    self.members = []

  def add_book(self,book):
    self.books.append(book)
    print(f"Book added: {book.title}")

  def register_member(self,member):
    self.members.append(member)
    print(f"Member registered: {member.name}")
 
  def lend_book(self,isbn, member_id):
    book = next((b for b in self.books if b.isbn == isbn and b.available ),None)
    member = next((m for m in self.members if m.member_id == member_id),None)

    if book and member:
      book.available = False
      member.borrowed_books.append(book)
      print(f"{book.title} has been lent to {member.name}")
    else:
      if(not book):
        print("Books not found.")
      elif(not member):
        print("Member not found")
      else:
        print("Member not found and books not available")
    
  def return_book(self,isbn,member_id):
    member = next((m for m in self.members if m.member_id == member_id),None)

    if member:
      book = next((b for b in member.borrowed_books if b.isbn == isbn),None)

      book.available = True
      member.borrowed_books.remove(book)
      print(f"{book.title} has been returned by {member.name}.")
      return
    print("Book not found in member's borrowed list.")

  def show_book(self):
    print("\nAll Books in Library:")
    for book in range(len(self.books)):
      print(f"{book + 1}. {self.books[book]}")
    
  def show_members(self):
        print("\nAll Members:")
        for member in self.members:
            print(member)
            if member.borrowed_books:
                print("  Borrowed books:")
                for book in member.borrowed_books:
                    print(f"    - {book.title}")
            else:
                print("  No borrowed books.")



library = Library()

library.add_book(Book("1984", "George Orwell", "9780451524935"))
library.add_book(Book("The Alchemist", "Paulo Coelho", "9780061122415"))
library.add_book(Book("Sapiens", "Yuval Noah Harari", "9780062316097"))

library.register_member(Member("Masum","M001"))
library.register_member(Member("Amina","M002"))

library.show_book()
library.show_members()
library.lend_book("9780061122415","M001")
library.show_members()
library.return_book("9780061122415","M001")
library.show_members()