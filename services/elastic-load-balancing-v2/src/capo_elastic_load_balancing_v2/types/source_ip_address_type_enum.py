"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#SourceIpAddressTypeEnum``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_load_balancing_v2._protocol.xml import Element

SourceIpAddressTypeEnum: TypeAlias = Literal[
    "ipv4",
    "ipv6",
]


# --- awsQuery ser/de ---
def to_query_text(value: SourceIpAddressTypeEnum) -> str:
    return value


def from_query_text(text: str) -> SourceIpAddressTypeEnum:
    return cast(SourceIpAddressTypeEnum, text)


def serialize_query(
    value: SourceIpAddressTypeEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> SourceIpAddressTypeEnum:
    return from_query_text(el.text or "")
