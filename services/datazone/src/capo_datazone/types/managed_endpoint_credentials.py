"""Generated from Smithy shape ``com.amazonaws.datazone#ManagedEndpointCredentials``."""

from typing_extensions import NotRequired, TypedDict


class ManagedEndpointCredentials(TypedDict, closed=True):
    id: NotRequired["str"]
    """<p>The identifier of the managed endpoint credentials.</p>"""
    token: NotRequired["str"]
    """<p>The ARN of the managed endpoint credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedEndpointCredentials) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "token" in value:
        out["token"] = value["token"]
    return out


def deserialize_json(data: dict) -> ManagedEndpointCredentials:
    out: ManagedEndpointCredentials = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("token") is not None:
        out["token"] = data["token"]
    return out
