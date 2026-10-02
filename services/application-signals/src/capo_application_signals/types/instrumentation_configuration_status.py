"""Generated from Smithy shape ``com.amazonaws.applicationsignals#InstrumentationConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of an instrumentation configuration on a host.</p> <ul> <li> <p> <code>READY</code> - The configuration has been applied but has not been hit yet.</p> </li> <li> <p> <code>ERROR</code> - Applying the configuration failed; see the error cause.</p> </li> <li> <p> <code>ACTIVE</code> - The configuration has been hit and is capturing data.</p> </li> <li> <p> <code>DISABLED</code> - The configuration was disabled, for example because a limit was reached.</p> </li> </ul>"""
InstrumentationConfigurationStatus: TypeAlias = Literal[
    "READY",
    "ERROR",
    "ACTIVE",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InstrumentationConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> InstrumentationConfigurationStatus:
    return cast(InstrumentationConfigurationStatus, data)
