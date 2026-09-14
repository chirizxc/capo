"""Generated from Smithy shape ``com.amazonaws.emr#SimplifiedApplication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.string


class SimplifiedApplication(TypedDict, closed=True):
    name: NotRequired["capo_emr.types.string.String"]
    """<p>The returned release label application name. For example, <code>hadoop</code>.</p>"""
    version: NotRequired["capo_emr.types.string.String"]
    """<p>The returned release label application version. For example, <code>3.2.1</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SimplifiedApplication) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SimplifiedApplication:
    out: SimplifiedApplication = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    return out
