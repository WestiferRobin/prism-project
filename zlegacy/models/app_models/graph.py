from typing import List, Optional, Dict

from pydantic import BaseModel


class GraphAxis(BaseModel):
    symbol: str
    label: str
    data: List[float]


class Graph(BaseModel):
    title: str
    axes: Dict[str, GraphAxis]
    series_label: Optional[str] = None

