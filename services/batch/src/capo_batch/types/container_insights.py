"""Generated from Smithy shape ``com.amazonaws.batch#ContainerInsights``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the CloudWatch Container Insights mode for the compute environment.</p>"""
ContainerInsights: TypeAlias = Literal[
    "ENABLED",
    "ENHANCED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContainerInsights) -> str:
    return value


def deserialize_json(data: str) -> ContainerInsights:
    return cast(ContainerInsights, data)
