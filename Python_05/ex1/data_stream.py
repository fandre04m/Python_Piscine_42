#!/usr/bin/env python3
from typing import Any, List, Dict, Optional, Union
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.stats = {
            "stream_id": stream_id,
            "stream_type": stream_type,
            "items_processed": 0,
            "main_value": 0
        }

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [
            item for item in data_batch
            if isinstance(item, str) and criteria in item
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return self.stats


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        if not isinstance(data_batch, list):
            raise ValueError("Data batch is not a list!")
        temps = [
            float(item.split(":")[1])
            for item in data_batch
            if isinstance(item, str) and item.startswith("temp:")
        ]
        avg_temp = sum(temps) / len(temps) if temps else 0
        self.stats["items_processed"] = len(data_batch)
        self.stats["main_value"] = avg_temp
        return (
            f"Sensor analysis: {len(data_batch)} readings processed, "
            f"avg temp: {avg_temp}°C"
        )
#
#
# class TransactionStream(DataStream):
#     def process_batch(self, data_batch: List[Any]) -> str:
#         pass
#
#     def filter_data(
#         self,
#         data_batch: List[Any],
#         criteria: Optional[str] = None
#     ) -> List[Any]:
#         pass
#
#     def get_stats(self) -> Dict[str, Union[str, int, float]]:
#         pass
#
#
# class EventStream(DataStream):
#     def process_batch(self, data_batch: List[Any]) -> str:
#         pass
#
#     def filter_data(
#         self,
#         data_batch: List[Any],
#         criteria: Optional[str] = None
#     ) -> List[Any]:
#         pass
#
#     def get_stats(self) -> Dict[str, Union[str, int, float]]:
#         pass


def ft_data_stream() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("\nInitializing Sensor Stream...")
    sensor_stream = SensorStream("SENSOR_001")
    print(
        f"Stream ID: {sensor_stream.stream_id}, "
        f"Type: {sensor_stream.stream_type}"
    )
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    result = sensor_stream.process_batch(sensor_batch)
    print(f"Processing sensor batch: {sensor_batch}")
    print(result)


if __name__ == "__main__":
    ft_data_stream()
