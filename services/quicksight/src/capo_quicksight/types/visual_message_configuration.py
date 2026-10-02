"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualMessageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean
    import capo_quicksight.types.visibility
    import capo_quicksight.types.visual_message_link_url
    import capo_quicksight.types.visual_message_text


class VisualMessageConfiguration(TypedDict, closed=True):
    enabled: "capo_quicksight.types.boolean.Boolean"
    """<p>Specifies whether the custom message is displayed on the visual. When set to <code>true</code>, the custom message appears in place of the default message. When set to <code>false</code> or omitted, the default message is displayed.</p>"""
    title: NotRequired["capo_quicksight.types.visual_message_text.VisualMessageText"]
    """<p>The title text of the message that is displayed on the visual.</p>"""
    title_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>Specifies whether the title of the message is displayed.</p>"""
    description: NotRequired[
        "capo_quicksight.types.visual_message_text.VisualMessageText"
    ]
    """<p>The description text of the message that is displayed on the visual.</p>"""
    description_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>Specifies whether the description of the message is displayed.</p>"""
    link_text: NotRequired[
        "capo_quicksight.types.visual_message_text.VisualMessageText"
    ]
    """<p>The display text of the hyperlink that is shown in the message.</p>"""
    link_url: NotRequired[
        "capo_quicksight.types.visual_message_link_url.VisualMessageLinkUrl"
    ]
    """<p>The destination URL of the hyperlink that is shown in the message. Only valid <code>http</code>, <code>https</code>, and <code>mailto</code> URLs are supported.</p>"""
    link_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>Specifies whether the hyperlink in the message is displayed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualMessageConfiguration) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    if "title" in value:
        out["Title"] = value["title"]
    if "title_visibility" in value:
        import capo_quicksight.types.visibility

        out["TitleVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["title_visibility"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "description_visibility" in value:
        import capo_quicksight.types.visibility

        out["DescriptionVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["description_visibility"]
        )
    if "link_text" in value:
        out["LinkText"] = value["link_text"]
    if "link_url" in value:
        out["LinkUrl"] = value["link_url"]
    if "link_visibility" in value:
        import capo_quicksight.types.visibility

        out["LinkVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["link_visibility"]
        )
    return out


def deserialize_json(data: dict) -> VisualMessageConfiguration:
    out: VisualMessageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("TitleVisibility") is not None:
        import capo_quicksight.types.visibility

        out["title_visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["TitleVisibility"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DescriptionVisibility") is not None:
        import capo_quicksight.types.visibility

        out["description_visibility"] = (
            capo_quicksight.types.visibility.deserialize_json(
                data["DescriptionVisibility"]
            )
        )
    if data.get("LinkText") is not None:
        out["link_text"] = data["LinkText"]
    if data.get("LinkUrl") is not None:
        out["link_url"] = data["LinkUrl"]
    if data.get("LinkVisibility") is not None:
        import capo_quicksight.types.visibility

        out["link_visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["LinkVisibility"]
        )
    return out
