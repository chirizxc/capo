"""Generated from Smithy shape ``com.amazonaws.kendra#DescribeExperienceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.description
    import capo_kendra.types.error_message
    import capo_kendra.types.experience_configuration
    import capo_kendra.types.experience_endpoints
    import capo_kendra.types.experience_id
    import capo_kendra.types.experience_name
    import capo_kendra.types.experience_status
    import capo_kendra.types.index_id
    import capo_kendra.types.role_arn
    import capo_kendra.types.timestamp


class DescribeExperienceResponse(TypedDict, closed=True):
    id: NotRequired["capo_kendra.types.experience_id.ExperienceId"]
    """<p>Shows the identifier of your Amazon Kendra experience.</p>"""
    index_id: NotRequired["capo_kendra.types.index_id.IndexId"]
    """<p>Shows the identifier of the index for your Amazon Kendra experience.</p>"""
    name: NotRequired["capo_kendra.types.experience_name.ExperienceName"]
    """<p>Shows the name of your Amazon Kendra experience.</p>"""
    endpoints: NotRequired["capo_kendra.types.experience_endpoints.ExperienceEndpoints"]
    """<p>Shows the endpoint URLs for your Amazon Kendra experiences. The URLs are unique and fully hosted by Amazon Web Services.</p>"""
    configuration: NotRequired[
        "capo_kendra.types.experience_configuration.ExperienceConfiguration"
    ]
    """<p>Shows the configuration information for your Amazon Kendra experience. This includes <code>ContentSourceConfiguration</code>, which specifies the data source IDs and/or FAQ IDs, and <code>UserIdentityConfiguration</code>, which specifies the user or group information to grant access to your Amazon Kendra experience.</p>"""
    created_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when your Amazon Kendra experience was created.</p>"""
    updated_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when your Amazon Kendra experience was last updated.</p>"""
    description: NotRequired["capo_kendra.types.description.Description"]
    """<p>Shows the description for your Amazon Kendra experience.</p>"""
    status: NotRequired["capo_kendra.types.experience_status.ExperienceStatus"]
    """<p>The current processing status of your Amazon Kendra experience. When the status is <code>ACTIVE</code>, your Amazon Kendra experience is ready to use. When the status is <code>FAILED</code>, the <code>ErrorMessage</code> field contains the reason that this failed.</p>"""
    role_arn: NotRequired["capo_kendra.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role with permission to access the <code>Query</code> API, <code>QuerySuggestions</code> API, <code>SubmitFeedback</code> API, and IAM Identity Center that stores your users and groups information.</p>"""
    error_message: NotRequired["capo_kendra.types.error_message.ErrorMessage"]
    """<p>The reason your Amazon Kendra experience could not properly process.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExperienceResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "index_id" in value:
        out["IndexId"] = value["index_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "endpoints" in value:
        import capo_kendra.types.experience_endpoints

        out["Endpoints"] = (
            capo_kendra.types.experience_endpoints.serialize_aws_json_1_1(
                value["endpoints"]
            )
        )
    if "configuration" in value:
        import capo_kendra.types.experience_configuration

        out["Configuration"] = (
            capo_kendra.types.experience_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "created_at" in value:
        import capo_kendra.types.timestamp

        out["CreatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_kendra.types.timestamp

        out["UpdatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_kendra.types.experience_status

        out["Status"] = capo_kendra.types.experience_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExperienceResponse:
    out: DescribeExperienceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Endpoints") is not None:
        import capo_kendra.types.experience_endpoints

        out["endpoints"] = (
            capo_kendra.types.experience_endpoints.deserialize_aws_json_1_1(
                data["Endpoints"]
            )
        )
    if data.get("Configuration") is not None:
        import capo_kendra.types.experience_configuration

        out["configuration"] = (
            capo_kendra.types.experience_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_kendra.types.timestamp

        out["created_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_kendra.types.timestamp

        out["updated_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Status") is not None:
        import capo_kendra.types.experience_status

        out["status"] = capo_kendra.types.experience_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
