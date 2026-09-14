"""Generated from Smithy shape ``com.amazonaws.xray#ResponseTimeRootCauseService``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.nullable_boolean
    import capo_xray.types.response_time_root_cause_entity_path
    import capo_xray.types.service_names
    import capo_xray.types.string


class ResponseTimeRootCauseService(TypedDict, closed=True):
    name: NotRequired["capo_xray.types.string.String"]
    """<p>The service name.</p>"""
    names: NotRequired["capo_xray.types.service_names.ServiceNames"]
    """<p>A collection of associated service names.</p>"""
    type: NotRequired["capo_xray.types.string.String"]
    """<p>The type associated to the service.</p>"""
    account_id: NotRequired["capo_xray.types.string.String"]
    """<p>The account ID associated to the service.</p>"""
    entity_path: NotRequired[
        "capo_xray.types.response_time_root_cause_entity_path.ResponseTimeRootCauseEntityPath"
    ]
    """<p>The path of root cause entities found on the service. </p>"""
    inferred: NotRequired["capo_xray.types.nullable_boolean.NullableBoolean"]
    """<p>A Boolean value indicating if the service is inferred from the trace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponseTimeRootCauseService) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "names" in value:
        import capo_xray.types.service_names

        out["Names"] = capo_xray.types.service_names.serialize_json(value["names"])
    if "type" in value:
        out["Type"] = value["type"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "entity_path" in value:
        import capo_xray.types.response_time_root_cause_entity_path

        out["EntityPath"] = (
            capo_xray.types.response_time_root_cause_entity_path.serialize_json(
                value["entity_path"]
            )
        )
    if "inferred" in value:
        out["Inferred"] = value["inferred"]
    return out


def deserialize_json(data: dict) -> ResponseTimeRootCauseService:
    out: ResponseTimeRootCauseService = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Names") is not None:
        import capo_xray.types.service_names

        out["names"] = capo_xray.types.service_names.deserialize_json(data["Names"])
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("EntityPath") is not None:
        import capo_xray.types.response_time_root_cause_entity_path

        out["entity_path"] = (
            capo_xray.types.response_time_root_cause_entity_path.deserialize_json(
                data["EntityPath"]
            )
        )
    if data.get("Inferred") is not None:
        out["inferred"] = data["Inferred"]
    return out
