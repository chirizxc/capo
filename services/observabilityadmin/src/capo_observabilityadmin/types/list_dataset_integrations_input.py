"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListDatasetIntegrationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.list_dataset_integrations_max_results
    import capo_observabilityadmin.types.next_token


class ListDatasetIntegrationsInput(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_observabilityadmin.types.list_dataset_integrations_max_results.ListDatasetIntegrationsMaxResults"
    ]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_observabilityadmin.types.next_token.NextToken"]
    """<p>The token for the next set of results. A previous call generates this token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetIntegrationsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatasetIntegrationsInput:
    out: ListDatasetIntegrationsInput = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
