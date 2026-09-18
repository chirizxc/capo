"""Generated from Smithy shape ``com.amazonaws.controlcatalog#AssociatedDomainSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controlcatalog.types.domain_arn


class AssociatedDomainSummary(TypedDict, closed=True):
    arn: NotRequired["capo_controlcatalog.types.domain_arn.DomainArn"]
    """<p>The Amazon Resource Name (ARN) of the related domain.</p>"""
    name: NotRequired["str"]
    """<p>The name of the related domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedDomainSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AssociatedDomainSummary:
    out: AssociatedDomainSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
