import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('movie_ratings.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS ratings
             (user TEXT, movie1 INTEGER, movie2 INTEGER, movie3 INTEGER, movie4 INTEGER, movie5 INTEGER)''')

# Insert sample data
c.execute("INSERT INTO ratings VALUES ('A', 5, 3, 4, 2, 1)")
c.execute("INSERT INTO ratings VALUES ('B', 4, 5, 1, 2, 3)")
c.execute("INSERT INTO ratings VALUES ('C', 1, 2, 5, 4, 2)")
c.execute("INSERT INTO ratings VALUES ('D', 4, 3, 3, 1, 5)")
c.execute("INSERT INTO ratings VALUES ('E', 2, 3, 4, 5, 4)")

# Save (commit) the changes and close the connection
conn.commit()
conn.close()
