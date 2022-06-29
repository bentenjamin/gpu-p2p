from typing import TypedDict, List

class gpuListing(TypedDict):
    price: int
    link: str
    name: str

class gpuSeries:
    model: str
    listings: List[gpuListing]

class gpuSeller:
    name: str
    link: str
    gpus: List[gpuSeries]