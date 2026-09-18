"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#WorkloadInsightsTopContributorsValuesList``."""

from typing import TypeAlias

WorkloadInsightsTopContributorsValuesList: TypeAlias = list["float"]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadInsightsTopContributorsValuesList) -> list:
    return [
        (
            "NaN"
            if item != item
            else "Infinity"
            if item == float("inf")
            else "-Infinity"
            if item == float("-inf")
            else item
        )
        for item in value
    ]


def deserialize_json(data: list) -> WorkloadInsightsTopContributorsValuesList:
    return [float(item) for item in data if item is not None]
