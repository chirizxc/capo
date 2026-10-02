"""Generated from Smithy shape ``com.amazonaws.connect#RuleAttributeAndCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.tag_and_condition_list


class RuleAttributeAndCondition(TypedDict, closed=True):
    tag_conditions: NotRequired[
        "capo_connect.types.tag_and_condition_list.TagAndConditionList"
    ]
    """<p>A list of tag conditions that need to be applied with <code>AND</code> condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleAttributeAndCondition) -> dict:
    out: dict = {}
    if "tag_conditions" in value:
        import capo_connect.types.tag_and_condition_list

        out["TagConditions"] = capo_connect.types.tag_and_condition_list.serialize_json(
            value["tag_conditions"]
        )
    return out


def deserialize_json(data: dict) -> RuleAttributeAndCondition:
    out: RuleAttributeAndCondition = {}  # type: ignore[typeddict-item]
    if data.get("TagConditions") is not None:
        import capo_connect.types.tag_and_condition_list

        out["tag_conditions"] = (
            capo_connect.types.tag_and_condition_list.deserialize_json(
                data["TagConditions"]
            )
        )
    return out
