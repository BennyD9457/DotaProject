import os
import json
from datetime import datetime
from flask import Flask, request, abort 
import numpy as np
import signal, sys
from DataStore import Series


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

    for dp in series.get():
        print((dp._idx,dp.kills, dp.deaths, dp.last_hits))
    sys.stdout.flush()
    sys.exit(0)

if __name__ == "__main__":
    # Ensure Ctrl+C/kill prints the tuples
    signal.signal(signal.SIGINT, dump_and_exit)

    app.run(port=5000, debug=False, use_reloader=False) 
   


