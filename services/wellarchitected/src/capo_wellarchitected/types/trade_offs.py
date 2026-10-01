"""Generated from Smithy shape ``com.amazonaws.wellarchitected#TradeOffs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.trade_off

TradeOffs: TypeAlias = list["capo_wellarchitected.types.trade_off.TradeOff"]


# --- restJson1 ser/de ---
def serialize_json(value: TradeOffs) -> list:
    import capo_wellarchitected.types.trade_off

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.trade_off.serialize_json(item))
    return out


def deserialize_json(data: list) -> TradeOffs:
    import capo_wellarchitected.types.trade_off

    out: TradeOffs = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wellarchitected.types.trade_off.deserialize_json(item))
    return out
