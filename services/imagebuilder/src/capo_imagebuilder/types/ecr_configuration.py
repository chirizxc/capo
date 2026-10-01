"""Generated from Smithy shape ``com.amazonaws.imagebuilder#EcrConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.string_list


class EcrConfiguration(TypedDict, closed=True):
    repository_name: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the container repository where Image Builder pushes the container image for the vulnerability scan. Provide the repository name only (a namespace path is allowed, but not the registry hostname); the repository must already exist in your account. If you don't specify a repository name, Image Builder creates the default repository <code>image-builder-image-scanning-repository</code> in your account.</p>"""
    container_tags: NotRequired["capo_imagebuilder.types.string_list.StringList"]
    """<p>Tags for Image Builder to apply to the output container image that Amazon Inspector scans. Tags can help you identify and manage your scanned images.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcrConfiguration) -> dict:
    out: dict = {}
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "container_tags" in value:
        import capo_imagebuilder.types.string_list

        out["containerTags"] = capo_imagebuilder.types.string_list.serialize_json(
            value["container_tags"]
        )
    return out


def deserialize_json(data: dict) -> EcrConfiguration:
    out: EcrConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    if data.get("containerTags") is not None:
        import capo_imagebuilder.types.string_list

        out["container_tags"] = capo_imagebuilder.types.string_list.deserialize_json(
            data["containerTags"]
        )
    return out
