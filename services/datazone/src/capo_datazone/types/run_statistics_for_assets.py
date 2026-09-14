"""Generated from Smithy shape ``com.amazonaws.datazone#RunStatisticsForAssets``."""

from typing_extensions import NotRequired, TypedDict


class RunStatisticsForAssets(TypedDict, closed=True):
    added: NotRequired["int"]
    """<p>The <code>added</code> statistic for the data source run.</p>"""
    updated: NotRequired["int"]
    """<p>The <code>updated</code> statistic for the data source run.</p>"""
    unchanged: NotRequired["int"]
    """<p>The <code>unchanged</code> statistic for the data source run.</p>"""
    skipped: NotRequired["int"]
    """<p>The <code>skipped</code> statistic for the data source run.</p>"""
    failed: NotRequired["int"]
    """<p>The <code>failed</code> statistic for the data source run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RunStatisticsForAssets) -> dict:
    out: dict = {}
    if "added" in value:
        out["added"] = value["added"]
    if "updated" in value:
        out["updated"] = value["updated"]
    if "unchanged" in value:
        out["unchanged"] = value["unchanged"]
    if "skipped" in value:
        out["skipped"] = value["skipped"]
    if "failed" in value:
        out["failed"] = value["failed"]
    return out


def deserialize_json(data: dict) -> RunStatisticsForAssets:
    out: RunStatisticsForAssets = {}  # type: ignore[typeddict-item]
    if data.get("added") is not None:
        out["added"] = data["added"]
    if data.get("updated") is not None:
        out["updated"] = data["updated"]
    if data.get("unchanged") is not None:
        out["unchanged"] = data["unchanged"]
    if data.get("skipped") is not None:
        out["skipped"] = data["skipped"]
    if data.get("failed") is not None:
        out["failed"] = data["failed"]
    return out
