"""Generated from Smithy shape ``com.amazonaws.emr#Studio``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.arn_type
    import capo_emr.types.auth_mode
    import capo_emr.types.boolean_object
    import capo_emr.types.date
    import capo_emr.types.idc_user_assignment
    import capo_emr.types.subnet_id_list
    import capo_emr.types.tag_list
    import capo_emr.types.xml_string
    import capo_emr.types.xml_string_max_len256


class Studio(TypedDict, closed=True):
    studio_id: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The ID of the Amazon EMR Studio.</p>"""
    studio_arn: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The Amazon Resource Name (ARN) of the Amazon EMR Studio.</p>"""
    name: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The name of the Amazon EMR Studio.</p>"""
    description: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The detailed description of the Amazon EMR Studio.</p>"""
    auth_mode: NotRequired["capo_emr.types.auth_mode.AuthMode"]
    """<p>Specifies whether the Amazon EMR Studio authenticates users with IAM or IAM Identity Center.</p>"""
    vpc_id: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The ID of the VPC associated with the Amazon EMR Studio.</p>"""
    subnet_ids: NotRequired["capo_emr.types.subnet_id_list.SubnetIdList"]
    """<p>The list of IDs of the subnets associated with the Amazon EMR Studio.</p>"""
    service_role: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The name of the IAM role assumed by the Amazon EMR Studio.</p>"""
    user_role: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The name of the IAM role assumed by users logged in to the Amazon EMR Studio. A Studio only requires a <code>UserRole</code> when you use IAM authentication.</p>"""
    workspace_security_group_id: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The ID of the Workspace security group associated with the Amazon EMR Studio. The Workspace security group allows outbound network traffic to resources in the Engine security group and to the internet.</p>"""
    engine_security_group_id: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The ID of the Engine security group associated with the Amazon EMR Studio. The Engine security group allows inbound network traffic from resources in the Workspace security group.</p>"""
    url: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The unique access URL of the Amazon EMR Studio.</p>"""
    creation_time: NotRequired["capo_emr.types.date.Date"]
    """<p>The time the Amazon EMR Studio was created.</p>"""
    default_s3_location: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The Amazon S3 location to back up Amazon EMR Studio Workspaces and notebook files.</p>"""
    idp_auth_url: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>Your identity provider's authentication endpoint. Amazon EMR Studio redirects federated users to this endpoint for authentication when logging in to a Studio with the Studio URL.</p>"""
    idp_relay_state_parameter_name: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The name of your identity provider's <code>RelayState</code> parameter.</p>"""
    tags: NotRequired["capo_emr.types.tag_list.TagList"]
    """<p>A list of tags associated with the Amazon EMR Studio.</p>"""
    idc_instance_arn: NotRequired["capo_emr.types.arn_type.ArnType"]
    """<p> The ARN of the IAM Identity Center instance the Studio application belongs to. </p>"""
    trusted_identity_propagation_enabled: NotRequired[
        "capo_emr.types.boolean_object.BooleanObject"
    ]
    """<p> Indicates whether the Studio has Trusted identity propagation enabled. The default value is <code>false</code>. </p>"""
    idc_user_assignment: NotRequired[
        "capo_emr.types.idc_user_assignment.IdcUserAssignment"
    ]
    """<p> Indicates whether the Studio has <code>REQUIRED</code> or <code>OPTIONAL</code> IAM Identity Center user assignment. If the value is set to <code>REQUIRED</code>, users must be explicitly assigned to the Studio application to access the Studio. </p>"""
    encryption_key_arn: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The KMS key identifier (ARN) used to encrypt Amazon EMR Studio workspace and notebook files when backed up to Amazon S3.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Studio) -> dict:
    out: dict = {}
    if "studio_id" in value:
        out["StudioId"] = value["studio_id"]
    if "studio_arn" in value:
        out["StudioArn"] = value["studio_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "auth_mode" in value:
        import capo_emr.types.auth_mode

        out["AuthMode"] = capo_emr.types.auth_mode.serialize_aws_json_1_1(
            value["auth_mode"]
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import capo_emr.types.subnet_id_list

        out["SubnetIds"] = capo_emr.types.subnet_id_list.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "service_role" in value:
        out["ServiceRole"] = value["service_role"]
    if "user_role" in value:
        out["UserRole"] = value["user_role"]
    if "workspace_security_group_id" in value:
        out["WorkspaceSecurityGroupId"] = value["workspace_security_group_id"]
    if "engine_security_group_id" in value:
        out["EngineSecurityGroupId"] = value["engine_security_group_id"]
    if "url" in value:
        out["Url"] = value["url"]
    if "creation_time" in value:
        import capo_emr.types.date

        out["CreationTime"] = capo_emr.types.date.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "default_s3_location" in value:
        out["DefaultS3Location"] = value["default_s3_location"]
    if "idp_auth_url" in value:
        out["IdpAuthUrl"] = value["idp_auth_url"]
    if "idp_relay_state_parameter_name" in value:
        out["IdpRelayStateParameterName"] = value["idp_relay_state_parameter_name"]
    if "tags" in value:
        import capo_emr.types.tag_list

        out["Tags"] = capo_emr.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "idc_instance_arn" in value:
        out["IdcInstanceArn"] = value["idc_instance_arn"]
    if "trusted_identity_propagation_enabled" in value:
        out["TrustedIdentityPropagationEnabled"] = value[
            "trusted_identity_propagation_enabled"
        ]
    if "idc_user_assignment" in value:
        import capo_emr.types.idc_user_assignment

        out["IdcUserAssignment"] = (
            capo_emr.types.idc_user_assignment.serialize_aws_json_1_1(
                value["idc_user_assignment"]
            )
        )
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Studio:
    out: Studio = {}  # type: ignore[typeddict-item]
    if data.get("StudioId") is not None:
        out["studio_id"] = data["StudioId"]
    if data.get("StudioArn") is not None:
        out["studio_arn"] = data["StudioArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("AuthMode") is not None:
        import capo_emr.types.auth_mode

        out["auth_mode"] = capo_emr.types.auth_mode.deserialize_aws_json_1_1(
            data["AuthMode"]
        )
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SubnetIds") is not None:
        import capo_emr.types.subnet_id_list

        out["subnet_ids"] = capo_emr.types.subnet_id_list.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    if data.get("ServiceRole") is not None:
        out["service_role"] = data["ServiceRole"]
    if data.get("UserRole") is not None:
        out["user_role"] = data["UserRole"]
    if data.get("WorkspaceSecurityGroupId") is not None:
        out["workspace_security_group_id"] = data["WorkspaceSecurityGroupId"]
    if data.get("EngineSecurityGroupId") is not None:
        out["engine_security_group_id"] = data["EngineSecurityGroupId"]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    if data.get("CreationTime") is not None:
        import capo_emr.types.date

        out["creation_time"] = capo_emr.types.date.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("DefaultS3Location") is not None:
        out["default_s3_location"] = data["DefaultS3Location"]
    if data.get("IdpAuthUrl") is not None:
        out["idp_auth_url"] = data["IdpAuthUrl"]
    if data.get("IdpRelayStateParameterName") is not None:
        out["idp_relay_state_parameter_name"] = data["IdpRelayStateParameterName"]
    if data.get("Tags") is not None:
        import capo_emr.types.tag_list

        out["tags"] = capo_emr.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if data.get("IdcInstanceArn") is not None:
        out["idc_instance_arn"] = data["IdcInstanceArn"]
    if data.get("TrustedIdentityPropagationEnabled") is not None:
        out["trusted_identity_propagation_enabled"] = data[
            "TrustedIdentityPropagationEnabled"
        ]
    if data.get("IdcUserAssignment") is not None:
        import capo_emr.types.idc_user_assignment

        out["idc_user_assignment"] = (
            capo_emr.types.idc_user_assignment.deserialize_aws_json_1_1(
                data["IdcUserAssignment"]
            )
        )
    if data.get("EncryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    return out
