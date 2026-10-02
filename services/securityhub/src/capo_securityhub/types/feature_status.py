"""Generated from Smithy shape ``com.amazonaws.securityhub#FeatureStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The enablement status of a feature. Valid values: <code>ENABLED</code> | <code>DISABLED</code>.</p>"""
FeatureStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: FeatureStatus) -> str:
    return value


def deserialize_json(data: str) -> FeatureStatus:
    return cast(FeatureStatus, data)
