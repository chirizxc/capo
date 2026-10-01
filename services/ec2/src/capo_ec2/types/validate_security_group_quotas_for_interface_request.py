"""Generated from Smithy shape ``com.amazonaws.ec2#ValidateSecurityGroupQuotasForInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.security_group_id_list


class ValidateSecurityGroupQuotasForInterfaceRequest(TypedDict, closed=True):
    security_group_ids: NotRequired[
        "capo_ec2.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>The IDs of the security groups to validate for association with a single network interface. You must specify at least one ID, and each ID must be unique. The number of IDs cannot exceed the maximum number of security groups allowed per network interface.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ValidateSecurityGroupQuotasForInterfaceRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "security_group_ids" in value:
        import capo_ec2.types.security_group_id_list

        capo_ec2.types.security_group_id_list.serialize_ec2_query(
            value["security_group_ids"], pairs, f"{key_prefix}SecurityGroupId"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> ValidateSecurityGroupQuotasForInterfaceRequest:
    out: ValidateSecurityGroupQuotasForInterfaceRequest = {}  # type: ignore[typeddict-item]
    child_security_group_ids = el.find("SecurityGroupId")
    if child_security_group_ids is not None:
        import capo_ec2.types.security_group_id_list

        out["security_group_ids"] = (
            capo_ec2.types.security_group_id_list.deserialize_ec2_query(
                child_security_group_ids
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
