"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsMskClusterClusterInfoDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_details
    import capo_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_details
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsMskClusterClusterInfoDetails(TypedDict, closed=True):
    encryption_info: NotRequired[
        "capo_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_details.AwsMskClusterClusterInfoEncryptionInfoDetails"
    ]
    """<p> Includes encryption-related information, such as the KMS key used for encrypting data at rest and whether you want Amazon MSK to encrypt your data in transit.</p>"""
    current_version: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The current version of the cluster.</p>"""
    number_of_broker_nodes: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The number of broker nodes in the cluster.</p>"""
    cluster_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the cluster.</p>"""
    client_authentication: NotRequired[
        "capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_details.AwsMskClusterClusterInfoClientAuthenticationDetails"
    ]
    """<p> Provides information for different modes of client authentication.</p>"""
    enhanced_monitoring: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> Specifies the level of monitoring for the cluster. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsMskClusterClusterInfoDetails) -> dict:
    out: dict = {}
    if "encryption_info" in value:
        import capo_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_details

        out["EncryptionInfo"] = (
            capo_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_details.serialize_json(
                value["encryption_info"]
            )
        )
    if "current_version" in value:
        out["CurrentVersion"] = value["current_version"]
    if "number_of_broker_nodes" in value:
        out["NumberOfBrokerNodes"] = value["number_of_broker_nodes"]
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "client_authentication" in value:
        import capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_details

        out["ClientAuthentication"] = (
            capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_details.serialize_json(
                value["client_authentication"]
            )
        )
    if "enhanced_monitoring" in value:
        out["EnhancedMonitoring"] = value["enhanced_monitoring"]
    return out


def deserialize_json(data: dict) -> AwsMskClusterClusterInfoDetails:
    out: AwsMskClusterClusterInfoDetails = {}  # type: ignore[typeddict-item]
    if data.get("EncryptionInfo") is not None:
        import capo_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_details

        out["encryption_info"] = (
            capo_securityhub.types.aws_msk_cluster_cluster_info_encryption_info_details.deserialize_json(
                data["EncryptionInfo"]
            )
        )
    if data.get("CurrentVersion") is not None:
        out["current_version"] = data["CurrentVersion"]
    if data.get("NumberOfBrokerNodes") is not None:
        out["number_of_broker_nodes"] = data["NumberOfBrokerNodes"]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    if data.get("ClientAuthentication") is not None:
        import capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_details

        out["client_authentication"] = (
            capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_details.deserialize_json(
                data["ClientAuthentication"]
            )
        )
    if data.get("EnhancedMonitoring") is not None:
        out["enhanced_monitoring"] = data["EnhancedMonitoring"]
    return out
