"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceOwner``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.resource_owner_account
    import capo_securityhub.types.resource_owner_org


class ResourceOwner(TypedDict, closed=True):
    account: NotRequired[
        "capo_securityhub.types.resource_owner_account.ResourceOwnerAccount"
    ]
    """<p>Information about the account that owns the resource, for example, an Azure Subscription or Amazon Web Services Account.</p>"""
    org: NotRequired["capo_securityhub.types.resource_owner_org.ResourceOwnerOrg"]
    """<p>Information about the organization that owns the resource, for example, an Azure Tenant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceOwner) -> dict:
    out: dict = {}
    if "account" in value:
        import capo_securityhub.types.resource_owner_account

        out["Account"] = capo_securityhub.types.resource_owner_account.serialize_json(
            value["account"]
        )
    if "org" in value:
        import capo_securityhub.types.resource_owner_org

        out["Org"] = capo_securityhub.types.resource_owner_org.serialize_json(
            value["org"]
        )
    return out


def deserialize_json(data: dict) -> ResourceOwner:
    out: ResourceOwner = {}  # type: ignore[typeddict-item]
    if data.get("Account") is not None:
        import capo_securityhub.types.resource_owner_account

        out["account"] = capo_securityhub.types.resource_owner_account.deserialize_json(
            data["Account"]
        )
    if data.get("Org") is not None:
        import capo_securityhub.types.resource_owner_org

        out["org"] = capo_securityhub.types.resource_owner_org.deserialize_json(
            data["Org"]
        )
    return out
