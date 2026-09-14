"""Generated from Smithy shape ``com.amazonaws.securityhub#ServiceNowDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.connector_auth_status
    import capo_securityhub.types.non_empty_string


class ServiceNowDetail(TypedDict, closed=True):
    instance_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The instanceName of ServiceNow ITSM.</p>"""
    secret_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that contains the ServiceNow credentials.</p>"""
    auth_status: NotRequired[
        "capo_securityhub.types.connector_auth_status.ConnectorAuthStatus"
    ]
    """<p>The status of the authorization between ServiceNow and the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNowDetail) -> dict:
    out: dict = {}
    if "instance_name" in value:
        out["InstanceName"] = value["instance_name"]
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    if "auth_status" in value:
        import capo_securityhub.types.connector_auth_status

        out["AuthStatus"] = capo_securityhub.types.connector_auth_status.serialize_json(
            value["auth_status"]
        )
    return out


def deserialize_json(data: dict) -> ServiceNowDetail:
    out: ServiceNowDetail = {}  # type: ignore[typeddict-item]
    if data.get("InstanceName") is not None:
        out["instance_name"] = data["InstanceName"]
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    if data.get("AuthStatus") is not None:
        import capo_securityhub.types.connector_auth_status

        out["auth_status"] = (
            capo_securityhub.types.connector_auth_status.deserialize_json(
                data["AuthStatus"]
            )
        )
    return out
