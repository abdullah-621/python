class Book:
  def __init__(self,title,author,isbn):
    self.title = title
    self.author = author
    self.isbn = isbn
    self.avaiable = True

  def __str__(self):
    status = "Avaiable" if self.avaiable else "Not Avaiable"
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
 