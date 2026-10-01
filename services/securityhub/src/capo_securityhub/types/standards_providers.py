"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsProviders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.standards_provider

StandardsProviders: TypeAlias = list[
    "capo_securityhub.types.standards_provider.StandardsProvider"
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardsProviders) -> list:
    import capo_securityhub.types.standards_provider

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.standards_provider.serialize_json(item))
    return out


def deserialize_json(data: list) -> StandardsProviders:
    import capo_securityhub.types.standards_provider

    out: StandardsProviders = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityhub.types.standards_provider.deserialize_json(item))
    return out
