import os
import json
from datetime import datetime
from flask import Flask, request, abort 
import numpy as np
from DataStore import add_kill, get_series, reset_series
import signal, sys


kills_list = [] 
app = Flask(__name__)

@app.route("/gsi", methods=["POST"])
def gsi():
    payload = request.get_json(force=True, silent=False)
    extract_last_hits(payload)
    kills = payload.get("player", {}).get("kills")
    if kills is not None:
        add_kill(int(kills))
        # DEBUG: show the latest tuple as soon as we add it
        series = get_series()
        print("Added:", series[-1], "| len:", len(series), flush=True)


    return ("", 200)
    

@app.route("/kills", methods=["GET"])
def kills_api():
    # Getter for plotting/inspection
    return jsonify(get_series())

def extract_last_hits(payload: dict):
        print(json.dumps(payload, indent=2))


def dump_and_exit(*_):
    series = get_series()
    for minute, k in series:
        print(f"Minute {minute}: {k} kills")
    sys.stdout.flush()
    sys.exit(0)

if __name__ == "__main__":
    # Ensure Ctrl+C/kill prints the tuples
    signal.signal(signal.SIGINT, dump_and_exit)

    try:
        app.run(port=5000, debug=False, use_reloader=False)  # <- important
    finally:
        dump_and_exit()


