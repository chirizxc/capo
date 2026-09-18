"""Generated from Smithy shape ``com.amazonaws.securityhub#Target``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class _Target_AccountId(TypedDict, closed=True):
    AccountId: "capo_securityhub.types.non_empty_string.NonEmptyString"


class _Target_OrganizationalUnitId(TypedDict, closed=True):
    OrganizationalUnitId: "capo_securityhub.types.non_empty_string.NonEmptyString"


class _Target_RootId(TypedDict, closed=True):
    RootId: "capo_securityhub.types.non_empty_string.NonEmptyString"


Target: TypeAlias = _Target_AccountId | _Target_OrganizationalUnitId | _Target_RootId


# --- restJson1 ser/de ---
def serialize_json(value: Target) -> dict:
    if "AccountId" in value:
        return {"AccountId": value["AccountId"]}
    elif "OrganizationalUnitId" in value:
        return {"OrganizationalUnitId": value["OrganizationalUnitId"]}
    elif "RootId" in value:
        return {"RootId": value["RootId"]}
    else:
        raise SerializationError("Target: no variant present")


def deserialize_json(data: dict) -> Target:
    if data.get("AccountId") is not None:
        return {"AccountId": data["AccountId"]}
    elif data.get("OrganizationalUnitId") is not None:
        return {"OrganizationalUnitId": data["OrganizationalUnitId"]}
    elif data.get("RootId") is not None:
        return {"RootId": data["RootId"]}
    else:
        raise DeserializationError("Target: no recognized variant key")
