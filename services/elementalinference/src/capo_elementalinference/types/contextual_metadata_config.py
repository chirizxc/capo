"""Generated from Smithy shape ``com.amazonaws.elementalinference#ContextualMetadataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.summary_generation_mode


class ContextualMetadataConfig(TypedDict, closed=True):
    summary_generation: NotRequired[
        "capo_elementalinference.types.summary_generation_mode.SummaryGenerationMode"
    ]
    """<p>Specifies whether Elemental Inference generates a descriptive summary of the media content for this output. </p> <p>Valid values:</p> <ul> <li> <p>ENABLED (default) – Elemental Inference generates a descriptive summary along with IAB taxonomy and GARM suitability classifications. </p> </li> <li> <p>DISABLED – No descriptive summary is generated.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContextualMetadataConfig) -> dict:
    out: dict = {}
    if "summary_generation" in value:
        import capo_elementalinference.types.summary_generation_mode

        out["summaryGeneration"] = (
            capo_elementalinference.types.summary_generation_mode.serialize_json(
                value["summary_generation"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContextualMetadataConfig:
    out: ContextualMetadataConfig = {}  # type: ignore[typeddict-item]
    if data.get("summaryGeneration") is not None:
        import capo_elementalinference.types.summary_generation_mode

        out["summary_generation"] = (
            capo_elementalinference.types.summary_generation_mode.deserialize_json(
                data["summaryGeneration"]
            )
        )
    return out
