"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StaticQueryParameterConflictResolution``."""

from typing import Literal, TypeAlias, cast

"""<p>The precedence used when a client-supplied query parameter has the same name as a configured static query parameter:</p> <ul> <li> <p> <code>CLIENT_OVERRIDE</code> - The client-supplied value overrides the configured static value for that parameter name. This is the default.</p> </li> <li> <p> <code>STATIC_OVERRIDE</code> - The configured static value is retained, overriding the client-supplied value for that parameter name.</p> </li> </ul>"""
StaticQueryParameterConflictResolution: TypeAlias = Literal[
    "CLIENT_OVERRIDE",
    "STATIC_OVERRIDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: StaticQueryParameterConflictResolution) -> str:
    return value


def deserialize_json(data: str) -> StaticQueryParameterConflictResolution:
    return cast(StaticQueryParameterConflictResolution, data)
