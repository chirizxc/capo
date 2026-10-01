"""Generated from Smithy shape ``com.amazonaws.connect#PreEvaluationFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.pre_evaluation_filter_list


class PreEvaluationFilters(TypedDict, closed=True):
    and_conditions: NotRequired[
        "capo_connect.types.pre_evaluation_filter_list.PreEvaluationFilterList"
    ]
    """<p>A list of conditions that the rule evaluates together using AND logic. All conditions must be met for the event to be evaluated by the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PreEvaluationFilters) -> dict:
    out: dict = {}
    if "and_conditions" in value:
        import capo_connect.types.pre_evaluation_filter_list

        out["AndConditions"] = (
            capo_connect.types.pre_evaluation_filter_list.serialize_json(
                value["and_conditions"]
            )
        )
    return out


def deserialize_json(data: dict) -> PreEvaluationFilters:
    out: PreEvaluationFilters = {}  # type: ignore[typeddict-item]
    if data.get("AndConditions") is not None:
        import capo_connect.types.pre_evaluation_filter_list

        out["and_conditions"] = (
            capo_connect.types.pre_evaluation_filter_list.deserialize_json(
                data["AndConditions"]
            )
        )
    return out
