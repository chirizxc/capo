"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationSortCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.investigation_sort_field
    import capo_guardduty.types.order_by


class InvestigationSortCriteria(TypedDict, closed=True):
    attribute_name: NotRequired[
        "capo_guardduty.types.investigation_sort_field.InvestigationSortField"
    ]
    """<p>The attribute by which to sort investigations.</p>"""
    order_by: NotRequired["capo_guardduty.types.order_by.OrderBy"]
    """<p>The order in which the sorted results are to be displayed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationSortCriteria) -> dict:
    out: dict = {}
    if "attribute_name" in value:
        import capo_guardduty.types.investigation_sort_field

        out["attributeName"] = (
            capo_guardduty.types.investigation_sort_field.serialize_json(
                value["attribute_name"]
            )
        )
    if "order_by" in value:
        import capo_guardduty.types.order_by

        out["orderBy"] = capo_guardduty.types.order_by.serialize_json(value["order_by"])
    return out


def deserialize_json(data: dict) -> InvestigationSortCriteria:
    out: InvestigationSortCriteria = {}  # type: ignore[typeddict-item]
    if data.get("attributeName") is not None:
        import capo_guardduty.types.investigation_sort_field

        out["attribute_name"] = (
            capo_guardduty.types.investigation_sort_field.deserialize_json(
                data["attributeName"]
            )
        )
    if data.get("orderBy") is not None:
        import capo_guardduty.types.order_by

        out["order_by"] = capo_guardduty.types.order_by.deserialize_json(
            data["orderBy"]
        )
    return out
