"""Generated from Smithy shape ``com.amazonaws.connect#AnalyticsModes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.analytics_mode

AnalyticsModes: TypeAlias = list["capo_connect.types.analytics_mode.AnalyticsMode"]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsModes) -> list:
    import capo_connect.types.analytics_mode

    out: list = []
    for item in value:
        out.append(capo_connect.types.analytics_mode.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnalyticsModes:
    import capo_connect.types.analytics_mode

    out: AnalyticsModes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.analytics_mode.deserialize_json(item))
    return out
