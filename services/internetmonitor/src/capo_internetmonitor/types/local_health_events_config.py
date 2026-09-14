"""Generated from Smithy shape ``com.amazonaws.internetmonitor#LocalHealthEventsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.local_health_events_config_status
    import capo_internetmonitor.types.percentage


class LocalHealthEventsConfig(TypedDict, closed=True):
    status: NotRequired[
        "capo_internetmonitor.types.local_health_events_config_status.LocalHealthEventsConfigStatus"
    ]
    """<p>The status of whether Internet Monitor creates a health event based on a threshold percentage set for a local health score. The status can be <code>ENABLED</code> or <code>DISABLED</code>.</p>"""
    health_score_threshold: "capo_internetmonitor.types.percentage.Percentage"
    """<p>The health event threshold percentage set for a local health score.</p>"""
    min_traffic_impact: "capo_internetmonitor.types.percentage.Percentage"
    """<p>The minimum percentage of overall traffic for an application that must be impacted by an issue before Internet Monitor creates an event when a threshold is crossed for a local health score.</p> <p>If you don't set a minimum traffic impact threshold, the default value is 0.1%.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LocalHealthEventsConfig) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    out["HealthScoreThreshold"] = (
        "NaN"
        if value.get("health_score_threshold", 0)
        != value.get("health_score_threshold", 0)
        else "Infinity"
        if value.get("health_score_threshold", 0) == float("inf")
        else "-Infinity"
        if value.get("health_score_threshold", 0) == float("-inf")
        else value.get("health_score_threshold", 0)
    )
    out["MinTrafficImpact"] = (
        "NaN"
        if value.get("min_traffic_impact", 0) != value.get("min_traffic_impact", 0)
        else "Infinity"
        if value.get("min_traffic_impact", 0) == float("inf")
        else "-Infinity"
        if value.get("min_traffic_impact", 0) == float("-inf")
        else value.get("min_traffic_impact", 0)
    )
    return out


def deserialize_json(data: dict) -> LocalHealthEventsConfig:
    out: LocalHealthEventsConfig = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("HealthScoreThreshold") is not None:
        out["health_score_threshold"] = float(data["HealthScoreThreshold"])
    else:
        out["health_score_threshold"] = 0
    if data.get("MinTrafficImpact") is not None:
        out["min_traffic_impact"] = float(data["MinTrafficImpact"])
    else:
        out["min_traffic_impact"] = 0
    return out
