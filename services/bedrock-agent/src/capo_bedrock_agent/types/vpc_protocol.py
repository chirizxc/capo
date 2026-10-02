"""Generated from Smithy shape ``com.amazonaws.bedrockagent#VpcProtocol``."""

from typing import Literal, TypeAlias, cast

"""<p>The protocol used to connect to the resource. Valid values:</p> <ul> <li> <p> <code>HTTP</code> – Connect over plaintext HTTP.</p> </li> <li> <p> <code>HTTPS</code> – Connect over TLS.</p> </li> </ul>"""
VpcProtocol: TypeAlias = Literal[
    "HTTP",
    "HTTPS",
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcProtocol) -> str:
    return value


def deserialize_json(data: str) -> VpcProtocol:
    return cast(VpcProtocol, data)
