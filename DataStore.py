from threading import Lock
from typing import List, Tuple



KillList = []

__all__ = []

_seconds_idx = -60
_lock = Lock()
_series: List[Tuple[int, int]] = []



def add_kill(kills:int) -> None:
    global _seconds_idx
    with _lock:
        _seconds_idx +=1
        _series.append((_seconds_idx, int(kills)))

def get_series():
    with _lock:
        return list(_series)

def reset_series()->None:
    global _seconds_idx
    with _lock:
        _series.clear()
        _seconds_idx = 0
