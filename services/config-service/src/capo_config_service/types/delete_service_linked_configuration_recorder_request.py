"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteServiceLinkedConfigurationRecorderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.amazon_resource_name
    import capo_config_service.types.service_principal


class DeleteServiceLinkedConfigurationRecorderRequest(TypedDict, closed=True):
    service_principal: NotRequired[
        "capo_config_service.types.service_principal.ServicePrincipal"
    ]
    """<p>The service principal of the Amazon Web Services service for the service-linked configuration recorder that you want to delete. This field is only supported for Amazon Web Services service principals. For third-party service-linked configuration recorders, use <code>Arn</code> instead.</p>"""
    arn: NotRequired[
        "capo_config_service.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the service-linked configuration recorder that you want to delete. For third-party service-linked configuration recorders, you must use <code>Arn</code>. You must specify exactly one of <code>Arn</code> or <code>ServicePrincipal</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DeleteServiceLinkedConfigurationRecorderRequest,
) -> dict:
    out: dict = {}
    if "service_principal" in value:
        out["ServicePrincipal"] = value["service_principal"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeleteServiceLinkedConfigurationRecorderRequest:
    out: DeleteServiceLinkedConfigurationRecorderRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServicePrincipal") is not None:
        out["service_principal"] = data["ServicePrincipal"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out
