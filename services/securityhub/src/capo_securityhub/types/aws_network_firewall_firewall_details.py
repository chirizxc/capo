"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsNetworkFirewallFirewallDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_network_firewall_firewall_subnet_mappings_list
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsNetworkFirewallFirewallDetails(TypedDict, closed=True):
    delete_protection: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the firewall is protected from deletion. If set to <code>true</code>, then the firewall cannot be deleted.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A description of the firewall.</p>"""
    firewall_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the firewall.</p>"""
    firewall_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the firewall.</p>"""
    firewall_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A descriptive name of the firewall.</p>"""
    firewall_policy_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the firewall policy.</p>"""
    firewall_policy_change_protection: NotRequired[
        "capo_securityhub.types.boolean.Boolean"
    ]
    """<p>Whether the firewall is protected from a change to the firewall policy. If set to <code>true</code>, you cannot associate a different policy with the firewall.</p>"""
    subnet_change_protection: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the firewall is protected from a change to the subnet associations. If set to <code>true</code>, you cannot map different subnets to the firewall.</p>"""
    subnet_mappings: NotRequired[
        "capo_securityhub.types.aws_network_firewall_firewall_subnet_mappings_list.AwsNetworkFirewallFirewallSubnetMappingsList"
    ]
    """<p>The public subnets that Network Firewall uses for the firewall. Each subnet must belong to a different Availability Zone.</p>"""
    vpc_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the VPC where the firewall is used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsNetworkFirewallFirewallDetails) -> dict:
    out: dict = {}
    if "delete_protection" in value:
        out["DeleteProtection"] = value["delete_protection"]
    if "description" in value:
        out["Description"] = value["description"]
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    if "firewall_id" in value:
        out["FirewallId"] = value["firewall_id"]
    if "firewall_name" in value:
        out["FirewallName"] = value["firewall_name"]
    if "firewall_policy_arn" in value:
        out["FirewallPolicyArn"] = value["firewall_policy_arn"]
    if "firewall_policy_change_protection" in value:
        out["FirewallPolicyChangeProtection"] = value[
            "firewall_policy_change_protection"
        ]
    if "subnet_change_protection" in value:
        out["SubnetChangeProtection"] = value["subnet_change_protection"]
    if "subnet_mappings" in value:
        import capo_securityhub.types.aws_network_firewall_firewall_subnet_mappings_list

        out["SubnetMappings"] = (
            capo_securityhub.types.aws_network_firewall_firewall_subnet_mappings_list.serialize_json(
                value["subnet_mappings"]
            )
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> AwsNetworkFirewallFirewallDetails:
    out: AwsNetworkFirewallFirewallDetails = {}  # type: ignore[typeddict-item]
    if data.get("DeleteProtection") is not None:
        out["delete_protection"] = data["DeleteProtection"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    if data.get("FirewallId") is not None:
        out["firewall_id"] = data["FirewallId"]
    if data.get("FirewallName") is not None:
        out["firewall_name"] = data["FirewallName"]
    if data.get("FirewallPolicyArn") is not None:
        out["firewall_policy_arn"] = data["FirewallPolicyArn"]
    if data.get("FirewallPolicyChangeProtection") is not None:
        out["firewall_policy_change_protection"] = data[
            "FirewallPolicyChangeProtection"
        ]
    if data.get("SubnetChangeProtection") is not None:
        out["subnet_change_protection"] = data["SubnetChangeProtection"]
    if data.get("SubnetMappings") is not None:
        import capo_securityhub.types.aws_network_firewall_firewall_subnet_mappings_list

        out["subnet_mappings"] = (
            capo_securityhub.types.aws_network_firewall_firewall_subnet_mappings_list.deserialize_json(
                data["SubnetMappings"]
            )
        )
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    return out
