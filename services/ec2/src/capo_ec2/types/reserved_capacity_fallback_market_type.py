"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedCapacityFallbackMarketType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ReservedCapacityFallbackMarketType: TypeAlias = Literal["on-demand",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ReservedCapacityFallbackMarketType) -> str:
    return value


def from_ec2_query_text(text: str) -> ReservedCapacityFallbackMarketType:
    return cast(ReservedCapacityFallbackMarketType, text)


def serialize_ec2_query(
    value: ReservedCapacityFallbackMarketType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ReservedCapacityFallbackMarketType:
    return from_ec2_query_text(el.text or "")
