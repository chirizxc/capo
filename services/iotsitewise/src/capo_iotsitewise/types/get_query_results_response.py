"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GetQueryResultsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.column_information_list
    import capo_iotsitewise.types.query_next_token
    import capo_iotsitewise.types.row_list


class GetQueryResultsResponse(TypedDict, closed=True):
    column_info: NotRequired[
        "capo_iotsitewise.types.column_information_list.ColumnInformationList"
    ]
    """<p>A list of column metadata for the query results. Each entry contains the column name and data type. Present when the query status is COMPLETED.</p>"""
    rows: NotRequired["capo_iotsitewise.types.row_list.RowList"]
    """<p>The result rows. Each row is a list of string column values, positional to match the columnInfo order. Present when the query status is COMPLETED.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.query_next_token.QueryNextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueryResultsResponse) -> dict:
    out: dict = {}
    if "column_info" in value:
        import capo_iotsitewise.types.column_information_list

        out["columnInfo"] = (
            capo_iotsitewise.types.column_information_list.serialize_json(
                value["column_info"]
            )
        )
    if "rows" in value:
        import capo_iotsitewise.types.row_list

        out["rows"] = capo_iotsitewise.types.row_list.serialize_json(value["rows"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetQueryResultsResponse:
    out: GetQueryResultsResponse = {}  # type: ignore[typeddict-item]
    if data.get("columnInfo") is not None:
        import capo_iotsitewise.types.column_information_list

        out["column_info"] = (
            capo_iotsitewise.types.column_information_list.deserialize_json(
                data["columnInfo"]
            )
        )
    if data.get("rows") is not None:
        import capo_iotsitewise.types.row_list

        out["rows"] = capo_iotsitewise.types.row_list.deserialize_json(data["rows"])
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
