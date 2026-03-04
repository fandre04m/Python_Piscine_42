#!/usr/bin/env python3
from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return f"Processing data: {data}"

    def validate(self, data: Any) -> bool:
        for num in data:
            if type(num) is not int:
                return False
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)
#
#
# class TextProcessor(DataProcessor):
#     def process(self, data: Any) -> str:
#         return "another placeholder"
#
#     def validate(self, data: Any) -> bool:
#         return True
#
#     def format_output(self, result: str) -> str:
#         return "placeholder"
#
#
# class LogProcessor(DataProcessor):
#     def process(self, data: Any) -> str:
#         return "another placeholder"
#
#     def validate(self, data: Any) -> bool:
#         return True
#
#     def format_output(self, result: str) -> str:
#         return "placeholder"


def stream_processor() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    int_list = [1, 2, 3, 4, 5]
    num = NumericProcessor()
    process = num.process(int_list)
    print(process)
    valid = num.validate(int_list)
    print(valid)


if __name__ == "__main__":
    stream_processor()
