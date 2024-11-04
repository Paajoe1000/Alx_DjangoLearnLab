# Import the Book model
>>>from bookshelf.models import Book

# Create a Book instance with the title "1984"' author "George Orwell". and publication year 1949
>>>Book.objects.create(title='1984', author='George Orwell', publication_year=1946)

# Expected Output: 
  Title: 1984, Author: George Orwell, Year: 1946

  # Retrieving an displaying the attributes of the book created
>>> Book.objects.get().title
# Expected Output:'1984'

>>> Book.objects.get().author
# Expected Output: 'George Orwell'

>>> Book.objects.get().publication_year
# Expected Output: 1946

# Update the title "1984" to "Nineteen Eighty-Four"
>>> Book.objects.filter(title='1984').update(title='Nineteen Eighty-Four')
# Expected output: 1

# Confirm update by retrieving the title
>>> Book.objects.get().title
# Expected output: 'Nineteen Eoghty-Four'

# Delete the book with the udated title
>>> Book.objects.filter(title='Nineteen Eighty-Four').delete()
# Expected output: (1, {'bookshelf.Book': 1})

# Confirming deletion by retrieving all book objects
>>> Book.objects.all()
# Expected Output: <QuerySet []>