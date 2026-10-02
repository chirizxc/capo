"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#PacingStrategyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.pacing_strategy

PacingStrategyList: TypeAlias = list[
    "capo_connectcampaignsv2.types.pacing_strategy.PacingStrategy"
]


# --- restJson1 ser/de ---
def serialize_json(value: PacingStrategyList) -> list:
    import capo_connectcampaignsv2.types.pacing_strategy

    out: list = []
    for item in value:
        out.append(capo_connectcampaignsv2.types.pacing_strategy.serialize_json(item))
    return out


def deserialize_json(data: list) -> PacingStrategyList:
    import capo_connectcampaignsv2.types.pacing_strategy

    out: PacingStrategyList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connectcampaignsv2.types.pacing_strategy.deserialize_json(item))
    return out
