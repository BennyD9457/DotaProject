import sqlite3


def init_db():
    with sqlite3.connect('GameData.db') as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            started_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            note TEXT
        );
        """)
        conn.execute("""
        CREATE TABLE IF NOT EXISTS GameData (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            game_id INTEGER NOT NULL,
            Seconds INTEGER NOT NULL,
            Kill INTEGER NOT NULL,
            Deaths INTEGER NOT NULL,
            LastHits INTEGER NOT NULL,
            FOREIGN KEY (game_id) REFERENCES games(id)
        );
        """)



def start_game(note=None):
    with sqlite3.connect('GameData.db') as conn:
        cur = conn.execute("INSERT INTO games(note) VALUES (?)", (note,))
        return cur.lastrowid  # Returns the new game ID

def add_point(game_id, seconds, kills, deaths, last_hits):
    with sqlite3.connect('GameData.db') as conn:
        conn.execute(
            "INSERT INTO GameData (game_id, Seconds, Kill, Deaths, LastHits) VALUES (?, ?, ?, ?, ?)",
            (game_id, seconds, kills, deaths, last_hits)
        )

def get_points(game_id):
    with sqlite3.connect('GameData.db') as conn:
        cur = conn.execute(
            "SELECT Seconds, Kill, Deaths, LastHits FROM GameData WHERE game_id=? ORDER BY Seconds",
            (game_id,)
        )
        return cur.fetchall()

      
   

# for dp in series.get():
        
#         conn = sqlite3.connect('GameData.db')
#         c = conn.cursor()
        
#         c.execute(
#             "INSERT INTO GameData (Seconds, Kill, Deaths, LastHits) Values (?,?,?,?) ",
        
#             (dp._idx,dp.kills,dp.deaths,dp.last_hits)
#         )
#         c.execute("SELECT Seconds, Kill, Deaths, LastHits FROM GameData ORDER BY Seconds")
#         rows = c.fetchall()
#         print(rows)

#         print(c.fetchall())
#         conn.commit()
#         conn.close()
        
#         print((dp._idx,dp.kills, dp.deaths, dp.last_hits))