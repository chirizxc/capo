"""Generated from Smithy shape ``com.amazonaws.odb#OciDnsForwardingConfig``."""

from typing_extensions import NotRequired, TypedDict


class OciDnsForwardingConfig(TypedDict, closed=True):
    domain_name: NotRequired["str"]
    """<p>Domain name to which DNS resolver forwards to.</p>"""
    oci_dns_listener_ip: NotRequired["str"]
    """<p>OCI DNS listener IP for custom DNS setup.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OciDnsForwardingConfig) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "oci_dns_listener_ip" in value:
        out["ociDnsListenerIp"] = value["oci_dns_listener_ip"]
    return out


def deserialize_aws_json_1_0(data: dict) -> OciDnsForwardingConfig:
    out: OciDnsForwardingConfig = {}  # type: ignore[typeddict-item]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    if data.get("ociDnsListenerIp") is not None:
        out["oci_dns_listener_ip"] = data["ociDnsListenerIp"]
    return out
