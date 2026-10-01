"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PolicyDeletedMetadata``."""

from typing_extensions import NotRequired, TypedDict


class PolicyDeletedMetadata(TypedDict, closed=True):
    affected_service_count: NotRequired["int"]
    """<p>The number of services that were using the policy when it was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyDeletedMetadata) -> dict:
    out: dict = {}
    if "affected_service_count" in value:
        out["affectedServiceCount"] = value["affected_service_count"]
    return out


def deserialize_json(data: dict) -> PolicyDeletedMetadata:
    out: PolicyDeletedMetadata = {}  # type: ignore[typeddict-item]
    if data.get("affectedServiceCount") is not None:
        out["affected_service_count"] = data["affectedServiceCount"]
    return out
