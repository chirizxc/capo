"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#FrameworkSummary``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_marketplace_catalog.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.ami_security_summary
    import capo_marketplace_catalog.types.container_security_summary


class _FrameworkSummary_AMISecuritySummary(TypedDict, closed=True):
    AMISecuritySummary: (
        "capo_marketplace_catalog.types.ami_security_summary.AMISecuritySummary"
    )


class _FrameworkSummary_ContainerSecuritySummary(TypedDict, closed=True):
    ContainerSecuritySummary: "capo_marketplace_catalog.types.container_security_summary.ContainerSecuritySummary"


FrameworkSummary: TypeAlias = (
    _FrameworkSummary_AMISecuritySummary | _FrameworkSummary_ContainerSecuritySummary
)


# --- restJson1 ser/de ---
def serialize_json(value: FrameworkSummary) -> dict:
    if "AMISecuritySummary" in value:
        import capo_marketplace_catalog.types.ami_security_summary

        return {
            "AMISecuritySummary": capo_marketplace_catalog.types.ami_security_summary.serialize_json(
                value["AMISecuritySummary"]
            )
        }
    elif "ContainerSecuritySummary" in value:
        import capo_marketplace_catalog.types.container_security_summary

        return {
            "ContainerSecuritySummary": capo_marketplace_catalog.types.container_security_summary.serialize_json(
                value["ContainerSecuritySummary"]
            )
        }
    else:
        raise SerializationError("FrameworkSummary: no variant present")


def deserialize_json(data: dict) -> FrameworkSummary:
    if data.get("AMISecuritySummary") is not None:
        import capo_marketplace_catalog.types.ami_security_summary

        return {
            "AMISecuritySummary": capo_marketplace_catalog.types.ami_security_summary.deserialize_json(
                data["AMISecuritySummary"]
            )
        }
    elif data.get("ContainerSecuritySummary") is not None:
        import capo_marketplace_catalog.types.container_security_summary

        return {
            "ContainerSecuritySummary": capo_marketplace_catalog.types.container_security_summary.deserialize_json(
                data["ContainerSecuritySummary"]
            )
        }
    else:
        raise DeserializationError("FrameworkSummary: no recognized variant key")
