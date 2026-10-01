"""Generated from Smithy shape ``com.amazonaws.quicksight#KnowledgeBaseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.kb_template_configuration


class KnowledgeBaseConfiguration(TypedDict, closed=True):
    template_configuration: NotRequired[
        "capo_quicksight.types.kb_template_configuration.KbTemplateConfiguration"
    ]
    """<p>The template configuration that defines how the data source connector crawls and indexes data for the knowledge base. The template structure varies by connector type. See <code>KbTemplateConfiguration</code> for connector-specific details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseConfiguration) -> dict:
    out: dict = {}
    if "template_configuration" in value:
        import capo_quicksight.types.kb_template_configuration

        out["templateConfiguration"] = (
            capo_quicksight.types.kb_template_configuration.serialize_json(
                value["template_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseConfiguration:
    out: KnowledgeBaseConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("templateConfiguration") is not None:
        import capo_quicksight.types.kb_template_configuration

        out["template_configuration"] = (
            capo_quicksight.types.kb_template_configuration.deserialize_json(
                data["templateConfiguration"]
            )
        )
    return out
