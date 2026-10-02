"""Generated from Smithy shape ``com.amazonaws.appconfig#ListExperimentDefinitionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.experiment_definition_status
    import capo_appconfig.types.identifier
    import capo_appconfig.types.max_results
    import capo_appconfig.types.next_token


class ListExperimentDefinitionsRequest(TypedDict, closed=True):
    application_identifier: NotRequired["capo_appconfig.types.identifier.Identifier"]
    """<p>The application ID or name to filter results.</p>"""
    configuration_profile_identifier: NotRequired[
        "capo_appconfig.types.identifier.Identifier"
    ]
    """<p>The configuration profile ID or name to filter results.</p>"""
    environment_identifier: NotRequired["capo_appconfig.types.identifier.Identifier"]
    """<p>The environment ID or name to filter results.</p>"""
    status: NotRequired[
        "capo_appconfig.types.experiment_definition_status.ExperimentDefinitionStatus"
    ]
    """<p>A filter for the experiment definition status.</p>"""
    max_results: NotRequired["capo_appconfig.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call.</p>"""
    next_token: NotRequired["capo_appconfig.types.next_token.NextToken"]
    """<p>A token to start the list from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExperimentDefinitionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListExperimentDefinitionsRequest:
    out: ListExperimentDefinitionsRequest = {}  # type: ignore[typeddict-item]
    return out
