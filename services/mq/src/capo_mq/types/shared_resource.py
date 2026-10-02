"""Generated from Smithy shape ``com.amazonaws.mq#SharedResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__list_of__string
    import capo_mq.types.__string
    import capo_mq.types.shared_resource_error
    import capo_mq.types.shared_resource_status
    import capo_mq.types.shared_resource_type


class SharedResource(TypedDict, closed=True):
    dns_names: NotRequired["capo_mq.types.__list_of__string.__listOf__string"]
    """<p>The DNS names accessible by the broker.</p>"""
    error: NotRequired["capo_mq.types.shared_resource_error.SharedResourceError"]
    """<p>Information on the error encountered by the resource.</p>"""
    resource_arn: NotRequired["capo_mq.types.__string.__string"]
    """<p>The ARN of the shared resource.</p>"""
    resource_share_arns: NotRequired["capo_mq.types.__list_of__string.__listOf__string"]
    """<p>The resource share ARNs to which the resource belongs.</p>"""
    status: NotRequired["capo_mq.types.shared_resource_status.SharedResourceStatus"]
    """<p>The status of the shared resource.</p>"""
    type: NotRequired["capo_mq.types.shared_resource_type.SharedResourceType"]
    """<p>The type of shared resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SharedResource) -> dict:
    out: dict = {}
    if "dns_names" in value:
        import capo_mq.types.__list_of__string

        out["dnsNames"] = capo_mq.types.__list_of__string.serialize_json(
            value["dns_names"]
        )
    if "error" in value:
        import capo_mq.types.shared_resource_error

        out["error"] = capo_mq.types.shared_resource_error.serialize_json(
            value["error"]
        )
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "resource_share_arns" in value:
        import capo_mq.types.__list_of__string

        out["resourceShareArns"] = capo_mq.types.__list_of__string.serialize_json(
            value["resource_share_arns"]
        )
    if "status" in value:
        import capo_mq.types.shared_resource_status

        out["status"] = capo_mq.types.shared_resource_status.serialize_json(
            value["status"]
        )
    if "type" in value:
        import capo_mq.types.shared_resource_type

        out["type"] = capo_mq.types.shared_resource_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> SharedResource:
    out: SharedResource = {}  # type: ignore[typeddict-item]
    if data.get("dnsNames") is not None:
        import capo_mq.types.__list_of__string

        out["dns_names"] = capo_mq.types.__list_of__string.deserialize_json(
            data["dnsNames"]
        )
    if data.get("error") is not None:
        import capo_mq.types.shared_resource_error

        out["error"] = capo_mq.types.shared_resource_error.deserialize_json(
            data["error"]
        )
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("resourceShareArns") is not None:
        import capo_mq.types.__list_of__string

        out["resource_share_arns"] = capo_mq.types.__list_of__string.deserialize_json(
            data["resourceShareArns"]
        )
    if data.get("status") is not None:
        import capo_mq.types.shared_resource_status

        out["status"] = capo_mq.types.shared_resource_status.deserialize_json(
            data["status"]
        )
    if data.get("type") is not None:
        import capo_mq.types.shared_resource_type

        out["type"] = capo_mq.types.shared_resource_type.deserialize_json(data["type"])
    return out
