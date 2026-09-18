"""Generated from Smithy shape ``com.amazonaws.macie2#IpOwner``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string


class IpOwner(TypedDict, closed=True):
    asn: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The autonomous system number (ASN) for the autonomous system that included the IP address.</p>"""
    asn_org: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The organization identifier that's associated with the autonomous system number (ASN) for the autonomous system that included the IP address.</p>"""
    isp: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The name of the internet service provider (ISP) that owned the IP address.</p>"""
    org: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The name of the organization that owned the IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IpOwner) -> dict:
    out: dict = {}
    if "asn" in value:
        out["asn"] = value["asn"]
    if "asn_org" in value:
        out["asnOrg"] = value["asn_org"]
    if "isp" in value:
        out["isp"] = value["isp"]
    if "org" in value:
        out["org"] = value["org"]
    return out


def deserialize_json(data: dict) -> IpOwner:
    out: IpOwner = {}  # type: ignore[typeddict-item]
    if data.get("asn") is not None:
        out["asn"] = data["asn"]
    if data.get("asnOrg") is not None:
        out["asn_org"] = data["asnOrg"]
    if data.get("isp") is not None:
        out["isp"] = data["isp"]
    if data.get("org") is not None:
        out["org"] = data["org"]
    return out
