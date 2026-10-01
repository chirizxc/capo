"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationSearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_evaluation_attribute_filter
    import capo_connect.types.control_plane_attribute_filter


class EvaluationSearchFilter(TypedDict, closed=True):
    attribute_filter: NotRequired[
        "capo_connect.types.control_plane_attribute_filter.ControlPlaneAttributeFilter"
    ]
    """<p>An object that can be used to specify tag conditions.</p>"""
    contact_evaluation_attribute_filter: NotRequired[
        "capo_connect.types.contact_evaluation_attribute_filter.ContactEvaluationAttributeFilter"
    ]
    """<p>An object that can be used to specify tag conditions and attribute conditions for contact evaluations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationSearchFilter) -> dict:
    out: dict = {}
    if "attribute_filter" in value:
        import capo_connect.types.control_plane_attribute_filter

        out["AttributeFilter"] = (
            capo_connect.types.control_plane_attribute_filter.serialize_json(
                value["attribute_filter"]
            )
        )
    if "contact_evaluation_attribute_filter" in value:
        import capo_connect.types.contact_evaluation_attribute_filter

        out["ContactEvaluationAttributeFilter"] = (
            capo_connect.types.contact_evaluation_attribute_filter.serialize_json(
                value["contact_evaluation_attribute_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationSearchFilter:
    out: EvaluationSearchFilter = {}  # type: ignore[typeddict-item]
    if data.get("AttributeFilter") is not None:
        import capo_connect.types.control_plane_attribute_filter

        out["attribute_filter"] = (
            capo_connect.types.control_plane_attribute_filter.deserialize_json(
                data["AttributeFilter"]
            )
        )
    if data.get("ContactEvaluationAttributeFilter") is not None:
        import capo_connect.types.contact_evaluation_attribute_filter

        out["contact_evaluation_attribute_filter"] = (
            capo_connect.types.contact_evaluation_attribute_filter.deserialize_json(
                data["ContactEvaluationAttributeFilter"]
            )
        )
    return out
