"""Generated from Smithy shape ``com.amazonaws.guardduty#Observations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.observation_numbers
    import capo_guardduty.types.observation_texts


class Observations(TypedDict, closed=True):
    text: NotRequired["capo_guardduty.types.observation_texts.ObservationTexts"]
    """<p>The text that was unusual.</p>"""
    number: NotRequired["capo_guardduty.types.observation_numbers.ObservationNumbers"]
    """<p>The numeric values that were unusual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Observations) -> dict:
    out: dict = {}
    if "text" in value:
        import capo_guardduty.types.observation_texts

        out["text"] = capo_guardduty.types.observation_texts.serialize_json(
            value["text"]
        )
    if "number" in value:
        import capo_guardduty.types.observation_numbers

        out["number"] = capo_guardduty.types.observation_numbers.serialize_json(
            value["number"]
        )
    return out


def deserialize_json(data: dict) -> Observations:
    out: Observations = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        import capo_guardduty.types.observation_texts

        out["text"] = capo_guardduty.types.observation_texts.deserialize_json(
            data["text"]
        )
    if data.get("number") is not None:
        import capo_guardduty.types.observation_numbers

        out["number"] = capo_guardduty.types.observation_numbers.deserialize_json(
            data["number"]
        )
    return out
