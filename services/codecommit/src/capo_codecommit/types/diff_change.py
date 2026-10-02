"""Generated from Smithy shape ``com.amazonaws.codecommit#DiffChange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.diff_change_type
    import capo_codecommit.types.line_content
    import capo_codecommit.types.line_number


class DiffChange(TypedDict, closed=True):
    type: NotRequired["capo_codecommit.types.diff_change_type.DiffChangeType"]
    """<p>The type of change for this line. Possible values:</p> <ul> <li> <p> <code>CONTEXT</code> – Unchanged line included for surrounding context.</p> </li> <li> <p> <code>ADD</code> – Line added in the after blob.</p> </li> <li> <p> <code>DELETE</code> – Line removed from the before blob.</p> </li> </ul>"""
    before_line_number: NotRequired["capo_codecommit.types.line_number.LineNumber"]
    """<p>The 1-based line number in the before blob. This field is omitted for <code>ADD</code> lines.</p>"""
    after_line_number: NotRequired["capo_codecommit.types.line_number.LineNumber"]
    """<p>The 1-based line number in the after blob. This field is omitted for <code>DELETE</code> lines.</p>"""
    content: NotRequired["capo_codecommit.types.line_content.LineContent"]
    """<p>The text content of the line, without the trailing newline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiffChange) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_codecommit.types.diff_change_type

        out["type"] = capo_codecommit.types.diff_change_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "before_line_number" in value:
        out["beforeLineNumber"] = value["before_line_number"]
    if "after_line_number" in value:
        out["afterLineNumber"] = value["after_line_number"]
    if "content" in value:
        out["content"] = value["content"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DiffChange:
    out: DiffChange = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_codecommit.types.diff_change_type

        out["type"] = capo_codecommit.types.diff_change_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if data.get("beforeLineNumber") is not None:
        out["before_line_number"] = data["beforeLineNumber"]
    if data.get("afterLineNumber") is not None:
        out["after_line_number"] = data["afterLineNumber"]
    if data.get("content") is not None:
        out["content"] = data["content"]
    return out
