"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PutTestSourcesResponse``."""

from typing_extensions import TypedDict


class PutTestSourcesResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutTestSourcesResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutTestSourcesResponse:
    out: PutTestSourcesResponse = {}  # type: ignore[typeddict-item]
    return out
