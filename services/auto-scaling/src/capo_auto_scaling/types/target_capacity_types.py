"""Generated from Smithy shape ``com.amazonaws.autoscaling#TargetCapacityTypes``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.target_capacity_type

TargetCapacityTypes: TypeAlias = list[
    "capo_auto_scaling.types.target_capacity_type.TargetCapacityType"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetCapacityTypes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.target_capacity_type

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.target_capacity_type.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TargetCapacityTypes:
    import capo_auto_scaling.types.target_capacity_type

    out: TargetCapacityTypes = []
    for child in el.findall("member"):
        out.append(
            capo_auto_scaling.types.target_capacity_type.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: TargetCapacityTypes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.target_capacity_type

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.target_capacity_type.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TargetCapacityTypes:
    import capo_auto_scaling.types.target_capacity_type

    out: TargetCapacityTypes = []
    for child in parent.findall(tag):
        out.append(
            capo_auto_scaling.types.target_capacity_type.deserialize_query(child)
        )
    return out
