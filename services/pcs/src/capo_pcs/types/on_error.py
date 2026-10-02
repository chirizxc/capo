"""Generated from Smithy shape ``com.amazonaws.pcs#OnError``."""

from typing import Literal, TypeAlias, cast

"""<p>The behavior when a node lifecycle script fails. Valid values:</p> <ul> <li> <p> <code>TERMINATE</code> – Terminates the compute node.</p> </li> <li> <p> <code>STOP_SEQUENCE</code> – Stops running subsequent scripts in the sequence but doesn't terminate the compute node.</p> </li> <li> <p> <code>CONTINUE</code> – Ignores the error and continues running the next script.</p> </li> </ul>"""
OnError: TypeAlias = Literal[
    "TERMINATE",
    "STOP_SEQUENCE",
    "CONTINUE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OnError) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OnError:
    return cast(OnError, data)
