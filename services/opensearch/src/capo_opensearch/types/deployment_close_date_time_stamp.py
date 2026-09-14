"""Generated from Smithy shape ``com.amazonaws.opensearch#DeploymentCloseDateTimeStamp``."""

import datetime
from typing import TypeAlias

DeploymentCloseDateTimeStamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentCloseDateTimeStamp) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> DeploymentCloseDateTimeStamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
