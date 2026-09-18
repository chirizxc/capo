"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteContainerImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.container_service_name
    import capo_lightsail.types.string


class DeleteContainerImageRequest(TypedDict, closed=True):
    service_name: "capo_lightsail.types.container_service_name.ContainerServiceName"
    """<p>The name of the container service for which to delete a registered container image.</p>"""
    image: "capo_lightsail.types.string.string"
    """<p>The name of the container image to delete from the container service.</p> <p>Use the <code>GetContainerImages</code> action to get the name of the container images that are registered to a container service.</p> <note> <p>Container images sourced from your Lightsail container service, that are registered and stored on your service, start with a colon (<code>:</code>). For example, <code>:container-service-1.mystaticwebsite.1</code>. Container images sourced from a public registry like Docker Hub don't start with a colon. For example, <code>nginx:latest</code> or <code>nginx</code>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteContainerImageRequest) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    out["image"] = value["image"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteContainerImageRequest:
    out: DeleteContainerImageRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError("DeleteContainerImageRequest.service_name required")
    if data.get("image") is not None:
        out["image"] = data["image"]
    else:
        raise DeserializationError("DeleteContainerImageRequest.image required")
    return out
