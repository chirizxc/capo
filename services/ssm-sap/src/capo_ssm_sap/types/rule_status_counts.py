"""Generated from Smithy shape ``com.amazonaws.ssmsap#RuleStatusCounts``."""

from typing_extensions import NotRequired, TypedDict


class RuleStatusCounts(TypedDict, closed=True):
    failed: NotRequired["int"]
    """<p>The number of rules that failed.</p>"""
    warning: NotRequired["int"]
    """<p>The number of rules that returned warnings.</p>"""
    info: NotRequired["int"]
    """<p>The number of rules that returned informational results.</p>"""
    passed: NotRequired["int"]
    """<p>The number of rules that passed.</p>"""
    unknown: NotRequired["int"]
    """<p>The number of rules with unknown status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleStatusCounts) -> dict:
    out: dict = {}
    if "failed" in value:
        out["Failed"] = value["failed"]
    if "warning" in value:
        out["Warning"] = value["warning"]
    if "info" in value:
        out["Info"] = value["info"]
    if "passed" in value:
        out["Passed"] = value["passed"]
    if "unknown" in value:
        out["Unknown"] = value["unknown"]
    return out


def deserialize_json(data: dict) -> RuleStatusCounts:
    out: RuleStatusCounts = {}  # type: ignore[typeddict-item]
    if data.get("Failed") is not None:
        out["failed"] = data["Failed"]
    if data.get("Warning") is not None:
        out["warning"] = data["Warning"]
    if data.get("Info") is not None:
        out["info"] = data["Info"]
    if data.get("Passed") is not None:
        out["passed"] = data["Passed"]
    if data.get("Unknown") is not None:
        out["unknown"] = data["Unknown"]
    return out
