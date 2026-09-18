"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#Iso8601DateTime``."""

import datetime
from typing import TypeAlias

Iso8601DateTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Iso8601DateTime) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_aws_json_1_1(data: str) -> Iso8601DateTime:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
