import db

def add_book(title, author, year, description, user_id):
    sql = """INSERT INTO books (title, author, year, description, user_id)
             VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, author, year, description, user_id])
    return db.last_insert_id()

def get_books():
    sql = """SELECT books.id, books.title, books.author,
                    users.id user_id, users.username
             FROM books JOIN users ON books.user_id = users.id
             ORDER BY books.id DESC"""
    return db.query(sql)

def get_book(book_id):
    sql = """SELECT books.id,
                    books.title,
                    books.author,
                    books.year,
                    books.description,
                    users.id user_id,
                    users.username
             FROM books, users
             WHERE books.user_id = users.id AND
                   books.id = ?"""
    result = db.query(sql, [book_id])
    return result[0] if result else None

def update_book(book_id, title, author, year, description):
    sql = """UPDATE books SET title = ?,
                              author = ?,
                              year = ?,
                              description = ?
                          WHERE id = ?"""
    db.execute(sql, [title, author, year, description, book_id])

def remove_book(book_id):
    sql = "DELETE FROM books WHERE id = ?"
    db.execute(sql, [book_id])
