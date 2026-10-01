"""Generated from Smithy shape ``com.amazonaws.glue#ExportStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The current status of the data catalog export.</p>"""
ExportStatus: TypeAlias = Literal[
    "ENABLING",
    "ENABLED",
    "DISABLING",
    "DISABLED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExportStatus:
    return cast(ExportStatus, data)
