import db

def add_book(title, author, year, description, user_id):
    sql = """INSERT INTO books (title, author, year, description, user_id)
             VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, author, year, description, user_id])
    return db.last_insert_id()
