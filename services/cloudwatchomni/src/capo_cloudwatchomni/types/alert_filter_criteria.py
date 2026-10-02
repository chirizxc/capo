"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AlertFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.alert_id_filter_list
    import capo_cloudwatchomni.types.alert_name_filter_list
    import capo_cloudwatchomni.types.alert_state_list


class AlertFilterCriteria(TypedDict, closed=True):
    names: NotRequired[
        "capo_cloudwatchomni.types.alert_name_filter_list.AlertNameFilterList"
    ]
    """Filter to alerts whose name exactly matches any entry (OR semantics). Mutually exclusive with {@code namePrefix} and {@code ids}."""
    name_prefix: NotRequired["str"]
    """Filter to alerts whose name starts with this prefix. Mutually exclusive with {@code names} and {@code ids}."""
    ids: NotRequired["capo_cloudwatchomni.types.alert_id_filter_list.AlertIdFilterList"]
    """Filter to alerts whose {@link AlertId} exactly matches any entry (OR semantics). Mutually exclusive with {@code names} and {@code namePrefix}."""
    state_value: NotRequired[
        "capo_cloudwatchomni.types.alert_state_list.AlertStateList"
    ]
    """Filter to alerts currently in any of these states (OR semantics)."""
    notifications_enabled: NotRequired["bool"]
    """Filter to alerts by whether notifications are enabled."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlertFilterCriteria) -> dict:
    out: dict = {}
    if "names" in value:
        import capo_cloudwatchomni.types.alert_name_filter_list

        out["names"] = capo_cloudwatchomni.types.alert_name_filter_list.serialize_cbor(
            value["names"]
        )
    if "name_prefix" in value:
        out["namePrefix"] = value["name_prefix"]
    if "ids" in value:
        import capo_cloudwatchomni.types.alert_id_filter_list

        out["ids"] = capo_cloudwatchomni.types.alert_id_filter_list.serialize_cbor(
            value["ids"]
        )
    if "state_value" in value:
        import capo_cloudwatchomni.types.alert_state_list

        out["stateValue"] = capo_cloudwatchomni.types.alert_state_list.serialize_cbor(
            value["state_value"]
        )
    if "notifications_enabled" in value:
        out["notificationsEnabled"] = value["notifications_enabled"]
    return out


def deserialize_cbor(data: dict) -> AlertFilterCriteria:
    out: AlertFilterCriteria = {}  # type: ignore[typeddict-item]
    if data.get("names") is not None:
        import capo_cloudwatchomni.types.alert_name_filter_list

        out["names"] = (
            capo_cloudwatchomni.types.alert_name_filter_list.deserialize_cbor(
                data["names"]
            )
        )
    if data.get("namePrefix") is not None:
        out["name_prefix"] = data["namePrefix"]
    if data.get("ids") is not None:
        import capo_cloudwatchomni.types.alert_id_filter_list

        out["ids"] = capo_cloudwatchomni.types.alert_id_filter_list.deserialize_cbor(
            data["ids"]
        )
    if data.get("stateValue") is not None:
        import capo_cloudwatchomni.types.alert_state_list

        out["state_value"] = (
            capo_cloudwatchomni.types.alert_state_list.deserialize_cbor(
                data["stateValue"]
            )
        )
    if data.get("notificationsEnabled") is not None:
        out["notifications_enabled"] = data["notificationsEnabled"]
    return out
