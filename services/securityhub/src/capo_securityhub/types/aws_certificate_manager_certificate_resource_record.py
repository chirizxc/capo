"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCertificateManagerCertificateResourceRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsCertificateManagerCertificateResourceRecord(TypedDict, closed=True):
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the resource.</p>"""
    type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of resource.</p>"""
    value: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The value of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCertificateManagerCertificateResourceRecord) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AwsCertificateManagerCertificateResourceRecord:
    out: AwsCertificateManagerCertificateResourceRecord = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
