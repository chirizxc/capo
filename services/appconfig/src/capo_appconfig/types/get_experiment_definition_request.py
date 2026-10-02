"""Generated from Smithy shape ``com.amazonaws.appconfig#GetExperimentDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.identifier


class GetExperimentDefinitionRequest(TypedDict, closed=True):
    application_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The application ID or name.</p>"""
    experiment_definition_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The experiment definition ID or name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExperimentDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetExperimentDefinitionRequest:
    out: GetExperimentDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
