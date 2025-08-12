import os
import json
from datetime import datetime
from flask import Flask, request, abort 
import numpy as np
import signal, sys
from DataStore import Series
import sqlite3
import sys 
from sqliteCode import init_db, add_point, start_game

app = Flask(__name__)

series = Series()
@app.route("/gsi", methods=["POST"])
def gsi():
    payload = request.get_json(force=True, silent=False)
    extract_GameData(payload)
    
    kills = payload.get("player", {}).get("kills")
    deaths = payload.get("player", {}).get("deaths")
    last_hits = payload.get("player", {}).get("last_hits")
    
    if kills is not None:
        # add_kill(int(kills))
        series.add(kills,deaths,last_hits) 
       
    return ("", 200)


def extract_GameData(payload: dict):
        print(json.dumps(payload, indent=2))


def dump_and_exit(*_):
    conn = sqlite3.connect("GameData.db")
    game_id = 1

    # Insert all datapoints
    for dp in series.get():
        conn.execute("""
            INSERT INTO GameData (game_id, Seconds, Kill, Deaths, LastHits)
            VALUES (?, ?, ?, ?, ?)
        """, (game_id, dp._idx, dp.kills, dp.deaths, dp.last_hits))

    # Commit so we can see the new rows in the select
    conn.commit()

    # Print all rows in the DB
    print("\n--- Database Contents ---")
    for row in conn.execute("SELECT * FROM GameData"):
        print(row)

    conn.close()
    sys.stdout.flush()
    sys.exit(0)


    for dp in series.get():
      conn = sqlite3.connect("GameData.db")
    
      
            

    sys.stdout.flush()
    sys.exit(0)

if __name__ == "__main__":
    # Ensure Ctrl+C/kill prints the tuples
    signal.signal(signal.SIGINT, dump_and_exit)

    app.run(port=5000, debug=False, use_reloader=False) 
   


