"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ControlAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.control_assessment_result
    import capo_marketplace_catalog.types.control_error_list
    import capo_marketplace_catalog.types.resource_id


class ControlAssessment(TypedDict, closed=True):
    control_id: NotRequired["capo_marketplace_catalog.types.resource_id.ResourceId"]
    """<p>The unique ID of the control that was evaluated.</p>"""
    control_assessment_result: NotRequired[
        "capo_marketplace_catalog.types.control_assessment_result.ControlAssessmentResult"
    ]
    """<p>The result of the control evaluation.</p>"""
    errors: NotRequired[
        "capo_marketplace_catalog.types.control_error_list.ControlErrorList"
    ]
    """<p>An array of <code>ControlError</code> objects associated with the control evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlAssessment) -> dict:
    out: dict = {}
    if "control_id" in value:
        out["ControlId"] = value["control_id"]
    if "control_assessment_result" in value:
        import capo_marketplace_catalog.types.control_assessment_result

        out["ControlAssessmentResult"] = (
            capo_marketplace_catalog.types.control_assessment_result.serialize_json(
                value["control_assessment_result"]
            )
        )
    if "errors" in value:
        import capo_marketplace_catalog.types.control_error_list

        out["Errors"] = (
            capo_marketplace_catalog.types.control_error_list.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> ControlAssessment:
    out: ControlAssessment = {}  # type: ignore[typeddict-item]
    if data.get("ControlId") is not None:
        out["control_id"] = data["ControlId"]
    if data.get("ControlAssessmentResult") is not None:
        import capo_marketplace_catalog.types.control_assessment_result

        out["control_assessment_result"] = (
            capo_marketplace_catalog.types.control_assessment_result.deserialize_json(
                data["ControlAssessmentResult"]
            )
        )
    if data.get("Errors") is not None:
        import capo_marketplace_catalog.types.control_error_list

        out["errors"] = (
            capo_marketplace_catalog.types.control_error_list.deserialize_json(
                data["Errors"]
            )
        )
    return out
