"""Generated from Smithy shape ``com.amazonaws.autoscaling#TargetCapacityType``."""

from typing import Literal, TypeAlias, cast

from capo_auto_scaling._protocol.xml import Element

TargetCapacityType: TypeAlias = Literal[
    "on-demand-capacity-reservation",
    "capacity-block",
    "interruptible-capacity-reservation",
    "on-demand",
]


# --- awsQuery ser/de ---
def to_query_text(value: TargetCapacityType) -> str:
    return value


def from_query_text(text: str) -> TargetCapacityType:
    return cast(TargetCapacityType, text)


def serialize_query(
    value: TargetCapacityType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TargetCapacityType:
    return from_query_text(el.text or "")
