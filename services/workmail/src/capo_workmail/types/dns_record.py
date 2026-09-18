"""Generated from Smithy shape ``com.amazonaws.workmail#DnsRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.string


class DnsRecord(TypedDict, closed=True):
    type: NotRequired["capo_workmail.types.string.String"]
    """<p>The RFC 1035 record type. Possible values: <code>CNAME</code>, <code>A</code>, <code>MX</code>.</p>"""
    hostname: NotRequired["capo_workmail.types.string.String"]
    """<p>The DNS hostname.- For example, <code>domain.example.com</code>.</p>"""
    value: NotRequired["capo_workmail.types.string.String"]
    """<p>The value returned by the DNS for a query to that hostname and record type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsRecord) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "hostname" in value:
        out["Hostname"] = value["hostname"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DnsRecord:
    out: DnsRecord = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Hostname") is not None:
        out["hostname"] = data["Hostname"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
