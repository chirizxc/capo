"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectionRuleFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detection_rule_filter_condition
    import capo_guardduty.types.detection_rule_filter_values
    import capo_guardduty.types.filter_field_name


class DetectionRuleFilter(TypedDict, closed=True):
    name: NotRequired["capo_guardduty.types.filter_field_name.FilterFieldName"]
    """<p>The name of the field to filter by.</p>"""
    values: NotRequired[
        "capo_guardduty.types.detection_rule_filter_values.DetectionRuleFilterValues"
    ]
    """<p>The values to match against the specified filter name.</p>"""
    condition: NotRequired[
        "capo_guardduty.types.detection_rule_filter_condition.DetectionRuleFilterCondition"
    ]
    """<p>The condition to apply to the filter. For example, <code>EQUALS</code> or <code>CONTAINS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectionRuleFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_guardduty.types.filter_field_name

        out["name"] = capo_guardduty.types.filter_field_name.serialize_json(
            value["name"]
        )
    if "values" in value:
        import capo_guardduty.types.detection_rule_filter_values

        out["values"] = (
            capo_guardduty.types.detection_rule_filter_values.serialize_json(
                value["values"]
            )
        )
    if "condition" in value:
        import capo_guardduty.types.detection_rule_filter_condition

        out["condition"] = (
            capo_guardduty.types.detection_rule_filter_condition.serialize_json(
                value["condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> DetectionRuleFilter:
    out: DetectionRuleFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_guardduty.types.filter_field_name

        out["name"] = capo_guardduty.types.filter_field_name.deserialize_json(
            data["name"]
        )
    if data.get("values") is not None:
        import capo_guardduty.types.detection_rule_filter_values

        out["values"] = (
            capo_guardduty.types.detection_rule_filter_values.deserialize_json(
                data["values"]
            )
        )
    if data.get("condition") is not None:
        import capo_guardduty.types.detection_rule_filter_condition

        out["condition"] = (
            capo_guardduty.types.detection_rule_filter_condition.deserialize_json(
                data["condition"]
            )
        )
    return out
