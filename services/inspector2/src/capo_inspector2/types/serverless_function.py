"""Generated from Smithy shape ``com.amazonaws.inspector2#ServerlessFunction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.architecture_list
    import capo_inspector2.types.cloud_security_group_id_list
    import capo_inspector2.types.cloud_subnet_id_list
    import capo_inspector2.types.date_time_timestamp
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.package_type
    import capo_inspector2.types.serverless_function_layer_list


class ServerlessFunction(TypedDict, closed=True):
    serverless_function_name: NotRequired[
        "capo_inspector2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the serverless function.</p>"""
    runtime: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The runtime of the serverless function.</p>"""
    version: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The version of the serverless function.</p>"""
    code_digest: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The code digest of the serverless function.</p>"""
    last_modified_at: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The date and time the serverless function was last modified.</p>"""
    network_id: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The network ID associated with the serverless function.</p>"""
    subnet_ids: NotRequired[
        "capo_inspector2.types.cloud_subnet_id_list.CloudSubnetIdList"
    ]
    """<p>The subnet IDs associated with the serverless function.</p>"""
    security_group_ids: NotRequired[
        "capo_inspector2.types.cloud_security_group_id_list.CloudSecurityGroupIdList"
    ]
    """<p>The security group IDs associated with the serverless function.</p>"""
    execution_role: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The execution role of the serverless function.</p>"""
    package_type: NotRequired["capo_inspector2.types.package_type.PackageType"]
    """<p>The package type of the serverless function.</p>"""
    architectures: NotRequired[
        "capo_inspector2.types.architecture_list.ArchitectureList"
    ]
    """<p>The architectures of the serverless function.</p>"""
    layers: NotRequired[
        "capo_inspector2.types.serverless_function_layer_list.ServerlessFunctionLayerList"
    ]
    """<p>The layers of the serverless function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerlessFunction) -> dict:
    out: dict = {}
    if "serverless_function_name" in value:
        out["serverlessFunctionName"] = value["serverless_function_name"]
    if "runtime" in value:
        out["runtime"] = value["runtime"]
    if "version" in value:
        out["version"] = value["version"]
    if "code_digest" in value:
        out["codeDigest"] = value["code_digest"]
    if "last_modified_at" in value:
        import capo_inspector2.types.date_time_timestamp

        out["lastModifiedAt"] = (
            capo_inspector2.types.date_time_timestamp.serialize_json(
                value["last_modified_at"]
            )
        )
    if "network_id" in value:
        out["networkId"] = value["network_id"]
    if "subnet_ids" in value:
        import capo_inspector2.types.cloud_subnet_id_list

        out["subnetIds"] = capo_inspector2.types.cloud_subnet_id_list.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_inspector2.types.cloud_security_group_id_list

        out["securityGroupIds"] = (
            capo_inspector2.types.cloud_security_group_id_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "execution_role" in value:
        out["executionRole"] = value["execution_role"]
    if "package_type" in value:
        out["packageType"] = value["package_type"]
    if "architectures" in value:
        import capo_inspector2.types.architecture_list

        out["architectures"] = capo_inspector2.types.architecture_list.serialize_json(
            value["architectures"]
        )
    if "layers" in value:
        import capo_inspector2.types.serverless_function_layer_list

        out["layers"] = (
            capo_inspector2.types.serverless_function_layer_list.serialize_json(
                value["layers"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServerlessFunction:
    out: ServerlessFunction = {}  # type: ignore[typeddict-item]
    if data.get("serverlessFunctionName") is not None:
        out["serverless_function_name"] = data["serverlessFunctionName"]
    if data.get("runtime") is not None:
        out["runtime"] = data["runtime"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("codeDigest") is not None:
        out["code_digest"] = data["codeDigest"]
    if data.get("lastModifiedAt") is not None:
        import capo_inspector2.types.date_time_timestamp

        out["last_modified_at"] = (
            capo_inspector2.types.date_time_timestamp.deserialize_json(
                data["lastModifiedAt"]
            )
        )
    if data.get("networkId") is not None:
        out["network_id"] = data["networkId"]
    if data.get("subnetIds") is not None:
        import capo_inspector2.types.cloud_subnet_id_list

        out["subnet_ids"] = capo_inspector2.types.cloud_subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    if data.get("securityGroupIds") is not None:
        import capo_inspector2.types.cloud_security_group_id_list

        out["security_group_ids"] = (
            capo_inspector2.types.cloud_security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if data.get("executionRole") is not None:
        out["execution_role"] = data["executionRole"]
    if data.get("packageType") is not None:
        out["package_type"] = data["packageType"]
    if data.get("architectures") is not None:
        import capo_inspector2.types.architecture_list

        out["architectures"] = capo_inspector2.types.architecture_list.deserialize_json(
            data["architectures"]
        )
    if data.get("layers") is not None:
        import capo_inspector2.types.serverless_function_layer_list

        out["layers"] = (
            capo_inspector2.types.serverless_function_layer_list.deserialize_json(
                data["layers"]
            )
        )
    return out
