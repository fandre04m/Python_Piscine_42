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
        valid_sensors = ("temp:", "humidity:", "pressure:")
        if not all(
            any(item.startswith(sensor) for sensor in valid_sensors)
            for item in data_batch
        ):
            raise ValueError(
                f"{data_batch} is invalid!\n"
                f"Valid sensors: {valid_sensors}"
            )
        temps = [
            float(item.split(":")[1])
            for item in data_batch
            if item.startswith("temp:")
        ]
        avg_temp = sum(temps) / len(temps) if temps else 0.0
        self.stats["items_processed"] = len(data_batch)
        self.stats["main_value"] = avg_temp
        return (
            f"Sensor analysis: {len(data_batch)} readings, "
            f"avg temp: {avg_temp}°C"
        )


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        valid_trans = ("buy:", "sell:")
        if not all(
            any(item.startswith(trans) for trans in valid_trans)
            for item in data_batch
        ):
            raise ValueError(
                f"{data_batch} is invalid!\n"
                f"Valid transactions: {valid_trans}"
            )
        buy_vals = [
            int(item.split(":")[1])
            for item in data_batch if item.startswith("buy:")
        ]
        sell_vals = [
            int(item.split(":")[1])
            for item in data_batch if item.startswith("sell:")
        ]
        net_val = sum(buy_vals) - sum(sell_vals)
        self.stats["items_processed"] = len(data_batch)
        return (
            f"Transaction analysis: {len(data_batch)} operations, "
            f"net flow: {'+' if net_val > 0 else ''}{net_val} units"
        )


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        valid_events = ("login", "error", "logout")
        if not all(item in valid_events for item in data_batch):
            raise ValueError(
                f"{data_batch} is invalid!\n"
                f"Valid events: {valid_events}"
            )
        error_log = [item for item in data_batch if item == "error"]
        return (
            f"Event analysis: {len(data_batch)} events, "
            f"{len(error_log)} error detected"
        )


class StreamProcessor:
    def __init__(self) -> None:
        self.streams = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, data_batch: List[Any]) -> None:
        processed = False
        for stream in self.streams:
            try:
                result = stream.process_batch(data_batch)
                print(result)
                processed = True
            except ValueError:
                pass
        if not processed:
            print(f"No data stream could process {data_batch}")


def ft_data_stream() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("\nInitializing Sensor Stream...")
    sensor_stream = SensorStream("SENSOR_001")
    print(
        f"Stream ID: {sensor_stream.stream_id}, "
        f"Type: {sensor_stream.stream_type}"
    )
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: [{', '.join(sensor_batch)}]")
    try:
        result = sensor_stream.process_batch(sensor_batch)
        print(result)
    except ValueError as e:
        print(f"ERROR: {e}")
    print("\nInitializing Transaction Stream...")
    trans_stream = TransactionStream("TRANS_001")
    print(
        f"Stream ID: {trans_stream.stream_id}, "
        f"Type: {trans_stream.stream_type}"
    )
    trans_batch = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: [{', '.join(trans_batch)}]")
    try:
        result = trans_stream.process_batch(trans_batch)
        print(result)
    except ValueError as e:
        print(f"ERROR: {e}")
    print("\nInitializing Event Stream...")
    event_stream = EventStream("EVENT_001")
    print(
        f"Stream ID: {event_stream.stream_id}, "
        f"Type: {event_stream.stream_type}"
    )
    event_batch = ["login", "error", "logout"]
    print(f"Processing event batch: [{', '.join(event_batch)}]")
    try:
        result = event_stream.process_batch(event_batch)
        print(result)
    except ValueError as e:
        print(f"ERROR: {e}")
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    processor = StreamProcessor()
    processor.add_stream(sensor_stream)
    processor.add_stream(trans_stream)
    processor.add_stream(event_stream)
    batch_1 = [
        sensor_batch,
        trans_batch,
        event_batch
    ]
    print("\nBatch 1 Results:")
    for batch in batch_1:
        processor.process_all(batch)


if __name__ == "__main__":
    ft_data_stream()
