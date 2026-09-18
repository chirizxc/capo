"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdatePartnerAppRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.boolean
    import capo_sagemaker.types.client_token
    import capo_sagemaker.types.major_minor_version
    import capo_sagemaker.types.non_empty_string64
    import capo_sagemaker.types.partner_app_arn
    import capo_sagemaker.types.partner_app_config
    import capo_sagemaker.types.partner_app_maintenance_config
    import capo_sagemaker.types.tag_list


class UpdatePartnerAppRequest(TypedDict, closed=True):
    arn: NotRequired["capo_sagemaker.types.partner_app_arn.PartnerAppArn"]
    """<p>The ARN of the SageMaker Partner AI App to update.</p>"""
    maintenance_config: NotRequired[
        "capo_sagemaker.types.partner_app_maintenance_config.PartnerAppMaintenanceConfig"
    ]
    """<p>Maintenance configuration settings for the SageMaker Partner AI App.</p>"""
    tier: NotRequired["capo_sagemaker.types.non_empty_string64.NonEmptyString64"]
    """<p>Indicates the instance type and size of the cluster attached to the SageMaker Partner AI App.</p>"""
    application_config: NotRequired[
        "capo_sagemaker.types.partner_app_config.PartnerAppConfig"
    ]
    """<p>Configuration settings for the SageMaker Partner AI App.</p>"""
    enable_iam_session_based_identity: NotRequired[
        "capo_sagemaker.types.boolean.Boolean"
    ]
    """<p>When set to <code>TRUE</code>, the SageMaker Partner AI App sets the Amazon Web Services IAM session name or the authenticated IAM user as the identity of the SageMaker Partner AI App user.</p>"""
    enable_auto_minor_version_upgrade: NotRequired[
        "capo_sagemaker.types.boolean.Boolean"
    ]
    """<p>When set to <code>TRUE</code>, the SageMaker Partner AI App is automatically upgraded to the latest minor version during the next scheduled maintenance window, if one is available.</p>"""
    app_version: NotRequired[
        "capo_sagemaker.types.major_minor_version.MajorMinorVersion"
    ]
    """<p>The semantic version to upgrade the SageMaker Partner AI App to. Must be the same semantic version returned in the <code>AvailableUpgrade</code> field from <code>DescribePartnerApp</code>. Version skipping and downgrades are not supported.</p>"""
    client_token: NotRequired["capo_sagemaker.types.client_token.ClientToken"]
    """<p>A unique token that guarantees that the call to this API is idempotent.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>Each tag consists of a key and an optional value. Tag keys must be unique per resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePartnerAppRequest) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "maintenance_config" in value:
        import capo_sagemaker.types.partner_app_maintenance_config

        out["MaintenanceConfig"] = (
            capo_sagemaker.types.partner_app_maintenance_config.serialize_aws_json_1_1(
                value["maintenance_config"]
            )
        )
    if "tier" in value:
        out["Tier"] = value["tier"]
    if "application_config" in value:
        import capo_sagemaker.types.partner_app_config

        out["ApplicationConfig"] = (
            capo_sagemaker.types.partner_app_config.serialize_aws_json_1_1(
                value["application_config"]
            )
        )
    if "enable_iam_session_based_identity" in value:
        out["EnableIamSessionBasedIdentity"] = value[
            "enable_iam_session_based_identity"
        ]
    if "enable_auto_minor_version_upgrade" in value:
        out["EnableAutoMinorVersionUpgrade"] = value[
            "enable_auto_minor_version_upgrade"
        ]
    if "app_version" in value:
        out["AppVersion"] = value["app_version"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePartnerAppRequest:
    out: UpdatePartnerAppRequest = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("MaintenanceConfig") is not None:
        import capo_sagemaker.types.partner_app_maintenance_config

        out["maintenance_config"] = (
            capo_sagemaker.types.partner_app_maintenance_config.deserialize_aws_json_1_1(
                data["MaintenanceConfig"]
            )
        )
    if data.get("Tier") is not None:
        out["tier"] = data["Tier"]
    if data.get("ApplicationConfig") is not None:
        import capo_sagemaker.types.partner_app_config

        out["application_config"] = (
            capo_sagemaker.types.partner_app_config.deserialize_aws_json_1_1(
                data["ApplicationConfig"]
            )
        )
    if data.get("EnableIamSessionBasedIdentity") is not None:
        out["enable_iam_session_based_identity"] = data["EnableIamSessionBasedIdentity"]
    if data.get("EnableAutoMinorVersionUpgrade") is not None:
        out["enable_auto_minor_version_upgrade"] = data["EnableAutoMinorVersionUpgrade"]
    if data.get("AppVersion") is not None:
        out["app_version"] = data["AppVersion"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
