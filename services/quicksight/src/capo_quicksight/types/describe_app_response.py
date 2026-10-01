"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAppResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.app_summary


class DescribeAppResponse(TypedDict, closed=True):
    app: "capo_quicksight.types.app_summary.AppSummary"
    """<p>The information about the app.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppResponse) -> dict:
    out: dict = {}
    import capo_quicksight.types.app_summary

    out["App"] = capo_quicksight.types.app_summary.serialize_json(value["app"])
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeAppResponse:
    out: DescribeAppResponse = {}  # type: ignore[typeddict-item]
    if data.get("App") is not None:
        import capo_quicksight.types.app_summary

        out["app"] = capo_quicksight.types.app_summary.deserialize_json(data["App"])
    else:
        raise DeserializationError("DescribeAppResponse.app required")
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out
