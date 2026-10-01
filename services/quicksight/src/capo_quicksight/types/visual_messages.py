"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualMessages``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.visual_message_configuration


class VisualMessages(TypedDict, closed=True):
    no_data_message: NotRequired[
        "capo_quicksight.types.visual_message_configuration.VisualMessageConfiguration"
    ]
    """<p>The message that is displayed on a visual when there is no data to display.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualMessages) -> dict:
    out: dict = {}
    if "no_data_message" in value:
        import capo_quicksight.types.visual_message_configuration

        out["NoDataMessage"] = (
            capo_quicksight.types.visual_message_configuration.serialize_json(
                value["no_data_message"]
            )
        )
    return out


def deserialize_json(data: dict) -> VisualMessages:
    out: VisualMessages = {}  # type: ignore[typeddict-item]
    if data.get("NoDataMessage") is not None:
        import capo_quicksight.types.visual_message_configuration

        out["no_data_message"] = (
            capo_quicksight.types.visual_message_configuration.deserialize_json(
                data["NoDataMessage"]
            )
        )
    return out
