"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PolicySharingRevokedMetadata``."""

from typing_extensions import NotRequired, TypedDict


class PolicySharingRevokedMetadata(TypedDict, closed=True):
    affected_service_count: NotRequired["int"]
    """<p>The number of services that were using the policy when sharing was revoked.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicySharingRevokedMetadata) -> dict:
    out: dict = {}
    if "affected_service_count" in value:
        out["affectedServiceCount"] = value["affected_service_count"]
    return out


def deserialize_json(data: dict) -> PolicySharingRevokedMetadata:
    out: PolicySharingRevokedMetadata = {}  # type: ignore[typeddict-item]
    if data.get("affectedServiceCount") is not None:
        out["affected_service_count"] = data["affectedServiceCount"]
    return out
