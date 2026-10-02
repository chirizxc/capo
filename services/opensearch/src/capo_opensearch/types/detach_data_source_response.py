"""Generated from Smithy shape ``com.amazonaws.opensearch#DetachDataSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.arn
    import capo_opensearch.types.id


class DetachDataSourceResponse(TypedDict, closed=True):
    id: NotRequired["capo_opensearch.types.id.Id"]
    """<p>The unique identifier of the OpenSearch application.</p>"""
    arn: NotRequired["capo_opensearch.types.arn.ARN"]
    data_source_arn: NotRequired["capo_opensearch.types.arn.ARN"]


# --- restJson1 ser/de ---
def serialize_json(value: DetachDataSourceResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "data_source_arn" in value:
        out["dataSourceArn"] = value["data_source_arn"]
    return out


def deserialize_json(data: dict) -> DetachDataSourceResponse:
    out: DetachDataSourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("dataSourceArn") is not None:
        out["data_source_arn"] = data["dataSourceArn"]
    return out
