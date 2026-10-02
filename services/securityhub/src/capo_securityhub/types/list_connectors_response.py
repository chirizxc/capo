"""Generated from Smithy shape ``com.amazonaws.securityhub#ListConnectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.cspm_connector_summary_list
    import capo_securityhub.types.next_token


class ListConnectorsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results. If there are no additional results, this value is null.</p>"""
    connectors: NotRequired[
        "capo_securityhub.types.cspm_connector_summary_list.CspmConnectorSummaryList"
    ]
    """<p>An array of connector summaries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "connectors" in value:
        import capo_securityhub.types.cspm_connector_summary_list

        out["Connectors"] = (
            capo_securityhub.types.cspm_connector_summary_list.serialize_json(
                value["connectors"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListConnectorsResponse:
    out: ListConnectorsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Connectors") is not None:
        import capo_securityhub.types.cspm_connector_summary_list

        out["connectors"] = (
            capo_securityhub.types.cspm_connector_summary_list.deserialize_json(
                data["Connectors"]
            )
        )
    return out
