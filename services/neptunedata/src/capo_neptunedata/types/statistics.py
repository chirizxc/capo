"""Generated from Smithy shape ``com.amazonaws.neptunedata#Statistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_neptunedata.types.statistics_summary


class Statistics(TypedDict, closed=True):
    auto_compute: NotRequired["bool"]
    """<p>Indicates whether or not automatic statistics generation is enabled.</p>"""
    active: NotRequired["bool"]
    """<p>Indicates whether or not DFE statistics generation is enabled at all.</p>"""
    statistics_id: NotRequired["str"]
    """<p>Reports the ID of the current statistics generation run. A value of -1 indicates that no statistics have been generated.</p>"""
    date: NotRequired["datetime.datetime"]
    """<p>The UTC time at which DFE statistics have most recently been generated.</p>"""
    note: NotRequired["str"]
    """<p>A note about problems in the case where statistics are invalid.</p>"""
    signature_info: NotRequired[
        "capo_neptunedata.types.statistics_summary.StatisticsSummary"
    ]
    """<p>A StatisticsSummary structure that contains:</p> <ul> <li> <p> <code>signatureCount</code> - The total number of signatures across all characteristic sets.</p> </li> <li> <p> <code>instanceCount</code> - The total number of characteristic-set instances.</p> </li> <li> <p> <code>predicateCount</code> - The total number of unique predicates.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: Statistics) -> dict:
    out: dict = {}
    if "auto_compute" in value:
        out["autoCompute"] = value["auto_compute"]
    if "active" in value:
        out["active"] = value["active"]
    if "statistics_id" in value:
        out["statisticsId"] = value["statistics_id"]
    if "date" in value:
        import capo_neptunedata._protocol.serialize

        out["date"] = capo_neptunedata._protocol.serialize.fmt_date_time(value["date"])
    if "note" in value:
        out["note"] = value["note"]
    if "signature_info" in value:
        import capo_neptunedata.types.statistics_summary

        out["signatureInfo"] = capo_neptunedata.types.statistics_summary.serialize_json(
            value["signature_info"]
        )
    return out


def deserialize_json(data: dict) -> Statistics:
    out: Statistics = {}  # type: ignore[typeddict-item]
    if data.get("autoCompute") is not None:
        out["auto_compute"] = data["autoCompute"]
    if data.get("active") is not None:
        out["active"] = data["active"]
    if data.get("statisticsId") is not None:
        out["statistics_id"] = data["statisticsId"]
    if data.get("date") is not None:
        import datetime

        out["date"] = datetime.datetime.fromisoformat(
            data["date"].replace("Z", "+00:00")
        )
    if data.get("note") is not None:
        out["note"] = data["note"]
    if data.get("signatureInfo") is not None:
        import capo_neptunedata.types.statistics_summary

        out["signature_info"] = (
            capo_neptunedata.types.statistics_summary.deserialize_json(
                data["signatureInfo"]
            )
        )
    return out
