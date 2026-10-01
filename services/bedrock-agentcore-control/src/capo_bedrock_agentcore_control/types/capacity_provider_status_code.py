"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CapacityProviderStatusCode``."""

from typing import Literal, TypeAlias, cast

"""<p>A reason code for a capacity provider that is not in the <code>READY</code> state. Possible values:</p> <ul> <li> <p> <code>VALIDATION_ERROR</code> – A configuration error prevented the operation. For example, missing permissions, invalid parameters, or a naming conflict.</p> </li> <li> <p> <code>QUOTA_EXCEEDED</code> – An Amazon EC2 resource quota was exceeded. Request a limit increase or remove unused resources.</p> </li> <li> <p> <code>THROTTLED</code> – The request was throttled. Retry after a short delay.</p> </li> <li> <p> <code>INTERNAL_SERVER_EXCEPTION</code> – An internal error occurred.</p> </li> </ul>"""
CapacityProviderStatusCode: TypeAlias = Literal[
    "VALIDATION_ERROR",
    "QUOTA_EXCEEDED",
    "THROTTLED",
    "INTERNAL_SERVER_EXCEPTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderStatusCode) -> str:
    return value


def deserialize_json(data: str) -> CapacityProviderStatusCode:
    return cast(CapacityProviderStatusCode, data)
