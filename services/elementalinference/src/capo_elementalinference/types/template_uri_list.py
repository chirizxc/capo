"""Generated from Smithy shape ``com.amazonaws.elementalinference#TemplateUriList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elementalinference.types.s3_uri

TemplateUriList: TypeAlias = list["capo_elementalinference.types.s3_uri.S3Uri"]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateUriList) -> list:
    return list(value)


def deserialize_json(data: list) -> TemplateUriList:
    return [item for item in data if item is not None]
