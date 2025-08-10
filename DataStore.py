from dataclasses import dataclass, asdict
from threading import Lock
from typing import List, Dict, Any, Optional
_seconds_idx = -60
@dataclass (frozen=True)
class DataPoint:
    _idx: int
    kills: int
    deaths: int
    last_hits: int


class Series:
    def __init__(self, start_index: int = -60):
        self._lock = Lock()
        self._series: List[DataPoint] = []
        self._idx = start_index
    
    def add(self, kills:int, deaths:int, last_hits:int) -> None:
        with self._lock:
            self._idx += 1
            self._series.append(DataPoint(self._idx, kills, deaths,last_hits))
    
    def get(self) -> List[DataPoint]:
        with self._lock:
            return list(self._series)

            

    def reset(self, start_index: int = -1) -> None:
        with self._lock:
            self._series.clear()
            self._idx = start_index