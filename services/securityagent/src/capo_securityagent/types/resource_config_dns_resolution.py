"""Generated from Smithy shape ``com.amazonaws.securityagent#ResourceConfigDnsResolution``."""

from typing import Literal, TypeAlias, cast

"""<p>The DNS resolution mode for a resource gateway.</p>"""
ResourceConfigDnsResolution: TypeAlias = Literal[
    "PUBLIC",
    "IN_VPC",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceConfigDnsResolution) -> str:
    return value


def deserialize_json(data: str) -> ResourceConfigDnsResolution:
    return cast(ResourceConfigDnsResolution, data)
