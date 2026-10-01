"""Generated from Smithy shape ``com.amazonaws.autoscaling#DistributionSegment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.target_capacity_types


class DistributionSegment(TypedDict, closed=True):
    target_capacity_types: NotRequired[
        "capo_auto_scaling.types.target_capacity_types.TargetCapacityTypes"
    ]
    """<p>The capacity types to prioritize, in order. Amazon EC2 Auto Scaling attempts to launch instances in the priority order of the capacity types, and within each capacity type, in the order of instance types listed in your launch template <code>Overrides</code>.</p> <p>The following lists the valid values:</p> <dl> <dt>on-demand-capacity-reservation</dt> <dd> <p>On-Demand Capacity Reservations.</p> </dd> <dt>capacity-block</dt> <dd> <p>Capacity Blocks.</p> </dd> <dt>interruptible-capacity-reservation</dt> <dd> <p>Interruptible Capacity Reservations.</p> </dd> <dt>on-demand</dt> <dd> <p>On-Demand capacity. Include this value to allow the group to fall back to On-Demand capacity when the preceding capacity types are unavailable.</p> </dd> </dl>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DistributionSegment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "target_capacity_types" in value:
        import capo_auto_scaling.types.target_capacity_types

        capo_auto_scaling.types.target_capacity_types.serialize_query(
            value["target_capacity_types"], pairs, f"{key_prefix}TargetCapacityTypes"
        )


def deserialize_query(el: Element) -> DistributionSegment:
    out: DistributionSegment = {}  # type: ignore[typeddict-item]
    child_target_capacity_types = el.find("TargetCapacityTypes")
    if child_target_capacity_types is not None:
        import capo_auto_scaling.types.target_capacity_types

        out["target_capacity_types"] = (
            capo_auto_scaling.types.target_capacity_types.deserialize_query(
                child_target_capacity_types
            )
        )
    return out
