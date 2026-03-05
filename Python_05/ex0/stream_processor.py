#!/usr/bin/env python3
from typing import Any
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
        if not self.validate(data):
            raise ValueError("Validation: Data must contain only integers!")
        total_sum = 0
        qty = 0
        avg = None
        for num in data:
            total_sum += num
            qty += 1
            avg = total_sum / qty
        return (
            f"Processed {qty} numeric values, sum={total_sum}, avg={avg:.1f}"
        )

    def validate(self, data: Any) -> bool:
        for num in data:
            if num.__class__ != int:
                return False
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError(
                "Validation: Data is not valid text -> "
                "Example:'Separated by one space each'"
            )
        char_num = 0
        word_num = 0
        for _ in data:
            char_num += 1
        word_list = data.split(" ")
        for _ in word_list:
            word_num += 1
        return f"Processed text: {char_num} characters, {word_num} words"

    def validate(self, data: Any) -> bool:
        if data.__class__ != str:
            return False
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError(
                "Invalid data type or format -> "
                "Must be: 'ERROR: Example text' or 'INFO: Example text'"
            )
        if data.startswith("ERROR:"):
            log_split = data.split(": ")
            return f"[ALERT] {log_split[0]} level detected: {log_split[1]}"
        log_split = data.split(": ")
        return f"[INFO] {log_split[0]} level detected: {log_split[1]}"

    def validate(self, data: Any) -> bool:
        if data.__class__ == str:
            if data.startswith("ERROR:") or data.startswith("INFO:"):
                return True
        return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def polymorphic_demo() -> None:
    print("\n=== Polymorphic Processing Demo ===")
    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    data_types = [
        [1, 2, 3],
        "Hello world!",
        "INFO: System ready"
    ]
    print("\nProcessing multiple data types trough same interface...")
    result_iter = 0
    for data in data_types:
        for processor in processors:
            if processor.validate(data):
                result_iter += 1
                result = processor.process(data)
                print(f"Result {result_iter}: {result}")
                processors.remove(processor)


def stream_processor() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    int_list = [1, 2, 3, 4, 5]
    processor = NumericProcessor()
    print(f"Processing data: {int_list}")
    try:
        result = processor.process(int_list)
        output = processor.format_output(result)
        print("Validation: Numeric data verified")
        print(output)
    except ValueError as e:
        print(e)
    print("\nInitializing Text Processor...")
    string = "Hello Nexus World"
    processor = TextProcessor()
    print(f"Processing data: \"{string}\"")
    try:
        result = processor.process(string)
        output = processor.format_output(result)
        print("Validation: Text data verified")
        print(output)
    except ValueError as e:
        print(e)
    print("\nInitializing Log Processor...")
    log_entry = "ERROR: Connection timeout"
    processor = LogProcessor()
    print(f"Processing data: \"{log_entry}\"")
    try:
        result = processor.process(log_entry)
        output = processor.format_output(result)
        print("Validation: Log entry verified")
        print(output)
    except ValueError as e:
        print(e)
    polymorphic_demo()
    print(
        "\nFoundation systems online. "
        "Nexus ready for advanced streams."
    )


if __name__ == "__main__":
    stream_processor()
