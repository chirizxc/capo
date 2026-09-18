"""Generated from Smithy shape ``com.amazonaws.internetmonitor#HealthEventsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.local_health_events_config
    import capo_internetmonitor.types.percentage


class HealthEventsConfig(TypedDict, closed=True):
    availability_score_threshold: "capo_internetmonitor.types.percentage.Percentage"
    """<p>The health event threshold percentage set for availability scores.</p>"""
    performance_score_threshold: "capo_internetmonitor.types.percentage.Percentage"
    """<p>The health event threshold percentage set for performance scores.</p>"""
    availability_local_health_events_config: NotRequired[
        "capo_internetmonitor.types.local_health_events_config.LocalHealthEventsConfig"
    ]
    """<p>The configuration that determines the threshold and other conditions for when Internet Monitor creates a health event for a local availability issue.</p>"""
    performance_local_health_events_config: NotRequired[
        "capo_internetmonitor.types.local_health_events_config.LocalHealthEventsConfig"
    ]
    """<p>The configuration that determines the threshold and other conditions for when Internet Monitor creates a health event for a local performance issue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HealthEventsConfig) -> dict:
    out: dict = {}
    out["AvailabilityScoreThreshold"] = (
        "NaN"
        if value.get("availability_score_threshold", 0)
        != value.get("availability_score_threshold", 0)
        else "Infinity"
        if value.get("availability_score_threshold", 0) == float("inf")
        else "-Infinity"
        if value.get("availability_score_threshold", 0) == float("-inf")
        else value.get("availability_score_threshold", 0)
    )
    out["PerformanceScoreThreshold"] = (
        "NaN"
        if value.get("performance_score_threshold", 0)
        != value.get("performance_score_threshold", 0)
        else "Infinity"
        if value.get("performance_score_threshold", 0) == float("inf")
        else "-Infinity"
        if value.get("performance_score_threshold", 0) == float("-inf")
        else value.get("performance_score_threshold", 0)
    )
    if "availability_local_health_events_config" in value:
        import capo_internetmonitor.types.local_health_events_config

        out["AvailabilityLocalHealthEventsConfig"] = (
            capo_internetmonitor.types.local_health_events_config.serialize_json(
                value["availability_local_health_events_config"]
            )
        )
    if "performance_local_health_events_config" in value:
        import capo_internetmonitor.types.local_health_events_config

        out["PerformanceLocalHealthEventsConfig"] = (
            capo_internetmonitor.types.local_health_events_config.serialize_json(
                value["performance_local_health_events_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> HealthEventsConfig:
    out: HealthEventsConfig = {}  # type: ignore[typeddict-item]
    if data.get("AvailabilityScoreThreshold") is not None:
        out["availability_score_threshold"] = float(data["AvailabilityScoreThreshold"])
    else:
        out["availability_score_threshold"] = 0
    if data.get("PerformanceScoreThreshold") is not None:
        out["performance_score_threshold"] = float(data["PerformanceScoreThreshold"])
    else:
        out["performance_score_threshold"] = 0
    if data.get("AvailabilityLocalHealthEventsConfig") is not None:
        import capo_internetmonitor.types.local_health_events_config

        out["availability_local_health_events_config"] = (
            capo_internetmonitor.types.local_health_events_config.deserialize_json(
                data["AvailabilityLocalHealthEventsConfig"]
            )
        )
    if data.get("PerformanceLocalHealthEventsConfig") is not None:
        import capo_internetmonitor.types.local_health_events_config

        out["performance_local_health_events_config"] = (
            capo_internetmonitor.types.local_health_events_config.deserialize_json(
                data["PerformanceLocalHealthEventsConfig"]
            )
        )
    return out
