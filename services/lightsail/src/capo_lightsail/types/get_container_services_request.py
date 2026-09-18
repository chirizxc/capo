"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContainerServicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.container_service_name


class GetContainerServicesRequest(TypedDict, closed=True):
    service_name: NotRequired[
        "capo_lightsail.types.container_service_name.ContainerServiceName"
    ]
    """<p>The name of the container service for which to return information.</p> <p>When omitted, the response includes all of your container services in the Amazon Web Services Region where the request is made.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContainerServicesRequest) -> dict:
    out: dict = {}
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContainerServicesRequest:
    out: GetContainerServicesRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    return out
