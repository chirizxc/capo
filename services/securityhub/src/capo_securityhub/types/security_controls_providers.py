"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityControlsProviders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.security_controls_provider

SecurityControlsProviders: TypeAlias = list[
    "capo_securityhub.types.security_controls_provider.SecurityControlsProvider"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityControlsProviders) -> list:
    import capo_securityhub.types.security_controls_provider

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.security_controls_provider.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SecurityControlsProviders:
    import capo_securityhub.types.security_controls_provider

    out: SecurityControlsProviders = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityhub.types.security_controls_provider.deserialize_json(item)
        )
    return out
