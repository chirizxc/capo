"""Generated from Smithy shape ``com.amazonaws.connect#ContactEvaluationAttributeCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_evaluation_attribute_comparison_type
    import capo_connect.types.contact_evaluation_attribute_key
    import capo_connect.types.contact_evaluation_attribute_value


class ContactEvaluationAttributeCondition(TypedDict, closed=True):
    attribute_key: NotRequired[
        "capo_connect.types.contact_evaluation_attribute_key.ContactEvaluationAttributeKey"
    ]
    """<p>The key of the attribute.</p>"""
    attribute_value: NotRequired[
        "capo_connect.types.contact_evaluation_attribute_value.ContactEvaluationAttributeValue"
    ]
    """<p>The value of the attribute.</p>"""
    comparison_type: NotRequired[
        "capo_connect.types.contact_evaluation_attribute_comparison_type.ContactEvaluationAttributeComparisonType"
    ]
    """<p>The comparison type for the condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactEvaluationAttributeCondition) -> dict:
    out: dict = {}
    if "attribute_key" in value:
        import capo_connect.types.contact_evaluation_attribute_key

        out["AttributeKey"] = (
            capo_connect.types.contact_evaluation_attribute_key.serialize_json(
                value["attribute_key"]
            )
        )
    if "attribute_value" in value:
        import capo_connect.types.contact_evaluation_attribute_value

        out["AttributeValue"] = (
            capo_connect.types.contact_evaluation_attribute_value.serialize_json(
                value["attribute_value"]
            )
        )
    if "comparison_type" in value:
        import capo_connect.types.contact_evaluation_attribute_comparison_type

        out["ComparisonType"] = (
            capo_connect.types.contact_evaluation_attribute_comparison_type.serialize_json(
                value["comparison_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactEvaluationAttributeCondition:
    out: ContactEvaluationAttributeCondition = {}  # type: ignore[typeddict-item]
    if data.get("AttributeKey") is not None:
        import capo_connect.types.contact_evaluation_attribute_key

        out["attribute_key"] = (
            capo_connect.types.contact_evaluation_attribute_key.deserialize_json(
                data["AttributeKey"]
            )
        )
    if data.get("AttributeValue") is not None:
        import capo_connect.types.contact_evaluation_attribute_value

        out["attribute_value"] = (
            capo_connect.types.contact_evaluation_attribute_value.deserialize_json(
                data["AttributeValue"]
            )
        )
    if data.get("ComparisonType") is not None:
        import capo_connect.types.contact_evaluation_attribute_comparison_type

        out["comparison_type"] = (
            capo_connect.types.contact_evaluation_attribute_comparison_type.deserialize_json(
                data["ComparisonType"]
            )
        )
    return out
