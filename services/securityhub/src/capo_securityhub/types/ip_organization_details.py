"""Generated from Smithy shape ``com.amazonaws.securityhub#IpOrganizationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class IpOrganizationDetails(TypedDict, closed=True):
    asn: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The Autonomous System Number (ASN) of the internet provider</p>"""
    asn_org: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the organization that registered the ASN.</p>"""
    isp: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ISP information for the internet provider.</p>"""
    org: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the internet provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IpOrganizationDetails) -> dict:
    out: dict = {}
    if "asn" in value:
        out["Asn"] = value["asn"]
    if "asn_org" in value:
        out["AsnOrg"] = value["asn_org"]
    if "isp" in value:
        out["Isp"] = value["isp"]
    if "org" in value:
        out["Org"] = value["org"]
    return out


def deserialize_json(data: dict) -> IpOrganizationDetails:
    out: IpOrganizationDetails = {}  # type: ignore[typeddict-item]
    if data.get("Asn") is not None:
        out["asn"] = data["Asn"]
    if data.get("AsnOrg") is not None:
        out["asn_org"] = data["AsnOrg"]
    if data.get("Isp") is not None:
        out["isp"] = data["Isp"]
    if data.get("Org") is not None:
        out["org"] = data["Org"]
    return out
