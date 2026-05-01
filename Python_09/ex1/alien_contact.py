#!/usr/bin/env python3
from typing import Optional
from typing_extensions import Self
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
# from alien_contacts import ALIEN_CONTACTS


class ContactType(str, Enum):
    rad = "radio"
    vis = "visual"
    phys = "physical"
    tele = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_contact(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "Contact ID must start with 'AC' (Alien Contact)"
            )
        if self.contact_type == ContactType.phys and not self.is_verified:
            raise ValueError(
                "Physical contact reports must be verified"
            )
        if self.contact_type == ContactType.tele and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return self


def report_checker() -> None:
    print("Alien Contact Log Validation")
    print("=" * 42)
    try:
        # for contact in ALIEN_CONTACTS:
        #     report = AlienContact(**contact)
        report = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.fromisoformat("2025-03-20T04:32:54"),
            location="Area 51, Nevada",
            contact_type=ContactType.rad,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Valid contact report:")
        print(
                f"ID: {report.contact_id}\n"
                f"Type: {report.contact_type}\n"
                f"Location: {report.location}\n"
                f"Signal: {report.signal_strength}/10\n"
                f"Duration: {report.duration_minutes} minutes\n"
                f"Witnesses: {report.witness_count}"
        )
        if report.message_received:
            print(f"Message: '{report.message_received}'\n")
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg']}")
    print("=" * 42)
    print("Expected validation error:")
    try:
        bad_rep = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.fromisoformat("2025-03-20T04:32:54"),
            location="Area 51, Nevada",
            contact_type=ContactType.tele,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli"
        )
        print("=" * 42)
        print("Valid contact report:")
        print(
                f"ID: {bad_rep.contact_id}\n"
                f"Type: {bad_rep.contact_type}\n"
                f"Location: {bad_rep.location}\n"
                f"Signal: {bad_rep.signal_strength}/10\n"
                f"Duration: {bad_rep.duration_minutes} minutes\n"
                f"Witnesses: {bad_rep.witness_count}\n"
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'].split(", ")[-1])


if __name__ == "__main__":
    report_checker()
