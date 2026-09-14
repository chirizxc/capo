"""Generated from Smithy shape ``com.amazonaws.sesv2#TopicFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.topic_name
    import capo_sesv2.types.use_default_if_preference_unavailable


class TopicFilter(TypedDict, closed=True):
    topic_name: NotRequired["capo_sesv2.types.topic_name.TopicName"]
    """<p>The name of a topic on which you wish to apply the filter.</p>"""
    use_default_if_preference_unavailable: "capo_sesv2.types.use_default_if_preference_unavailable.UseDefaultIfPreferenceUnavailable"
    """<p>Notes that the default subscription status should be applied to a contact because the contact has not noted their preference for subscribing to a topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicFilter) -> dict:
    out: dict = {}
    if "topic_name" in value:
        out["TopicName"] = value["topic_name"]
    out["UseDefaultIfPreferenceUnavailable"] = value.get(
        "use_default_if_preference_unavailable", False
    )
    return out


def deserialize_json(data: dict) -> TopicFilter:
    out: TopicFilter = {}  # type: ignore[typeddict-item]
    if data.get("TopicName") is not None:
        out["topic_name"] = data["TopicName"]
    if data.get("UseDefaultIfPreferenceUnavailable") is not None:
        out["use_default_if_preference_unavailable"] = data[
            "UseDefaultIfPreferenceUnavailable"
        ]
    else:
        out["use_default_if_preference_unavailable"] = False
    return out
