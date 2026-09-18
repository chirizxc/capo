"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallRuleGroupAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.arn
    import capo_route53resolver.types.creator_request_id
    import capo_route53resolver.types.firewall_rule_group_association_status
    import capo_route53resolver.types.mutation_protection_status
    import capo_route53resolver.types.name
    import capo_route53resolver.types.priority
    import capo_route53resolver.types.resource_id
    import capo_route53resolver.types.rfc3339_time_string
    import capo_route53resolver.types.service_principle
    import capo_route53resolver.types.status_message


class FirewallRuleGroupAssociation(TypedDict, closed=True):
    id: NotRequired["capo_route53resolver.types.resource_id.ResourceId"]
    """<p>The identifier for the association.</p>"""
    arn: NotRequired["capo_route53resolver.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the firewall rule group association.</p>"""
    firewall_rule_group_id: NotRequired[
        "capo_route53resolver.types.resource_id.ResourceId"
    ]
    """<p>The unique identifier of the firewall rule group. </p>"""
    vpc_id: NotRequired["capo_route53resolver.types.resource_id.ResourceId"]
    """<p>The unique identifier of the VPC that is associated with the rule group. </p>"""
    name: NotRequired["capo_route53resolver.types.name.Name"]
    """<p>The name of the association.</p>"""
    priority: NotRequired["capo_route53resolver.types.priority.Priority"]
    """<p>The setting that determines the processing order of the rule group among the rule groups that are associated with a single VPC. DNS Firewall filters VPC traffic starting from rule group with the lowest numeric priority setting. </p>"""
    mutation_protection: NotRequired[
        "capo_route53resolver.types.mutation_protection_status.MutationProtectionStatus"
    ]
    """<p>If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections. </p>"""
    managed_owner_name: NotRequired[
        "capo_route53resolver.types.service_principle.ServicePrinciple"
    ]
    """<p>The owner of the association, used only for associations that are not managed by you. If you use Firewall Manager to manage your DNS Firewalls, then this reports Firewall Manager as the managed owner.</p>"""
    status: NotRequired[
        "capo_route53resolver.types.firewall_rule_group_association_status.FirewallRuleGroupAssociationStatus"
    ]
    """<p>The current status of the association.</p>"""
    status_message: NotRequired[
        "capo_route53resolver.types.status_message.StatusMessage"
    ]
    """<p>Additional information about the status of the response, if available.</p>"""
    creator_request_id: NotRequired[
        "capo_route53resolver.types.creator_request_id.CreatorRequestId"
    ]
    """<p>A unique string defined by you to identify the request. This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp. </p>"""
    creation_time: NotRequired[
        "capo_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the association was created, in Unix time format and Coordinated Universal Time (UTC). </p>"""
    modification_time: NotRequired[
        "capo_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the association was last modified, in Unix time format and Coordinated Universal Time (UTC).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallRuleGroupAssociation) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "firewall_rule_group_id" in value:
        out["FirewallRuleGroupId"] = value["firewall_rule_group_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "mutation_protection" in value:
        import capo_route53resolver.types.mutation_protection_status

        out["MutationProtection"] = (
            capo_route53resolver.types.mutation_protection_status.serialize_aws_json_1_1(
                value["mutation_protection"]
            )
        )
    if "managed_owner_name" in value:
        out["ManagedOwnerName"] = value["managed_owner_name"]
    if "status" in value:
        import capo_route53resolver.types.firewall_rule_group_association_status

        out["Status"] = (
            capo_route53resolver.types.firewall_rule_group_association_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "creation_time" in value:
        out["CreationTime"] = value["creation_time"]
    if "modification_time" in value:
        out["ModificationTime"] = value["modification_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FirewallRuleGroupAssociation:
    out: FirewallRuleGroupAssociation = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("FirewallRuleGroupId") is not None:
        out["firewall_rule_group_id"] = data["FirewallRuleGroupId"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    if data.get("MutationProtection") is not None:
        import capo_route53resolver.types.mutation_protection_status

        out["mutation_protection"] = (
            capo_route53resolver.types.mutation_protection_status.deserialize_aws_json_1_1(
                data["MutationProtection"]
            )
        )
    if data.get("ManagedOwnerName") is not None:
        out["managed_owner_name"] = data["ManagedOwnerName"]
    if data.get("Status") is not None:
        import capo_route53resolver.types.firewall_rule_group_association_status

        out["status"] = (
            capo_route53resolver.types.firewall_rule_group_association_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    if data.get("CreationTime") is not None:
        out["creation_time"] = data["CreationTime"]
    if data.get("ModificationTime") is not None:
        out["modification_time"] = data["ModificationTime"]
    return out
