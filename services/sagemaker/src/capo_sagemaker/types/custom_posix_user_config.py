"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomPosixUserConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.gid
    import capo_sagemaker.types.uid


class CustomPosixUserConfig(TypedDict, closed=True):
    uid: NotRequired["capo_sagemaker.types.uid.Uid"]
    """<p>The POSIX user ID.</p>"""
    gid: NotRequired["capo_sagemaker.types.gid.Gid"]
    """<p>The POSIX group ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomPosixUserConfig) -> dict:
    out: dict = {}
    if "uid" in value:
        out["Uid"] = value["uid"]
    if "gid" in value:
        out["Gid"] = value["gid"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomPosixUserConfig:
    out: CustomPosixUserConfig = {}  # type: ignore[typeddict-item]
    if data.get("Uid") is not None:
        out["uid"] = data["Uid"]
    if data.get("Gid") is not None:
        out["gid"] = data["Gid"]
    return out
