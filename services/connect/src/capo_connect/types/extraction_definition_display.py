"""Generated from Smithy shape ``com.amazonaws.connect#ExtractionDefinitionDisplay``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.extraction_definition_display_label


class ExtractionDefinitionDisplay(TypedDict, closed=True):
    label: NotRequired[
        "capo_connect.types.extraction_definition_display_label.ExtractionDefinitionDisplayLabel"
    ]
    """<p>The label displayed in the agent workspace for this extraction definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionDefinitionDisplay) -> dict:
    out: dict = {}
    if "label" in value:
        out["Label"] = value["label"]
    return out


def deserialize_json(data: dict) -> ExtractionDefinitionDisplay:
    out: ExtractionDefinitionDisplay = {}  # type: ignore[typeddict-item]
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    return out
