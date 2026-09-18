"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#Collector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.collector_health
    import capo_migrationhubstrategy.types.configuration_summary
    import capo_migrationhubstrategy.types.string


class Collector(TypedDict, closed=True):
    collector_id: NotRequired["capo_migrationhubstrategy.types.string.String"]
    """<p> The ID of the collector. </p>"""
    ip_address: NotRequired["capo_migrationhubstrategy.types.string.String"]
    """<p> IP address of the server that is hosting the collector. </p>"""
    host_name: NotRequired["capo_migrationhubstrategy.types.string.String"]
    """<p> Hostname of the server that is hosting the collector. </p>"""
    collector_health: NotRequired[
        "capo_migrationhubstrategy.types.collector_health.CollectorHealth"
    ]
    """<p> Indicates the health of a collector. </p>"""
    collector_version: NotRequired["capo_migrationhubstrategy.types.string.String"]
    """<p> Current version of the collector that is running in the environment that you specify. </p>"""
    registered_time_stamp: NotRequired["capo_migrationhubstrategy.types.string.String"]
    """<p> Time when the collector registered with the service. </p>"""
    last_activity_time_stamp: NotRequired[
        "capo_migrationhubstrategy.types.string.String"
    ]
    """<p> Time when the collector last pinged the service. </p>"""
    configuration_summary: NotRequired[
        "capo_migrationhubstrategy.types.configuration_summary.ConfigurationSummary"
    ]
    """<p>Summary of the collector configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Collector) -> dict:
    out: dict = {}
    if "collector_id" in value:
        out["collectorId"] = value["collector_id"]
    if "ip_address" in value:
        out["ipAddress"] = value["ip_address"]
    if "host_name" in value:
        out["hostName"] = value["host_name"]
    if "collector_health" in value:
        out["collectorHealth"] = value["collector_health"]
    if "collector_version" in value:
        out["collectorVersion"] = value["collector_version"]
    if "registered_time_stamp" in value:
        out["registeredTimeStamp"] = value["registered_time_stamp"]
    if "last_activity_time_stamp" in value:
        out["lastActivityTimeStamp"] = value["last_activity_time_stamp"]
    if "configuration_summary" in value:
        import capo_migrationhubstrategy.types.configuration_summary

        out["configurationSummary"] = (
            capo_migrationhubstrategy.types.configuration_summary.serialize_json(
                value["configuration_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> Collector:
    out: Collector = {}  # type: ignore[typeddict-item]
    if data.get("collectorId") is not None:
        out["collector_id"] = data["collectorId"]
    if data.get("ipAddress") is not None:
        out["ip_address"] = data["ipAddress"]
    if data.get("hostName") is not None:
        out["host_name"] = data["hostName"]
    if data.get("collectorHealth") is not None:
        out["collector_health"] = data["collectorHealth"]
    if data.get("collectorVersion") is not None:
        out["collector_version"] = data["collectorVersion"]
    if data.get("registeredTimeStamp") is not None:
        out["registered_time_stamp"] = data["registeredTimeStamp"]
    if data.get("lastActivityTimeStamp") is not None:
        out["last_activity_time_stamp"] = data["lastActivityTimeStamp"]
    if data.get("configurationSummary") is not None:
        import capo_migrationhubstrategy.types.configuration_summary

        out["configuration_summary"] = (
            capo_migrationhubstrategy.types.configuration_summary.deserialize_json(
                data["configurationSummary"]
            )
        )
    return out
