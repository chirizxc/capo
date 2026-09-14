"""Generated from Smithy shape ``com.amazonaws.finspace#Environment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.description
    import capo_finspace.types.environment_arn
    import capo_finspace.types.environment_name
    import capo_finspace.types.environment_status
    import capo_finspace.types.federation_mode
    import capo_finspace.types.federation_parameters
    import capo_finspace.types.id_type
    import capo_finspace.types.kms_key_id
    import capo_finspace.types.sms_domain_url
    import capo_finspace.types.url


class Environment(TypedDict, closed=True):
    name: NotRequired["capo_finspace.types.environment_name.EnvironmentName"]
    """<p>The name of the FinSpace environment.</p>"""
    environment_id: NotRequired["capo_finspace.types.id_type.IdType"]
    """<p>The identifier of the FinSpace environment.</p>"""
    aws_account_id: NotRequired["capo_finspace.types.id_type.IdType"]
    """<p>The ID of the AWS account in which the FinSpace environment is created.</p>"""
    status: NotRequired["capo_finspace.types.environment_status.EnvironmentStatus"]
    """<p>The current status of creation of the FinSpace environment.</p>"""
    environment_url: NotRequired["capo_finspace.types.url.url"]
    """<p>The sign-in URL for the web application of your FinSpace environment.</p>"""
    description: NotRequired["capo_finspace.types.description.Description"]
    """<p>The description of the FinSpace environment.</p>"""
    environment_arn: NotRequired["capo_finspace.types.environment_arn.EnvironmentArn"]
    """<p>The Amazon Resource Name (ARN) of your FinSpace environment.</p>"""
    sage_maker_studio_domain_url: NotRequired[
        "capo_finspace.types.sms_domain_url.SmsDomainUrl"
    ]
    """<p>The URL of the integrated FinSpace notebook environment in your web application.</p>"""
    kms_key_id: NotRequired["capo_finspace.types.kms_key_id.KmsKeyId"]
    """<p>The KMS key id used to encrypt in the FinSpace environment.</p>"""
    dedicated_service_account_id: NotRequired["capo_finspace.types.id_type.IdType"]
    """<p>The AWS account ID of the dedicated service account associated with your FinSpace environment.</p>"""
    federation_mode: NotRequired["capo_finspace.types.federation_mode.FederationMode"]
    """<p>The authentication mode for the environment.</p>"""
    federation_parameters: NotRequired[
        "capo_finspace.types.federation_parameters.FederationParameters"
    ]
    """<p>Configuration information when authentication mode is FEDERATED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Environment) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "status" in value:
        import capo_finspace.types.environment_status

        out["status"] = capo_finspace.types.environment_status.serialize_json(
            value["status"]
        )
    if "environment_url" in value:
        out["environmentUrl"] = value["environment_url"]
    if "description" in value:
        out["description"] = value["description"]
    if "environment_arn" in value:
        out["environmentArn"] = value["environment_arn"]
    if "sage_maker_studio_domain_url" in value:
        out["sageMakerStudioDomainUrl"] = value["sage_maker_studio_domain_url"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "dedicated_service_account_id" in value:
        out["dedicatedServiceAccountId"] = value["dedicated_service_account_id"]
    if "federation_mode" in value:
        import capo_finspace.types.federation_mode

        out["federationMode"] = capo_finspace.types.federation_mode.serialize_json(
            value["federation_mode"]
        )
    if "federation_parameters" in value:
        import capo_finspace.types.federation_parameters

        out["federationParameters"] = (
            capo_finspace.types.federation_parameters.serialize_json(
                value["federation_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> Environment:
    out: Environment = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    if data.get("awsAccountId") is not None:
        out["aws_account_id"] = data["awsAccountId"]
    if data.get("status") is not None:
        import capo_finspace.types.environment_status

        out["status"] = capo_finspace.types.environment_status.deserialize_json(
            data["status"]
        )
    if data.get("environmentUrl") is not None:
        out["environment_url"] = data["environmentUrl"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("environmentArn") is not None:
        out["environment_arn"] = data["environmentArn"]
    if data.get("sageMakerStudioDomainUrl") is not None:
        out["sage_maker_studio_domain_url"] = data["sageMakerStudioDomainUrl"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("dedicatedServiceAccountId") is not None:
        out["dedicated_service_account_id"] = data["dedicatedServiceAccountId"]
    if data.get("federationMode") is not None:
        import capo_finspace.types.federation_mode

        out["federation_mode"] = capo_finspace.types.federation_mode.deserialize_json(
            data["federationMode"]
        )
    if data.get("federationParameters") is not None:
        import capo_finspace.types.federation_parameters

        out["federation_parameters"] = (
            capo_finspace.types.federation_parameters.deserialize_json(
                data["federationParameters"]
            )
        )
    return out
