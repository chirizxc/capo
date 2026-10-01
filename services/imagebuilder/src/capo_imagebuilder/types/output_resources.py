"""Generated from Smithy shape ``com.amazonaws.imagebuilder#OutputResources``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.ami_list
    import capo_imagebuilder.types.container_list


class OutputResources(TypedDict, closed=True):
    amis: NotRequired["capo_imagebuilder.types.ami_list.AmiList"]
    """<p>The Amazon EC2 AMIs created by this image. The list contains one entry per AMI, including copies that distribution created in each target Amazon Web Services Region and account.</p>"""
    containers: NotRequired["capo_imagebuilder.types.container_list.ContainerList"]
    """<p>The container images that Image Builder created when it built this image, stored in the output Amazon ECR repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputResources) -> dict:
    out: dict = {}
    if "amis" in value:
        import capo_imagebuilder.types.ami_list

        out["amis"] = capo_imagebuilder.types.ami_list.serialize_json(value["amis"])
    if "containers" in value:
        import capo_imagebuilder.types.container_list

        out["containers"] = capo_imagebuilder.types.container_list.serialize_json(
            value["containers"]
        )
    return out


def deserialize_json(data: dict) -> OutputResources:
    out: OutputResources = {}  # type: ignore[typeddict-item]
    if data.get("amis") is not None:
        import capo_imagebuilder.types.ami_list

        out["amis"] = capo_imagebuilder.types.ami_list.deserialize_json(data["amis"])
    if data.get("containers") is not None:
        import capo_imagebuilder.types.container_list

        out["containers"] = capo_imagebuilder.types.container_list.deserialize_json(
            data["containers"]
        )
    return out
