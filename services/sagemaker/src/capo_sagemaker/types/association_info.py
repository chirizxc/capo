"""Generated from Smithy shape ``com.amazonaws.sagemaker#AssociationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.string2048


class AssociationInfo(TypedDict, closed=True):
    source_arn: NotRequired["capo_sagemaker.types.string2048.String2048"]
    """<p> The Amazon Resource Name (ARN) of the <code>AssociationInfo</code> source. </p>"""
    destination_arn: NotRequired["capo_sagemaker.types.string2048.String2048"]
    """<p> The Amazon Resource Name (ARN) of the <code>AssociationInfo</code> destination. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationInfo) -> dict:
    out: dict = {}
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "destination_arn" in value:
        out["DestinationArn"] = value["destination_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationInfo:
    out: AssociationInfo = {}  # type: ignore[typeddict-item]
    if data.get("SourceArn") is not None:
        out["source_arn"] = data["SourceArn"]
    if data.get("DestinationArn") is not None:
        out["destination_arn"] = data["DestinationArn"]
    return out
