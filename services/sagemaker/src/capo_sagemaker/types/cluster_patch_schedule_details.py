"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterPatchScheduleDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.timestamp


class ClusterPatchScheduleDetails(TypedDict, closed=True):
    next_patch_date: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time of the next scheduled automatic patch.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterPatchScheduleDetails) -> dict:
    out: dict = {}
    if "next_patch_date" in value:
        import capo_sagemaker.types.timestamp

        out["NextPatchDate"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["next_patch_date"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterPatchScheduleDetails:
    out: ClusterPatchScheduleDetails = {}  # type: ignore[typeddict-item]
    if data.get("NextPatchDate") is not None:
        import capo_sagemaker.types.timestamp

        out["next_patch_date"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["NextPatchDate"]
            )
        )
    return out
