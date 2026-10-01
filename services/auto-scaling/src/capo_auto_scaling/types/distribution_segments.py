"""Generated from Smithy shape ``com.amazonaws.autoscaling#DistributionSegments``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.distribution_segment

DistributionSegments: TypeAlias = list[
    "capo_auto_scaling.types.distribution_segment.DistributionSegment"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DistributionSegments, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.distribution_segment

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.distribution_segment.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> DistributionSegments:
    import capo_auto_scaling.types.distribution_segment

    out: DistributionSegments = []
    for child in el.findall("member"):
        out.append(
            capo_auto_scaling.types.distribution_segment.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: DistributionSegments, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.distribution_segment

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.distribution_segment.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DistributionSegments:
    import capo_auto_scaling.types.distribution_segment

    out: DistributionSegments = []
    for child in parent.findall(tag):
        out.append(
            capo_auto_scaling.types.distribution_segment.deserialize_query(child)
        )
    return out
