"""
this module contains the infrastructure related to the building
"""
from typing import List
from pprint import pprint

MAX_FLOORS: int = 50


class Floor:
    def __init__(self, position: int, name: str) -> "Floor":
        self.position = position
        self.name = f"{name}"

    def __repr__(self) -> str:
        return f"<Floor(position: {self.position}, name: {self.name})>"


class Building:
    NAME = "Nakatomi Plaza"

    def __init__(self, floors: List[Floor]) -> "Building":
        self.floors: list = floors

    @classmethod
    def make_building(cls) -> list:
        "factory method that 'builds' the building"
        floors: list = []
        basement: Floor = Floor(-1, "basement")
        floors.append(basement)

        for i in range(1, MAX_FLOORS+1):
            floor: Floor = Floor(i, f"Floor # {i}")
            floors.append(floor)

        return cls(floors)

    def __repr__(self) -> str:
        return f"<Building(name: {self.NAME}, floors: {self.floors})>"
