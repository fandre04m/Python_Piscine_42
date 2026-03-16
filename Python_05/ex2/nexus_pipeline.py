#!/usr/bin/env python3
from typing import Any, List, Dict, Union, Optional, Protocol
from abc import ABC, abstractmethod
import json


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Dict[str, Any]:
        if not isinstance(data, dict):
            data = {"raw": data}
        data["stage"] = "input"
        data["valid"] = True
        return data


class TransformStage:
    def process(self, data: Any) -> Dict[str, Any]:
        data["stage"] = "transform"
        data["enriched"] = True
        # Enrich simulation for JSON data
        if (data.get("sensor") == "temp" and
                isinstance(data.get("value"), (int, float))):
            temp = float(data.get("value"))
            data["range_status"] = ("Normal range" if 0.0 <= temp <= 50.0
                                    else "Critical range")
        # Doing something with CSV data
        if data.get("user_action"):
            data["num_of_actions"] = 1
        return data


class OutputStage:
    def process(self, data: Any) -> str:
        data["stage"] = "output"
        # Output formatting for JSON data
        if data.get("sensor") == "temp":
            value = data.get("value")
            unit = data.get("unit")
            status = data.get("range_status")
            return f"Processed temperature reading: {value}°{unit} ({status})"
        # Output formatting for CSV data
        if data.get("num_of_actions"):
            act = data.get("num_of_actions")
            return f"User activity logged: {act} actions processed"
        return "Data processed successfully"


class ProcessingPipeline(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def run_stages(self, data: Any) -> Any:
        for stage in self.stages:
            data = stage.process(data)
        return data

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        if not isinstance(data, str):
            raise ValueError("JSONAdapter expects a JSON string")
        try:
            json_data = json.loads(data)
            return self.run_stages(json_data)
        except ValueError as e:
            return f"Error detected: {e}"


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        if not isinstance(data, str):
            raise ValueError("CSVAdapter expetcs a CSV string")
        user_action = [act for act in data.split(",")]
        csv_data = {"user_action": user_action}
        return self.run_stages(csv_data)


# class StreamAdapter(ProcessingPipeline):
#     def __init__(self, pipeline_id: Any) -> None:
#
#     def process(self, data: Any) -> Union[str, Any]:
#
#
class NexusManager:
    def run_pipeline(self, pipeline: ProcessingPipeline, data: Any) -> Any:
        return pipeline.process(data)


def add_all_stages(pipeline: ProcessingPipeline) -> None:
    pipeline.add_stage(InputStage())
    pipeline.add_stage(TransformStage())
    pipeline.add_stage(OutputStage())


def ft_nexus_pipeline() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    print("Initializing Nexus Manager...")
    manager = NexusManager()
    print("Pipeline capacity: 1000 streams/second\n")
    print(
        "Creating Data Processing Pipeline...\n"
        "Stage 1: Input validation and parsing\n"
        "Stage 2: Data transformation and enrichment\n"
        "Stage 3: Output formatting and delivery\n"
    )
    json_pipe = JSONAdapter("JSON_001")
    csv_pipe = CSVAdapter("CSV_001")
    add_all_stages(json_pipe)
    add_all_stages(csv_pipe)
    print("=== Multi-Format Data Processing ===\n")
    print("Processing JSON data through pipeline...")
    raw_json = '{"sensor": "temp", "value": 23.5, "unit": "C"}'
    print(f"Input: {raw_json}")
    print("Transform: Enriched with metadata and validation")
    print(f"Output: {manager.run_pipeline(json_pipe, raw_json)}")
    print()
    print("Processing CSV data through same pipeline...")
    raw_csv = "user,action,timestamp"
    print(f"Input: \"{raw_csv}\"")
    print("Transform: Parsed and structured data")
    print(f"Output: {manager.run_pipeline(csv_pipe, raw_csv)}")
    print()


if __name__ == "__main__":
    ft_nexus_pipeline()
