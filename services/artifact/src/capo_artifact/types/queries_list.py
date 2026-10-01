"""Generated from Smithy shape ``com.amazonaws.artifact#QueriesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_artifact.types.query_summary

QueriesList: TypeAlias = list["capo_artifact.types.query_summary.QuerySummary"]


# --- restJson1 ser/de ---
def serialize_json(value: QueriesList) -> list:
    import capo_artifact.types.query_summary

    out: list = []
    for item in value:
        out.append(capo_artifact.types.query_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueriesList:
    import capo_artifact.types.query_summary

    out: QueriesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_artifact.types.query_summary.deserialize_json(item))
    return out
