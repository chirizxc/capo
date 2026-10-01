"""Generated from Smithy shape ``com.amazonaws.appconfig#GetExperimentRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.identifier
    import capo_appconfig.types.positive_integer


class GetExperimentRunRequest(TypedDict, closed=True):
    application_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The application ID or name.</p>"""
    experiment_definition_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The experiment definition ID or name.</p>"""
    run: "capo_appconfig.types.positive_integer.PositiveInteger"
    """<p>The run number to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExperimentRunRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetExperimentRunRequest:
    out: GetExperimentRunRequest = {}  # type: ignore[typeddict-item]
    return out
