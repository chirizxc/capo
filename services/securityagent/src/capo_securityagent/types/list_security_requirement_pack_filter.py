"""Generated from Smithy shape ``com.amazonaws.securityagent#ListSecurityRequirementPackFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.management_type
    import capo_securityagent.types.security_requirement_pack_status


class ListSecurityRequirementPackFilter(TypedDict, closed=True):
    management_type: NotRequired[
        "capo_securityagent.types.management_type.ManagementType"
    ]
    """<p>Filter packs by management type. Valid values are AWS_MANAGED and CUSTOMER_MANAGED.</p>"""
    status: NotRequired[
        "capo_securityagent.types.security_requirement_pack_status.SecurityRequirementPackStatus"
    ]
    """<p>Filter packs by status. Valid values are ENABLED and DISABLED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityRequirementPackFilter) -> dict:
    out: dict = {}
    if "management_type" in value:
        import capo_securityagent.types.management_type

        out["managementType"] = capo_securityagent.types.management_type.serialize_json(
            value["management_type"]
        )
    if "status" in value:
        import capo_securityagent.types.security_requirement_pack_status

        out["status"] = (
            capo_securityagent.types.security_requirement_pack_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSecurityRequirementPackFilter:
    out: ListSecurityRequirementPackFilter = {}  # type: ignore[typeddict-item]
    if data.get("managementType") is not None:
        import capo_securityagent.types.management_type

        out["management_type"] = (
            capo_securityagent.types.management_type.deserialize_json(
                data["managementType"]
            )
        )
    if data.get("status") is not None:
        import capo_securityagent.types.security_requirement_pack_status

        out["status"] = (
            capo_securityagent.types.security_requirement_pack_status.deserialize_json(
                data["status"]
            )
        )
    return out
