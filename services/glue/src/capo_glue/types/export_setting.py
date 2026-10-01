"""Generated from Smithy shape ``com.amazonaws.glue#ExportSetting``."""

from typing import Literal, TypeAlias, cast

"""<p>The export setting for the data catalog.</p>"""
ExportSetting: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportSetting) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExportSetting:
    return cast(ExportSetting, data)
