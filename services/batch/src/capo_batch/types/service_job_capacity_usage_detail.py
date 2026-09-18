"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobCapacityUsageDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.double
    import capo_batch.types.string


class ServiceJobCapacityUsageDetail(TypedDict, closed=True):
    capacity_unit: NotRequired["capo_batch.types.string.String"]
    """<p>The unit of measure for the service job capacity usage. For service jobs, this is the instance type.</p>"""
    quantity: NotRequired["capo_batch.types.double.Double"]
    """<p>The quantity of capacity being used by the service job, measured in the units specified by <code>capacityUnit</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceJobCapacityUsageDetail) -> dict:
    out: dict = {}
    if "capacity_unit" in value:
        out["capacityUnit"] = value["capacity_unit"]
    if "quantity" in value:
        out["quantity"] = (
            "NaN"
            if value["quantity"] != value["quantity"]
            else "Infinity"
            if value["quantity"] == float("inf")
            else "-Infinity"
            if value["quantity"] == float("-inf")
            else value["quantity"]
        )
    return out


def deserialize_json(data: dict) -> ServiceJobCapacityUsageDetail:
    out: ServiceJobCapacityUsageDetail = {}  # type: ignore[typeddict-item]
    if data.get("capacityUnit") is not None:
        out["capacity_unit"] = data["capacityUnit"]
    if data.get("quantity") is not None:
        out["quantity"] = float(data["quantity"])
    return out
