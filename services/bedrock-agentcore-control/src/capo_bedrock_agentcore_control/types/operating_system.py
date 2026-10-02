"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OperatingSystem``."""

from typing import Literal, TypeAlias, cast

"""<p>The operating system and CPU architecture for capacity provider instances.</p>"""
OperatingSystem: TypeAlias = Literal[
    "LINUX_X86_64",
    "LINUX_ARM64",
]


# --- restJson1 ser/de ---
def serialize_json(value: OperatingSystem) -> str:
    return value


def deserialize_json(data: str) -> OperatingSystem:
    return cast(OperatingSystem, data)
