"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#DeleteResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.policy_revision_id


class DeleteResourcePolicyResponse(TypedDict, closed=True):
    revision_id: NotRequired[
        "capo_eventbridgev2.types.policy_revision_id.PolicyRevisionId"
    ]
    """Revision ID of the policy that was deleted. Absent when no policy was deleted."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteResourcePolicyResponse) -> dict:
    out: dict = {}
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    return out


def deserialize_cbor(data: dict) -> DeleteResourcePolicyResponse:
    out: DeleteResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    return out
