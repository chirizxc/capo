"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListTestTemplatesRequest``."""

from typing_extensions import TypedDict


class ListTestTemplatesRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: ListTestTemplatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTestTemplatesRequest:
    out: ListTestTemplatesRequest = {}  # type: ignore[typeddict-item]
    return out
