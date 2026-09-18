"""Generated from Smithy shape ``com.amazonaws.omics#ReadOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.comment_char
    import capo_omics.types.encoding
    import capo_omics.types.escape_char
    import capo_omics.types.escape_quotes
    import capo_omics.types.header
    import capo_omics.types.line_sep
    import capo_omics.types.quote
    import capo_omics.types.quote_all
    import capo_omics.types.separator


class ReadOptions(TypedDict, closed=True):
    sep: NotRequired["capo_omics.types.separator.Separator"]
    """<p>The file's field separator.</p>"""
    encoding: NotRequired["capo_omics.types.encoding.Encoding"]
    """<p>The file's encoding.</p>"""
    quote: NotRequired["capo_omics.types.quote.Quote"]
    """<p>The file's quote character.</p>"""
    quote_all: "capo_omics.types.quote_all.QuoteAll"
    """<p>Whether all values need to be quoted, or just those that contain quotes.</p>"""
    escape: NotRequired["capo_omics.types.escape_char.EscapeChar"]
    """<p>A character for escaping quotes in the file.</p>"""
    escape_quotes: "capo_omics.types.escape_quotes.EscapeQuotes"
    """<p>Whether quotes need to be escaped in the file.</p>"""
    comment: NotRequired["capo_omics.types.comment_char.CommentChar"]
    """<p>The file's comment character.</p>"""
    header: "capo_omics.types.header.Header"
    """<p>Whether the file has a header row.</p>"""
    line_sep: NotRequired["capo_omics.types.line_sep.LineSep"]
    """<p>A line separator for the file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadOptions) -> dict:
    out: dict = {}
    if "sep" in value:
        out["sep"] = value["sep"]
    if "encoding" in value:
        out["encoding"] = value["encoding"]
    if "quote" in value:
        out["quote"] = value["quote"]
    out["quoteAll"] = value.get("quote_all", False)
    if "escape" in value:
        out["escape"] = value["escape"]
    out["escapeQuotes"] = value.get("escape_quotes", False)
    if "comment" in value:
        out["comment"] = value["comment"]
    out["header"] = value.get("header", False)
    if "line_sep" in value:
        out["lineSep"] = value["line_sep"]
    return out


def deserialize_json(data: dict) -> ReadOptions:
    out: ReadOptions = {}  # type: ignore[typeddict-item]
    if data.get("sep") is not None:
        out["sep"] = data["sep"]
    if data.get("encoding") is not None:
        out["encoding"] = data["encoding"]
    if data.get("quote") is not None:
        out["quote"] = data["quote"]
    if data.get("quoteAll") is not None:
        out["quote_all"] = data["quoteAll"]
    else:
        out["quote_all"] = False
    if data.get("escape") is not None:
        out["escape"] = data["escape"]
    if data.get("escapeQuotes") is not None:
        out["escape_quotes"] = data["escapeQuotes"]
    else:
        out["escape_quotes"] = False
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    if data.get("header") is not None:
        out["header"] = data["header"]
    else:
        out["header"] = False
    if data.get("lineSep") is not None:
        out["line_sep"] = data["lineSep"]
    return out
