"""Generated from Smithy shape ``com.amazonaws.glue#IterableFormEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.form_type_id


class IterableFormEntry(TypedDict, closed=True):
    form_type_id: NotRequired["capo_glue.types.form_type_id.FormTypeId"]
    """<p>The form type identifier of the iterable form (for example, <code>columns</code>), used to retrieve its items via <code>ListIterableForms</code> or <code>BatchGetIterableForms</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IterableFormEntry) -> dict:
    out: dict = {}
    if "form_type_id" in value:
        out["FormTypeId"] = value["form_type_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IterableFormEntry:
    out: IterableFormEntry = {}  # type: ignore[typeddict-item]
    if data.get("FormTypeId") is not None:
        out["form_type_id"] = data["FormTypeId"]
    return out
