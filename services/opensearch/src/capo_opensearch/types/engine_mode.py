"""Generated from Smithy shape ``com.amazonaws.opensearch#EngineMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The engine mode for the domain. Valid values are <code>GENERAL</code> (the standard OpenSearch engine) and <code>OPTIMIZED</code>. If you don't specify an engine mode, <code>GENERAL</code> is used. <code>OPTIMIZED</code> requires OpenSearch 3.5 or later, OpenSearch Optimized instance types (OR1, OR2, OM2, or OI2) for the data tier, and is available only for the <code>OBSERVABILITY</code> use cases. The engine mode can't be changed after the domain is created.</p>"""
EngineMode: TypeAlias = Literal[
    "GENERAL",
    "OPTIMIZED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EngineMode) -> str:
    return value


def deserialize_json(data: str) -> EngineMode:
    return cast(EngineMode, data)
