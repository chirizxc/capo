"""Generated from Smithy shape ``com.amazonaws.glue#AssetFormEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.form_content
    import capo_glue.types.form_type_id


class AssetFormEntry(TypedDict, closed=True):
    form_type_id: NotRequired["capo_glue.types.form_type_id.FormTypeId"]
    """<p>The identifier of the form type that defines this form's schema.</p>"""
    content: NotRequired["capo_glue.types.form_content.FormContent"]
    """<p>The JSON content of the form, conforming to the schema of the specified form type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssetFormEntry) -> dict:
    out: dict = {}
    if "form_type_id" in value:
        out["FormTypeId"] = value["form_type_id"]
    if "content" in value:
        out["Content"] = value["content"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssetFormEntry:
    out: AssetFormEntry = {}  # type: ignore[typeddict-item]
    if data.get("FormTypeId") is not None:
        out["form_type_id"] = data["FormTypeId"]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    return out
