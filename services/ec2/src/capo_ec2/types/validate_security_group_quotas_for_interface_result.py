"""Generated from Smithy shape ``com.amazonaws.ec2#ValidateSecurityGroupQuotasForInterfaceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean


class ValidateSecurityGroupQuotasForInterfaceResult(TypedDict, closed=True):
    valid: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether the specified security groups can be associated with a single network interface without exceeding the quotas. If associating the security groups would exceed a quota, the operation returns an error.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ValidateSecurityGroupQuotasForInterfaceResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "valid" in value:
        pairs.append((f"{key_prefix}Valid", "true" if value["valid"] else "false"))


def deserialize_ec2_query(el: Element) -> ValidateSecurityGroupQuotasForInterfaceResult:
    out: ValidateSecurityGroupQuotasForInterfaceResult = {}  # type: ignore[typeddict-item]
    child_valid = el.find("valid")
    if child_valid is not None:
        out["valid"] = (child_valid.text or "").lower() == "true"
    return out
