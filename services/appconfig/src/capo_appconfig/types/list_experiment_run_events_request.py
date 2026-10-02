"""Generated from Smithy shape ``com.amazonaws.appconfig#ListExperimentRunEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.identifier
    import capo_appconfig.types.max_results
    import capo_appconfig.types.next_token
    import capo_appconfig.types.positive_integer


class ListExperimentRunEventsRequest(TypedDict, closed=True):
    application_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The application ID or name.</p>"""
    experiment_definition_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The experiment definition ID or name.</p>"""
    run: "capo_appconfig.types.positive_integer.PositiveInteger"
    """<p>The run number.</p>"""
    max_results: NotRequired["capo_appconfig.types.max_results.MaxResults"]
    """<p>The maximum number of items to return.</p>"""
    next_token: NotRequired["capo_appconfig.types.next_token.NextToken"]
    """<p>A token to start the list from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExperimentRunEventsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListExperimentRunEventsRequest:
    out: ListExperimentRunEventsRequest = {}  # type: ignore[typeddict-item]
    return out
