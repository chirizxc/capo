"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateDataSourcePermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.resource_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class UpdateDataSourcePermissionsResponse(TypedDict, closed=True):
    data_source_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the data source.</p>"""
    data_source_id: NotRequired["capo_quicksight.types.resource_id.ResourceId"]
    """<p>The ID of the data source. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataSourcePermissionsResponse) -> dict:
    out: dict = {}
    if "data_source_arn" in value:
        out["DataSourceArn"] = value["data_source_arn"]
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateDataSourcePermissionsResponse:
    out: UpdateDataSourcePermissionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("DataSourceArn") is not None:
        out["data_source_arn"] = data["DataSourceArn"]
    if data.get("DataSourceId") is not None:
        out["data_source_id"] = data["DataSourceId"]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out
