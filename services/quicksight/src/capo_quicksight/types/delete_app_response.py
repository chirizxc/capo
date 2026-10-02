"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteAppResponse``."""

from typing_extensions import NotRequired, TypedDict


class DeleteAppResponse(TypedDict, closed=True):
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DeleteAppResponse:
    out: DeleteAppResponse = {}  # type: ignore[typeddict-item]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out
