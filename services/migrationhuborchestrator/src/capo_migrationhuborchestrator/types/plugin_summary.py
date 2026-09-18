"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#PluginSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.ip_address
    import capo_migrationhuborchestrator.types.plugin_health
    import capo_migrationhuborchestrator.types.plugin_id
    import capo_migrationhuborchestrator.types.plugin_version


class PluginSummary(TypedDict, closed=True):
    plugin_id: NotRequired["capo_migrationhuborchestrator.types.plugin_id.PluginId"]
    """<p>The ID of the plugin.</p>"""
    hostname: NotRequired["str"]
    """<p>The name of the host.</p>"""
    status: NotRequired[
        "capo_migrationhuborchestrator.types.plugin_health.PluginHealth"
    ]
    """<p>The status of the plugin.</p>"""
    ip_address: NotRequired["capo_migrationhuborchestrator.types.ip_address.IPAddress"]
    """<p>The IP address at which the plugin is located.</p>"""
    version: NotRequired[
        "capo_migrationhuborchestrator.types.plugin_version.PluginVersion"
    ]
    """<p>The version of the plugin.</p>"""
    registered_time: NotRequired["str"]
    """<p>The time at which the plugin was registered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PluginSummary) -> dict:
    out: dict = {}
    if "plugin_id" in value:
        out["pluginId"] = value["plugin_id"]
    if "hostname" in value:
        out["hostname"] = value["hostname"]
    if "status" in value:
        out["status"] = value["status"]
    if "ip_address" in value:
        out["ipAddress"] = value["ip_address"]
    if "version" in value:
        out["version"] = value["version"]
    if "registered_time" in value:
        out["registeredTime"] = value["registered_time"]
    return out


def deserialize_json(data: dict) -> PluginSummary:
    out: PluginSummary = {}  # type: ignore[typeddict-item]
    if data.get("pluginId") is not None:
        out["plugin_id"] = data["pluginId"]
    if data.get("hostname") is not None:
        out["hostname"] = data["hostname"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("ipAddress") is not None:
        out["ip_address"] = data["ipAddress"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("registeredTime") is not None:
        out["registered_time"] = data["registeredTime"]
    return out
