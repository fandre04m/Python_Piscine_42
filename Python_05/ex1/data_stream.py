#!/usr/bin/env python3
from typing import Any, List, Dict, Optional, Union
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.stats = {
            "batch_type": "placeholder",
            "units": "placeholder",
            "items_processed": 0
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
        self.stats["batch_type"] = "Sensor"
        self.stats["units"] = "readings"

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
        return (
            f"Sensor analysis: {len(data_batch)} readings, "
            f"avg temp: {avg_temp}°C"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        if criteria == "critical":
            return [
                item for item in data_batch
                if item.startswith("temp:") and (
                    float(item.split(":")[1]) > 100 or
                    float(item.split(":")[1]) < 0
                )
            ]
        return [item for item in data_batch if item.startswith(criteria)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        super().get_stats()
        return self.stats


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")
        self.stats["batch_type"] = "Transaction"
        self.stats["units"] = "operations"

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

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        if criteria == "large":
            return [
                item for item in data_batch
                if (item.startswith("buy:") or item.startswith("sell:")) and
                int(item.split(":")[1]) > 200
            ]
        return [item for item in data_batch if item.startswith(criteria)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        super().get_stats()
        return self.stats


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")
        self.stats["batch_type"] = "Event"
        self.stats["units"] = "events"

    def process_batch(self, data_batch: List[Any]) -> str:
        valid_events = ("login", "error", "logout")
        if not all(item in valid_events for item in data_batch):
            raise ValueError(
                f"{data_batch} is invalid!\n"
                f"Valid events: {valid_events}"
            )
        error_log = [item for item in data_batch if item == "error"]
        self.stats["items_processed"] = len(data_batch)
        return (
            f"Event analysis: {len(data_batch)} events, "
            f"{len(error_log)} error detected"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        if criteria == "error":
            return [
                item for item in data_batch
                if item == "error"
            ]
        return [item for item in data_batch if item == criteria]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        super().get_stats()
        return self.stats


class StreamProcessor:
    def __init__(self) -> None:
        self.streams = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_and_stats(
        self, data_batch: List[Any]
    ) -> Dict[str, Union[str, int, float]]:
        for stream in self.streams:
            try:
                stream.process_batch(data_batch)
                return stream.get_stats()
            except ValueError:
                pass
        raise ValueError(f"No data stream could process {data_batch}!")

    def filter_all(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        for stream in self.streams:
            try:
                stream.process_batch(data_batch)
                return stream.filter_data(data_batch, criteria)
            except ValueError:
                pass
        raise ValueError(f"The {criteria} was not valid for filtering!")


def poly_processing(processor: StreamProcessor) -> None:
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    batch_1 = [
        ["temp:102.3", "temp:-9.8"],
        ["buy:50", "buy:80", "buy:60", "sell:210"],
        ["login", "error", "logout"]
    ]
    print("\nBatch 1 Results:")
    for batch in batch_1:
        try:
            stats = processor.process_and_stats(batch)
            print(
                f"- {stats['batch_type']} data: {stats['items_processed']} "
                f"{stats['units']} processed"
            )
        except ValueError as e:
            print(e)
    print("\nStream filtering active: High-priority data only")
    filters = ["critical", "large"]
    filter_msg = []
    for batch in batch_1:
        for filt in filters:
            try:
                res = len(processor.filter_all(batch, filt))
                if res and filt == "critical":
                    filter_msg.append(f"{res} {filt} sensor alerts")
                elif res and filt == "large":
                    filter_msg.append(f"{res} {filt} transaction")
            except ValueError as e:
                print(e)
    print(f"Filtered results: {', '.join(filter_msg)}")


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
    processor = StreamProcessor()
    processor.add_stream(sensor_stream)
    processor.add_stream(trans_stream)
    processor.add_stream(event_stream)
    poly_processing(processor)
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    ft_data_stream()
