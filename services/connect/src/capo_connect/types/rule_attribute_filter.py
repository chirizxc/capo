"""Generated from Smithy shape ``com.amazonaws.connect#RuleAttributeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.rule_attribute_and_condition
    import capo_connect.types.rule_attribute_or_condition_list
    import capo_connect.types.tag_condition


class RuleAttributeFilter(TypedDict, closed=True):
    or_conditions: NotRequired[
        "capo_connect.types.rule_attribute_or_condition_list.RuleAttributeOrConditionList"
    ]
    """<p>A list of conditions which would be applied together with an <code>OR</code> condition.</p>"""
    and_condition: NotRequired[
        "capo_connect.types.rule_attribute_and_condition.RuleAttributeAndCondition"
    ]
    """<p>A list of conditions which would be applied together with an <code>AND</code> condition.</p>"""
    tag_condition: NotRequired["capo_connect.types.tag_condition.TagCondition"]


# --- restJson1 ser/de ---
def serialize_json(value: RuleAttributeFilter) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import capo_connect.types.rule_attribute_or_condition_list

        out["OrConditions"] = (
            capo_connect.types.rule_attribute_or_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_condition" in value:
        import capo_connect.types.rule_attribute_and_condition

        out["AndCondition"] = (
            capo_connect.types.rule_attribute_and_condition.serialize_json(
                value["and_condition"]
            )
        )
    if "tag_condition" in value:
        import capo_connect.types.tag_condition

        out["TagCondition"] = capo_connect.types.tag_condition.serialize_json(
            value["tag_condition"]
        )
    return out


def deserialize_json(data: dict) -> RuleAttributeFilter:
    out: RuleAttributeFilter = {}  # type: ignore[typeddict-item]
    if data.get("OrConditions") is not None:
        import capo_connect.types.rule_attribute_or_condition_list

        out["or_conditions"] = (
            capo_connect.types.rule_attribute_or_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if data.get("AndCondition") is not None:
        import capo_connect.types.rule_attribute_and_condition

        out["and_condition"] = (
            capo_connect.types.rule_attribute_and_condition.deserialize_json(
                data["AndCondition"]
            )
        )
    if data.get("TagCondition") is not None:
        import capo_connect.types.tag_condition

        out["tag_condition"] = capo_connect.types.tag_condition.deserialize_json(
            data["TagCondition"]
        )
    return out
