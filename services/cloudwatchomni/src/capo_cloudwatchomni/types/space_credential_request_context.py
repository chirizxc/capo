"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#SpaceCredentialRequestContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.account_id
    import capo_cloudwatchomni.types.domain_id
    import capo_cloudwatchomni.types.space_id


class SpaceCredentialRequestContext(TypedDict, closed=True):
    space_id: NotRequired["capo_cloudwatchomni.types.space_id.SpaceId"]
    """The ID of an existing space to return credentials for."""
    domain_id: NotRequired["capo_cloudwatchomni.types.domain_id.DomainId"]
    """The ID of the domain, when returning credentials for a target account that does not yet have a space."""
    target_account_id: NotRequired["capo_cloudwatchomni.types.account_id.AccountId"]
    """The ID of the target member account. Required when domainId is set."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SpaceCredentialRequestContext) -> dict:
    out: dict = {}
    if "space_id" in value:
        out["spaceId"] = value["space_id"]
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "target_account_id" in value:
        out["targetAccountId"] = value["target_account_id"]
    return out


def deserialize_cbor(data: dict) -> SpaceCredentialRequestContext:
    out: SpaceCredentialRequestContext = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    if data.get("targetAccountId") is not None:
        out["target_account_id"] = data["targetAccountId"]
    return out
