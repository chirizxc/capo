"""Generated from Smithy shape ``com.amazonaws.launchwizard#ManagementAccountConstraint``."""

from typing_extensions import TypedDict


class ManagementAccountConstraint(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: ManagementAccountConstraint) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ManagementAccountConstraint:
    out: ManagementAccountConstraint = {}  # type: ignore[typeddict-item]
    return out
