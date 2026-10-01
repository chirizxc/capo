"""Generated from Smithy shape ``com.amazonaws.pcs#ExecutionPolicy``."""

from typing import Literal, TypeAlias, cast

"""<p>The policy that determines when a node lifecycle script runs. Valid values:</p> <ul> <li> <p> <code>FIRST_BOOT_ONLY</code> – Runs the script only the first time the compute node boots.</p> </li> <li> <p> <code>EVERY_BOOT</code> – Runs the script every time the compute node boots, including reboots.</p> </li> </ul>"""
ExecutionPolicy: TypeAlias = Literal[
    "FIRST_BOOT_ONLY",
    "EVERY_BOOT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionPolicy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExecutionPolicy:
    return cast(ExecutionPolicy, data)
