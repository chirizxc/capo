"""Generated from Smithy shape ``com.amazonaws.codecommit#DiffHunk``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.count
    import capo_codecommit.types.diff_change_list
    import capo_codecommit.types.line_number


class DiffHunk(TypedDict, closed=True):
    before_start_line: NotRequired["capo_codecommit.types.line_number.LineNumber"]
    """<p>The 1-based line number in the before blob where this hunk begins. When the hunk consists entirely of additions, <code>beforeLineCount</code> is <code>0</code>.</p>"""
    before_line_count: NotRequired["capo_codecommit.types.count.Count"]
    """<p>The number of lines from the before blob covered by this hunk, including any context lines.</p>"""
    after_start_line: NotRequired["capo_codecommit.types.line_number.LineNumber"]
    """<p>The 1-based line number in the after blob where this hunk begins. When the hunk consists entirely of deletions, <code>afterLineCount</code> is <code>0</code>.</p>"""
    after_line_count: NotRequired["capo_codecommit.types.count.Count"]
    """<p>The number of lines from the after blob covered by this hunk, including any context lines.</p>"""
    changes: NotRequired["capo_codecommit.types.diff_change_list.DiffChangeList"]
    """<p>An ordered list of line-level changes that make up this hunk. Each entry indicates whether the line is unchanged context, an addition, or a deletion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiffHunk) -> dict:
    out: dict = {}
    if "before_start_line" in value:
        out["beforeStartLine"] = value["before_start_line"]
    if "before_line_count" in value:
        out["beforeLineCount"] = value["before_line_count"]
    if "after_start_line" in value:
        out["afterStartLine"] = value["after_start_line"]
    if "after_line_count" in value:
        out["afterLineCount"] = value["after_line_count"]
    if "changes" in value:
        import capo_codecommit.types.diff_change_list

        out["changes"] = capo_codecommit.types.diff_change_list.serialize_aws_json_1_1(
            value["changes"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DiffHunk:
    out: DiffHunk = {}  # type: ignore[typeddict-item]
    if data.get("beforeStartLine") is not None:
        out["before_start_line"] = data["beforeStartLine"]
    if data.get("beforeLineCount") is not None:
        out["before_line_count"] = data["beforeLineCount"]
    if data.get("afterStartLine") is not None:
        out["after_start_line"] = data["afterStartLine"]
    if data.get("afterLineCount") is not None:
        out["after_line_count"] = data["afterLineCount"]
    if data.get("changes") is not None:
        import capo_codecommit.types.diff_change_list

        out["changes"] = (
            capo_codecommit.types.diff_change_list.deserialize_aws_json_1_1(
                data["changes"]
            )
        )
    return out
