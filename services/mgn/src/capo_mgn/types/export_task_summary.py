"""Generated from Smithy shape ``com.amazonaws.mgn#ExportTaskSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.positive_integer


class ExportTaskSummary(TypedDict, closed=True):
    servers_count: "capo_mgn.types.positive_integer.PositiveInteger"
    """<p>Export task summary servers count.</p>"""
    applications_count: "capo_mgn.types.positive_integer.PositiveInteger"
    """<p>Export task summary applications count.</p>"""
    waves_count: "capo_mgn.types.positive_integer.PositiveInteger"
    """<p>Export task summary waves count.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportTaskSummary) -> dict:
    out: dict = {}
    out["serversCount"] = value.get("servers_count", 0)
    out["applicationsCount"] = value.get("applications_count", 0)
    out["wavesCount"] = value.get("waves_count", 0)
    return out


def deserialize_json(data: dict) -> ExportTaskSummary:
    out: ExportTaskSummary = {}  # type: ignore[typeddict-item]
    if data.get("serversCount") is not None:
        out["servers_count"] = data["serversCount"]
    else:
        out["servers_count"] = 0
    if data.get("applicationsCount") is not None:
        out["applications_count"] = data["applicationsCount"]
    else:
        out["applications_count"] = 0
    if data.get("wavesCount") is not None:
        out["waves_count"] = data["wavesCount"]
    else:
        out["waves_count"] = 0
    return out
