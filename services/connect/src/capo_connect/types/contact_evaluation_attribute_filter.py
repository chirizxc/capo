"""Generated from Smithy shape ``com.amazonaws.connect#ContactEvaluationAttributeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_evaluation_attribute_and_condition
    import capo_connect.types.contact_evaluation_attribute_condition
    import capo_connect.types.contact_evaluation_attribute_or_condition_list
    import capo_connect.types.tag_condition


class ContactEvaluationAttributeFilter(TypedDict, closed=True):
    or_conditions: NotRequired[
        "capo_connect.types.contact_evaluation_attribute_or_condition_list.ContactEvaluationAttributeOrConditionList"
    ]
    """<p>A list of conditions which would be applied together with an <code>OR</code> condition.</p>"""
    and_condition: NotRequired[
        "capo_connect.types.contact_evaluation_attribute_and_condition.ContactEvaluationAttributeAndCondition"
    ]
    """<p>A list of conditions which would be applied together with an <code>AND</code> condition.</p>"""
    tag_condition: NotRequired["capo_connect.types.tag_condition.TagCondition"]
    """<p>A tag condition to apply.</p>"""
    contact_evaluation_attribute_condition: NotRequired[
        "capo_connect.types.contact_evaluation_attribute_condition.ContactEvaluationAttributeCondition"
    ]
    """<p>An attribute condition to apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactEvaluationAttributeFilter) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import capo_connect.types.contact_evaluation_attribute_or_condition_list

        out["OrConditions"] = (
            capo_connect.types.contact_evaluation_attribute_or_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_condition" in value:
        import capo_connect.types.contact_evaluation_attribute_and_condition

        out["AndCondition"] = (
            capo_connect.types.contact_evaluation_attribute_and_condition.serialize_json(
                value["and_condition"]
            )
        )
    if "tag_condition" in value:
        import capo_connect.types.tag_condition

        out["TagCondition"] = capo_connect.types.tag_condition.serialize_json(
            value["tag_condition"]
        )
    if "contact_evaluation_attribute_condition" in value:
        import capo_connect.types.contact_evaluation_attribute_condition

        out["ContactEvaluationAttributeCondition"] = (
            capo_connect.types.contact_evaluation_attribute_condition.serialize_json(
                value["contact_evaluation_attribute_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactEvaluationAttributeFilter:
    out: ContactEvaluationAttributeFilter = {}  # type: ignore[typeddict-item]
    if data.get("OrConditions") is not None:
        import capo_connect.types.contact_evaluation_attribute_or_condition_list

        out["or_conditions"] = (
            capo_connect.types.contact_evaluation_attribute_or_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if data.get("AndCondition") is not None:
        import capo_connect.types.contact_evaluation_attribute_and_condition

        out["and_condition"] = (
            capo_connect.types.contact_evaluation_attribute_and_condition.deserialize_json(
                data["AndCondition"]
            )
        )
    if data.get("TagCondition") is not None:
        import capo_connect.types.tag_condition

        out["tag_condition"] = capo_connect.types.tag_condition.deserialize_json(
            data["TagCondition"]
        )
    if data.get("ContactEvaluationAttributeCondition") is not None:
        import capo_connect.types.contact_evaluation_attribute_condition

        out["contact_evaluation_attribute_condition"] = (
            capo_connect.types.contact_evaluation_attribute_condition.deserialize_json(
                data["ContactEvaluationAttributeCondition"]
            )
        )
    return out
