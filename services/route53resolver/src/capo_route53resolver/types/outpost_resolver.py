"""Generated from Smithy shape ``com.amazonaws.route53resolver#OutpostResolver``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.arn
    import capo_route53resolver.types.creator_request_id
    import capo_route53resolver.types.instance_count
    import capo_route53resolver.types.outpost_arn
    import capo_route53resolver.types.outpost_instance_type
    import capo_route53resolver.types.outpost_resolver_name
    import capo_route53resolver.types.outpost_resolver_status
    import capo_route53resolver.types.outpost_resolver_status_message
    import capo_route53resolver.types.resource_id
    import capo_route53resolver.types.rfc3339_time_string


class OutpostResolver(TypedDict, closed=True):
    arn: NotRequired["capo_route53resolver.types.arn.Arn"]
    """<p>The ARN (Amazon Resource Name) for the Resolver on an Outpost.</p>"""
    creation_time: NotRequired[
        "capo_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the Outpost Resolver was created, in Unix time format and Coordinated Universal Time (UTC).</p>"""
    modification_time: NotRequired[
        "capo_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the Outpost Resolver was modified, in Unix time format and Coordinated Universal Time (UTC).</p>"""
    creator_request_id: NotRequired[
        "capo_route53resolver.types.creator_request_id.CreatorRequestId"
    ]
    """<p>A unique string that identifies the request that created the Resolver endpoint. The <code>CreatorRequestId</code> allows failed requests to be retried without the risk of running the operation twice.</p>"""
    id: NotRequired["capo_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of the Resolver on Outpost.</p>"""
    instance_count: NotRequired[
        "capo_route53resolver.types.instance_count.InstanceCount"
    ]
    """<p>Amazon EC2 instance count for the Resolver on the Outpost.</p>"""
    preferred_instance_type: NotRequired[
        "capo_route53resolver.types.outpost_instance_type.OutpostInstanceType"
    ]
    """<p> The Amazon EC2 instance type. </p>"""
    name: NotRequired[
        "capo_route53resolver.types.outpost_resolver_name.OutpostResolverName"
    ]
    """<p>Name of the Resolver.</p>"""
    status: NotRequired[
        "capo_route53resolver.types.outpost_resolver_status.OutpostResolverStatus"
    ]
    """<p>Status of the Resolver.</p>"""
    status_message: NotRequired[
        "capo_route53resolver.types.outpost_resolver_status_message.OutpostResolverStatusMessage"
    ]
    """<p>A detailed description of the Resolver.</p>"""
    outpost_arn: NotRequired["capo_route53resolver.types.outpost_arn.OutpostArn"]
    """<p>The ARN (Amazon Resource Name) for the Outpost.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutpostResolver) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "creation_time" in value:
        out["CreationTime"] = value["creation_time"]
    if "modification_time" in value:
        out["ModificationTime"] = value["modification_time"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "id" in value:
        out["Id"] = value["id"]
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "preferred_instance_type" in value:
        out["PreferredInstanceType"] = value["preferred_instance_type"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_route53resolver.types.outpost_resolver_status

        out["Status"] = (
            capo_route53resolver.types.outpost_resolver_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "outpost_arn" in value:
        out["OutpostArn"] = value["outpost_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OutpostResolver:
    out: OutpostResolver = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("CreationTime") is not None:
        out["creation_time"] = data["CreationTime"]
    if data.get("ModificationTime") is not None:
        out["modification_time"] = data["ModificationTime"]
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("InstanceCount") is not None:
        out["instance_count"] = data["InstanceCount"]
    if data.get("PreferredInstanceType") is not None:
        out["preferred_instance_type"] = data["PreferredInstanceType"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_route53resolver.types.outpost_resolver_status

        out["status"] = (
            capo_route53resolver.types.outpost_resolver_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("OutpostArn") is not None:
        out["outpost_arn"] = data["OutpostArn"]
    return out
