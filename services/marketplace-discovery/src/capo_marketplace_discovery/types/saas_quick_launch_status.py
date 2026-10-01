"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SaasQuickLaunchStatus``."""

from typing import Literal, TypeAlias, cast

SaasQuickLaunchStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SaasQuickLaunchStatus) -> str:
    return value


def deserialize_json(data: str) -> SaasQuickLaunchStatus:
    return cast(SaasQuickLaunchStatus, data)
