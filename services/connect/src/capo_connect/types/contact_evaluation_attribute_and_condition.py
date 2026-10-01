"""Generated from Smithy shape ``com.amazonaws.connect#ContactEvaluationAttributeAndCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_evaluation_attribute_condition_list
    import capo_connect.types.tag_and_condition_list


class ContactEvaluationAttributeAndCondition(TypedDict, closed=True):
    tag_conditions: NotRequired[
        "capo_connect.types.tag_and_condition_list.TagAndConditionList"
    ]
    """<p>A list of tag conditions to apply.</p>"""
    attribute_conditions: NotRequired[
        "capo_connect.types.contact_evaluation_attribute_condition_list.ContactEvaluationAttributeConditionList"
    ]
    """<p>A list of attribute conditions to apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactEvaluationAttributeAndCondition) -> dict:
    out: dict = {}
    if "tag_conditions" in value:
        import capo_connect.types.tag_and_condition_list

        out["TagConditions"] = capo_connect.types.tag_and_condition_list.serialize_json(
            value["tag_conditions"]
        )
    if "attribute_conditions" in value:
        import capo_connect.types.contact_evaluation_attribute_condition_list

        out["AttributeConditions"] = (
            capo_connect.types.contact_evaluation_attribute_condition_list.serialize_json(
                value["attribute_conditions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactEvaluationAttributeAndCondition:
    out: ContactEvaluationAttributeAndCondition = {}  # type: ignore[typeddict-item]
    if data.get("TagConditions") is not None:
        import capo_connect.types.tag_and_condition_list

        out["tag_conditions"] = (
            capo_connect.types.tag_and_condition_list.deserialize_json(
                data["TagConditions"]
            )
        )
    if data.get("AttributeConditions") is not None:
        import capo_connect.types.contact_evaluation_attribute_condition_list

        out["attribute_conditions"] = (
            capo_connect.types.contact_evaluation_attribute_condition_list.deserialize_json(
                data["AttributeConditions"]
            )
        )
    return out
