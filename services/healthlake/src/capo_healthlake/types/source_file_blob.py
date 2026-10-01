"""Generated from Smithy shape ``com.amazon.awshealthlakedatatransformationfrontendservice#SourceFileBlob``."""

import base64
from typing import TypeAlias

SourceFileBlob: TypeAlias = bytes


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SourceFileBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_0(data: str) -> SourceFileBlob:
    return base64.b64decode(data)
