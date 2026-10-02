"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ImageSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.string


class ImageSource(TypedDict, closed=True):
    uri: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The URI of the container image, including the registry, the repository, and the image tag or digest. For example, <code>111122223333.dkr.ecr.us-east-1.amazonaws.com/my-repository:latest</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ImageSource, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "uri" in value:
        pairs.append((f"{key_prefix}Uri", str(value["uri"])))


def deserialize_query(el: Element) -> ImageSource:
    out: ImageSource = {}  # type: ignore[typeddict-item]
    child_uri = el.find("Uri")
    if child_uri is not None:
        out["uri"] = str(child_uri.text or "")
    return out
