pages = 100
lines = 50
chars = 25
bytes_s = 4

book_size = pages * lines * chars * bytes_s
open_size = 1.44 * 1024 * 1024
num_books = int(open_size // book_size)

print("Количество книг, помещающихся на дискету:", num_books)