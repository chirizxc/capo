"""Generated from Smithy shape ``com.amazonaws.sagemaker#AppDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.app_name
    import capo_sagemaker.types.app_status
    import capo_sagemaker.types.app_type
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.domain_id
    import capo_sagemaker.types.resource_spec
    import capo_sagemaker.types.space_name
    import capo_sagemaker.types.user_profile_name


class AppDetails(TypedDict, closed=True):
    domain_id: NotRequired["capo_sagemaker.types.domain_id.DomainId"]
    """<p>The domain ID.</p>"""
    user_profile_name: NotRequired[
        "capo_sagemaker.types.user_profile_name.UserProfileName"
    ]
    """<p>The user profile name.</p>"""
    space_name: NotRequired["capo_sagemaker.types.space_name.SpaceName"]
    """<p>The name of the space.</p>"""
    app_type: NotRequired["capo_sagemaker.types.app_type.AppType"]
    """<p>The type of app.</p>"""
    app_name: NotRequired["capo_sagemaker.types.app_name.AppName"]
    """<p>The name of the app.</p>"""
    status: NotRequired["capo_sagemaker.types.app_status.AppStatus"]
    """<p>The status.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>The creation time.</p>"""
    resource_spec: NotRequired["capo_sagemaker.types.resource_spec.ResourceSpec"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppDetails) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "user_profile_name" in value:
        out["UserProfileName"] = value["user_profile_name"]
    if "space_name" in value:
        out["SpaceName"] = value["space_name"]
    if "app_type" in value:
        import capo_sagemaker.types.app_type

        out["AppType"] = capo_sagemaker.types.app_type.serialize_aws_json_1_1(
            value["app_type"]
        )
    if "app_name" in value:
        out["AppName"] = value["app_name"]
    if "status" in value:
        import capo_sagemaker.types.app_status

        out["Status"] = capo_sagemaker.types.app_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "creation_time" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTime"] = capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "resource_spec" in value:
        import capo_sagemaker.types.resource_spec

        out["ResourceSpec"] = capo_sagemaker.types.resource_spec.serialize_aws_json_1_1(
            value["resource_spec"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AppDetails:
    out: AppDetails = {}  # type: ignore[typeddict-item]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    if data.get("UserProfileName") is not None:
        out["user_profile_name"] = data["UserProfileName"]
    if data.get("SpaceName") is not None:
        out["space_name"] = data["SpaceName"]
    if data.get("AppType") is not None:
        import capo_sagemaker.types.app_type

        out["app_type"] = capo_sagemaker.types.app_type.deserialize_aws_json_1_1(
            data["AppType"]
        )
    if data.get("AppName") is not None:
        out["app_name"] = data["AppName"]
    if data.get("Status") is not None:
        import capo_sagemaker.types.app_status

        out["status"] = capo_sagemaker.types.app_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.creation_time

        out["creation_time"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if data.get("ResourceSpec") is not None:
        import capo_sagemaker.types.resource_spec

        out["resource_spec"] = (
            capo_sagemaker.types.resource_spec.deserialize_aws_json_1_1(
                data["ResourceSpec"]
            )
        )
    return out
