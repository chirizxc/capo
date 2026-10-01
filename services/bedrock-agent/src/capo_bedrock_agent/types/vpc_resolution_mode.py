"""Generated from Smithy shape ``com.amazonaws.bedrockagent#VpcResolutionMode``."""

from typing import Literal, TypeAlias, cast

"""<p>Controls how a domain-name resource target is resolved. This applies only when the target is a domain name; it has no effect for IP-address targets. In all cases the resolved address must be reachable from inside the VPC. Valid values:</p> <ul> <li> <p> <code>IN_VPC</code> (default, recommended) – The target domain name is resolved privately, using the DNS resolvers of the VPC.</p> </li> <li> <p> <code>PUBLIC</code> – The target domain name is resolved against public DNS resolvers, for the uncommon case where the name must resolve through public DNS but the resulting address remains reachable from the VPC.</p> </li> </ul>"""
VpcResolutionMode: TypeAlias = Literal[
    "PUBLIC",
    "IN_VPC",
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcResolutionMode) -> str:
    return value


def deserialize_json(data: str) -> VpcResolutionMode:
    return cast(VpcResolutionMode, data)
