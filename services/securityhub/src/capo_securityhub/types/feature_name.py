"""Generated from Smithy shape ``com.amazonaws.securityhub#FeatureName``."""

from typing import Literal, TypeAlias, cast

"""<p>The name of an opt-in feature. Valid values: <code>NETWORK_SCANNING</code>.</p>"""
FeatureName: TypeAlias = Literal["NETWORK_SCANNING",]


# --- restJson1 ser/de ---
def serialize_json(value: FeatureName) -> str:
    return value


def deserialize_json(data: str) -> FeatureName:
    return cast(FeatureName, data)
