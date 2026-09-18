"""Generated from Smithy shape ``com.amazonaws.pinpoint#InAppMessageBodyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.alignment


class InAppMessageBodyConfig(TypedDict, closed=True):
    alignment: NotRequired["capo_pinpoint.types.alignment.Alignment"]
    """<p>The alignment of the text. Valid values: LEFT, CENTER, RIGHT.</p>"""
    body: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>Message Body.</p>"""
    text_color: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The text color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InAppMessageBodyConfig) -> dict:
    out: dict = {}
    if "alignment" in value:
        import capo_pinpoint.types.alignment

        out["Alignment"] = capo_pinpoint.types.alignment.serialize_json(
            value["alignment"]
        )
    if "body" in value:
        out["Body"] = value["body"]
    if "text_color" in value:
        out["TextColor"] = value["text_color"]
    return out


def deserialize_json(data: dict) -> InAppMessageBodyConfig:
    out: InAppMessageBodyConfig = {}  # type: ignore[typeddict-item]
    if data.get("Alignment") is not None:
        import capo_pinpoint.types.alignment

        out["alignment"] = capo_pinpoint.types.alignment.deserialize_json(
            data["Alignment"]
        )
    if data.get("Body") is not None:
        out["body"] = data["Body"]
    if data.get("TextColor") is not None:
        out["text_color"] = data["TextColor"]
    return out
