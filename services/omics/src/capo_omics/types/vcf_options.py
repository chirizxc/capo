"""Generated from Smithy shape ``com.amazonaws.omics#VcfOptions``."""

from typing_extensions import NotRequired, TypedDict


class VcfOptions(TypedDict, closed=True):
    ignore_qual_field: NotRequired["bool"]
    """<p>The file's ignore qual field setting.</p>"""
    ignore_filter_field: NotRequired["bool"]
    """<p>The file's ignore filter field setting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VcfOptions) -> dict:
    out: dict = {}
    if "ignore_qual_field" in value:
        out["ignoreQualField"] = value["ignore_qual_field"]
    if "ignore_filter_field" in value:
        out["ignoreFilterField"] = value["ignore_filter_field"]
    return out


def deserialize_json(data: dict) -> VcfOptions:
    out: VcfOptions = {}  # type: ignore[typeddict-item]
    if data.get("ignoreQualField") is not None:
        out["ignore_qual_field"] = data["ignoreQualField"]
    if data.get("ignoreFilterField") is not None:
        out["ignore_filter_field"] = data["ignoreFilterField"]
    return out
