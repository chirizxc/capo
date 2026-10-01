"""Generated from Smithy shape ``com.amazonaws.connect#MetricSearchCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.boolean_condition
    import capo_connect.types.metric_search_condition_list
    import capo_connect.types.string_condition


class MetricSearchCriteria(TypedDict, closed=True):
    or_conditions: NotRequired[
        "capo_connect.types.metric_search_condition_list.MetricSearchConditionList"
    ]
    """<p>A list of conditions to be met, where at least one condition must be satisfied.</p>"""
    and_conditions: NotRequired[
        "capo_connect.types.metric_search_condition_list.MetricSearchConditionList"
    ]
    """<p>A list of conditions that must all be satisfied.</p>"""
    string_condition: NotRequired["capo_connect.types.string_condition.StringCondition"]
    boolean_condition: NotRequired[
        "capo_connect.types.boolean_condition.BooleanCondition"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MetricSearchCriteria) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import capo_connect.types.metric_search_condition_list

        out["OrConditions"] = (
            capo_connect.types.metric_search_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_conditions" in value:
        import capo_connect.types.metric_search_condition_list

        out["AndConditions"] = (
            capo_connect.types.metric_search_condition_list.serialize_json(
                value["and_conditions"]
            )
        )
    if "string_condition" in value:
        import capo_connect.types.string_condition

        out["StringCondition"] = capo_connect.types.string_condition.serialize_json(
            value["string_condition"]
        )
    if "boolean_condition" in value:
        import capo_connect.types.boolean_condition

        out["BooleanCondition"] = capo_connect.types.boolean_condition.serialize_json(
            value["boolean_condition"]
        )
    return out


def deserialize_json(data: dict) -> MetricSearchCriteria:
    out: MetricSearchCriteria = {}  # type: ignore[typeddict-item]
    if data.get("OrConditions") is not None:
        import capo_connect.types.metric_search_condition_list

        out["or_conditions"] = (
            capo_connect.types.metric_search_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if data.get("AndConditions") is not None:
        import capo_connect.types.metric_search_condition_list

        out["and_conditions"] = (
            capo_connect.types.metric_search_condition_list.deserialize_json(
                data["AndConditions"]
            )
        )
    if data.get("StringCondition") is not None:
        import capo_connect.types.string_condition

        out["string_condition"] = capo_connect.types.string_condition.deserialize_json(
            data["StringCondition"]
        )
    if data.get("BooleanCondition") is not None:
        import capo_connect.types.boolean_condition

        out["boolean_condition"] = (
            capo_connect.types.boolean_condition.deserialize_json(
                data["BooleanCondition"]
            )
        )
    return out
