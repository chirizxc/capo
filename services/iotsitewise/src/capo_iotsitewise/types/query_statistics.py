"""Generated from Smithy shape ``com.amazonaws.iotsitewise#QueryStatistics``."""

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError


class QueryStatistics(TypedDict, closed=True):
    row_count: "int"
    """<p>The total number of rows returned by the query.</p>"""
    bytes_scanned: "int"
    """<p>The total number of bytes scanned during query execution.</p>"""
    execution_time_in_millis: "int"
    """<p>The total query execution time, in milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryStatistics) -> dict:
    out: dict = {}
    out["rowCount"] = value["row_count"]
    out["bytesScanned"] = value["bytes_scanned"]
    out["executionTimeInMillis"] = value["execution_time_in_millis"]
    return out


def deserialize_json(data: dict) -> QueryStatistics:
    out: QueryStatistics = {}  # type: ignore[typeddict-item]
    if data.get("rowCount") is not None:
        out["row_count"] = data["rowCount"]
    else:
        raise DeserializationError("QueryStatistics.row_count required")
    if data.get("bytesScanned") is not None:
        out["bytes_scanned"] = data["bytesScanned"]
    else:
        raise DeserializationError("QueryStatistics.bytes_scanned required")
    if data.get("executionTimeInMillis") is not None:
        out["execution_time_in_millis"] = data["executionTimeInMillis"]
    else:
        raise DeserializationError("QueryStatistics.execution_time_in_millis required")
    return out
