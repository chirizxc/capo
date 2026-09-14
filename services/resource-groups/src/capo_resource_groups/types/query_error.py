"""Generated from Smithy shape ``com.amazonaws.resourcegroups#QueryError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.query_error_code
    import capo_resource_groups.types.query_error_message


class QueryError(TypedDict, closed=True):
    error_code: NotRequired[
        "capo_resource_groups.types.query_error_code.QueryErrorCode"
    ]
    """<p>Specifies the error code that was raised.</p>"""
    message: NotRequired[
        "capo_resource_groups.types.query_error_message.QueryErrorMessage"
    ]
    """<p>A message that explains the <code>ErrorCode</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryError) -> dict:
    out: dict = {}
    if "error_code" in value:
        import capo_resource_groups.types.query_error_code

        out["ErrorCode"] = capo_resource_groups.types.query_error_code.serialize_json(
            value["error_code"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> QueryError:
    out: QueryError = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        import capo_resource_groups.types.query_error_code

        out["error_code"] = (
            capo_resource_groups.types.query_error_code.deserialize_json(
                data["ErrorCode"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
