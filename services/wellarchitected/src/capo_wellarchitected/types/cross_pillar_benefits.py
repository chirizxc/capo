"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CrossPillarBenefits``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.cross_pillar_benefit

CrossPillarBenefits: TypeAlias = list[
    "capo_wellarchitected.types.cross_pillar_benefit.CrossPillarBenefit"
]


# --- restJson1 ser/de ---
def serialize_json(value: CrossPillarBenefits) -> list:
    import capo_wellarchitected.types.cross_pillar_benefit

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.cross_pillar_benefit.serialize_json(item))
    return out


def deserialize_json(data: list) -> CrossPillarBenefits:
    import capo_wellarchitected.types.cross_pillar_benefit

    out: CrossPillarBenefits = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wellarchitected.types.cross_pillar_benefit.deserialize_json(item)
        )
    return out
