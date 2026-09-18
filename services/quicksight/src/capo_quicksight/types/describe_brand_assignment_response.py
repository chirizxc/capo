"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeBrandAssignmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.string


class DescribeBrandAssignmentResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    brand_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the brand.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBrandAssignmentResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "brand_arn" in value:
        out["BrandArn"] = value["brand_arn"]
    return out


def deserialize_json(data: dict) -> DescribeBrandAssignmentResponse:
    out: DescribeBrandAssignmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    if data.get("BrandArn") is not None:
        out["brand_arn"] = data["BrandArn"]
    return out
