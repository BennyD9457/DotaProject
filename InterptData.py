import sqlite3

conn = sqlite3.connect('GameData.db')

c = conn.cursor()

c.execute("""CREATE TABLE GameData(
          
        Seconds INTEGER,
        Kill INTEGER,
        Deaths INTEGER,
        LastHits INTEGER
          )""")

conn.commit()

conn.close()



