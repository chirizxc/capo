"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteCustomPermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DeleteCustomPermissionsResponse(TypedDict, closed=True):
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the custom permissions profile.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomPermissionsResponse) -> dict:
    out: dict = {}
    out["Status"] = value.get("status", 0)
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DeleteCustomPermissionsResponse:
    out: DeleteCustomPermissionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = 0
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out
