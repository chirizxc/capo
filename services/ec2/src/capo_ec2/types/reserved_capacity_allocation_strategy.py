"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedCapacityAllocationStrategy``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ReservedCapacityAllocationStrategy: TypeAlias = Literal["prioritized",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ReservedCapacityAllocationStrategy) -> str:
    return value


def from_ec2_query_text(text: str) -> ReservedCapacityAllocationStrategy:
    return cast(ReservedCapacityAllocationStrategy, text)


def serialize_ec2_query(
    value: ReservedCapacityAllocationStrategy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ReservedCapacityAllocationStrategy:
    return from_ec2_query_text(el.text or "")
