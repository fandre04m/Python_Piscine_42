#!/usr/bin/env python3
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional
# import json
# import csv
# from space_stations import SPACE_STATIONS


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(max_length=200)


def station_monitor() -> None:
    print("Space Station Data Validation")
    # with open("space_stations.json", "r") as f:
    #     data = json.load(f)
    try:
        # for space_station in data:
        #     station = SpaceStation(**space_station)
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.fromisoformat("2077-03-20T10:45:00"),
            notes=None
        )
        print("=" * 42)
        print("Valid station created:")
        print(
            f"ID: {station.station_id}\n"
            f"Name: {station.name}\n"
            f"Crew: {station.crew_size} people\n"
            f"Power: {station.power_level}%\n"
            f"Oxygen: {station.oxygen_level}%\n"
            "Status: "
            f"{'Operational' if station.is_operational else 'Offline'}\n"
            f"Last maintenance: {station.last_maintenance}"
        )
        if station.notes:
            print(f"Notes: {station.notes}\n")
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['loc']} {error['msg']}")
    print("=" * 42)
    print("Expected validation error:")
    try:
        station_2 = SpaceStation(
            station_id="ISS002",
            name="International Space Station",
            crew_size=22,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.fromisoformat("2074-08-22T17:45:00"),
            is_operational=False,
            notes="Needs major engine repairs"
        )
        print(f"ID: {station_2.station_id}")
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['loc']} {error['msg']}")


if __name__ == "__main__":
    station_monitor()
