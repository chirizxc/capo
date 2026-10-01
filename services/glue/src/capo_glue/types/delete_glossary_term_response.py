"""Generated from Smithy shape ``com.amazonaws.glue#DeleteGlossaryTermResponse``."""

from typing_extensions import TypedDict


class DeleteGlossaryTermResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGlossaryTermResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteGlossaryTermResponse:
    out: DeleteGlossaryTermResponse = {}  # type: ignore[typeddict-item]
    return out
