"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTableInheritedConstraints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.inherited_additional_analyses
    import capo_cleanrooms.types.inherited_allowed_additional_analyses
    import capo_cleanrooms.types.inherited_allowed_result_receivers
    import capo_cleanrooms.types.inherited_disallowed_output_columns


class IntermediateTableInheritedConstraints(TypedDict, closed=True):
    additional_analyses: NotRequired[
        "capo_cleanrooms.types.inherited_additional_analyses.InheritedAdditionalAnalyses"
    ]
    """<p>The inherited additional analyses constraint.</p>"""
    allowed_additional_analyses: NotRequired[
        "capo_cleanrooms.types.inherited_allowed_additional_analyses.InheritedAllowedAdditionalAnalyses"
    ]
    """<p>The inherited allowed additional analyses constraint.</p>"""
    allowed_result_receivers: NotRequired[
        "capo_cleanrooms.types.inherited_allowed_result_receivers.InheritedAllowedResultReceivers"
    ]
    """<p>The inherited allowed result receivers constraint.</p>"""
    disallowed_output_columns: NotRequired[
        "capo_cleanrooms.types.inherited_disallowed_output_columns.InheritedDisallowedOutputColumns"
    ]
    """<p>The inherited disallowed output columns constraint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTableInheritedConstraints) -> dict:
    out: dict = {}
    if "additional_analyses" in value:
        import capo_cleanrooms.types.inherited_additional_analyses

        out["additionalAnalyses"] = (
            capo_cleanrooms.types.inherited_additional_analyses.serialize_json(
                value["additional_analyses"]
            )
        )
    if "allowed_additional_analyses" in value:
        import capo_cleanrooms.types.inherited_allowed_additional_analyses

        out["allowedAdditionalAnalyses"] = (
            capo_cleanrooms.types.inherited_allowed_additional_analyses.serialize_json(
                value["allowed_additional_analyses"]
            )
        )
    if "allowed_result_receivers" in value:
        import capo_cleanrooms.types.inherited_allowed_result_receivers

        out["allowedResultReceivers"] = (
            capo_cleanrooms.types.inherited_allowed_result_receivers.serialize_json(
                value["allowed_result_receivers"]
            )
        )
    if "disallowed_output_columns" in value:
        import capo_cleanrooms.types.inherited_disallowed_output_columns

        out["disallowedOutputColumns"] = (
            capo_cleanrooms.types.inherited_disallowed_output_columns.serialize_json(
                value["disallowed_output_columns"]
            )
        )
    return out


def deserialize_json(data: dict) -> IntermediateTableInheritedConstraints:
    out: IntermediateTableInheritedConstraints = {}  # type: ignore[typeddict-item]
    if data.get("additionalAnalyses") is not None:
        import capo_cleanrooms.types.inherited_additional_analyses

        out["additional_analyses"] = (
            capo_cleanrooms.types.inherited_additional_analyses.deserialize_json(
                data["additionalAnalyses"]
            )
        )
    if data.get("allowedAdditionalAnalyses") is not None:
        import capo_cleanrooms.types.inherited_allowed_additional_analyses

        out["allowed_additional_analyses"] = (
            capo_cleanrooms.types.inherited_allowed_additional_analyses.deserialize_json(
                data["allowedAdditionalAnalyses"]
            )
        )
    if data.get("allowedResultReceivers") is not None:
        import capo_cleanrooms.types.inherited_allowed_result_receivers

        out["allowed_result_receivers"] = (
            capo_cleanrooms.types.inherited_allowed_result_receivers.deserialize_json(
                data["allowedResultReceivers"]
            )
        )
    if data.get("disallowedOutputColumns") is not None:
        import capo_cleanrooms.types.inherited_disallowed_output_columns

        out["disallowed_output_columns"] = (
            capo_cleanrooms.types.inherited_disallowed_output_columns.deserialize_json(
                data["disallowedOutputColumns"]
            )
        )
    return out
