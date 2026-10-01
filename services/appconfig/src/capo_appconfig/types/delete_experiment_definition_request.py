"""Generated from Smithy shape ``com.amazonaws.appconfig#DeleteExperimentDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.delete_type
    import capo_appconfig.types.identifier


class DeleteExperimentDefinitionRequest(TypedDict, closed=True):
    application_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The application ID or name.</p>"""
    experiment_definition_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The experiment definition ID or name.</p>"""
    delete_type: NotRequired["capo_appconfig.types.delete_type.DeleteType"]
    """<p>The type of deletion to perform. Valid values include archive (hide but preserve) and permanent (delete permanently).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteExperimentDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteExperimentDefinitionRequest:
    out: DeleteExperimentDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
