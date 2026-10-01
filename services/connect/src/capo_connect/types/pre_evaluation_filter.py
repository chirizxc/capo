"""Generated from Smithy shape ``com.amazonaws.connect#PreEvaluationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.pre_evaluation_filter_operator
    import capo_connect.types.pre_evaluation_filter_resource_type
    import capo_connect.types.pre_evaluation_filter_type
    import capo_connect.types.string


class PreEvaluationFilter(TypedDict, closed=True):
    resource_type: "capo_connect.types.pre_evaluation_filter_resource_type.PreEvaluationFilterResourceType"
    """<p>The type of resource to filter on. Valid values: <code>CONTACT</code>.</p>"""
    filter_type: "capo_connect.types.pre_evaluation_filter_type.PreEvaluationFilterType"
    """<p>The type of filter to apply. Valid values: <code>TAG</code>.</p>"""
    filter_key: "capo_connect.types.string.String"
    """<p>The key of the attribute to filter on. For tag filters, this is the tag key.</p>"""
    filter_value: "capo_connect.types.string.String"
    """<p>The value to match against. For tag filters, this is the tag value.</p>"""
    operator: (
        "capo_connect.types.pre_evaluation_filter_operator.PreEvaluationFilterOperator"
    )
    """<p>The comparison operator for the filter condition. Valid values: <code>EQUALS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PreEvaluationFilter) -> dict:
    out: dict = {}
    import capo_connect.types.pre_evaluation_filter_resource_type

    out["ResourceType"] = (
        capo_connect.types.pre_evaluation_filter_resource_type.serialize_json(
            value["resource_type"]
        )
    )
    import capo_connect.types.pre_evaluation_filter_type

    out["FilterType"] = capo_connect.types.pre_evaluation_filter_type.serialize_json(
        value["filter_type"]
    )
    out["FilterKey"] = value["filter_key"]
    out["FilterValue"] = value["filter_value"]
    import capo_connect.types.pre_evaluation_filter_operator

    out["Operator"] = capo_connect.types.pre_evaluation_filter_operator.serialize_json(
        value["operator"]
    )
    return out


def deserialize_json(data: dict) -> PreEvaluationFilter:
    out: PreEvaluationFilter = {}  # type: ignore[typeddict-item]
    if data.get("ResourceType") is not None:
        import capo_connect.types.pre_evaluation_filter_resource_type

        out["resource_type"] = (
            capo_connect.types.pre_evaluation_filter_resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    else:
        raise DeserializationError("PreEvaluationFilter.resource_type required")
    if data.get("FilterType") is not None:
        import capo_connect.types.pre_evaluation_filter_type

        out["filter_type"] = (
            capo_connect.types.pre_evaluation_filter_type.deserialize_json(
                data["FilterType"]
            )
        )
    else:
        raise DeserializationError("PreEvaluationFilter.filter_type required")
    if data.get("FilterKey") is not None:
        out["filter_key"] = data["FilterKey"]
    else:
        raise DeserializationError("PreEvaluationFilter.filter_key required")
    if data.get("FilterValue") is not None:
        out["filter_value"] = data["FilterValue"]
    else:
        raise DeserializationError("PreEvaluationFilter.filter_value required")
    if data.get("Operator") is not None:
        import capo_connect.types.pre_evaluation_filter_operator

        out["operator"] = (
            capo_connect.types.pre_evaluation_filter_operator.deserialize_json(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("PreEvaluationFilter.operator required")
    return out
