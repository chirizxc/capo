"""Generated from Smithy shape ``com.amazonaws.appflow#AuthParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.boolean
    import capo_appflow.types.connector_supplied_value_list
    import capo_appflow.types.description
    import capo_appflow.types.key
    import capo_appflow.types.label


class AuthParameter(TypedDict, closed=True):
    key: NotRequired["capo_appflow.types.key.Key"]
    """<p>The authentication key required to authenticate with the connector.</p>"""
    is_required: "capo_appflow.types.boolean.Boolean"
    """<p>Indicates whether this authentication parameter is required.</p>"""
    label: NotRequired["capo_appflow.types.label.Label"]
    """<p>Label used for authentication parameter.</p>"""
    description: NotRequired["capo_appflow.types.description.Description"]
    """<p>A description about the authentication parameter.</p>"""
    is_sensitive_field: "capo_appflow.types.boolean.Boolean"
    """<p>Indicates whether this authentication parameter is a sensitive field.</p>"""
    connector_supplied_values: NotRequired[
        "capo_appflow.types.connector_supplied_value_list.ConnectorSuppliedValueList"
    ]
    """<p>Contains default values for this authentication parameter that are supplied by the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthParameter) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    out["isRequired"] = value.get("is_required", False)
    if "label" in value:
        out["label"] = value["label"]
    if "description" in value:
        out["description"] = value["description"]
    out["isSensitiveField"] = value.get("is_sensitive_field", False)
    if "connector_supplied_values" in value:
        import capo_appflow.types.connector_supplied_value_list

        out["connectorSuppliedValues"] = (
            capo_appflow.types.connector_supplied_value_list.serialize_json(
                value["connector_supplied_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuthParameter:
    out: AuthParameter = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("isRequired") is not None:
        out["is_required"] = data["isRequired"]
    else:
        out["is_required"] = False
    if data.get("label") is not None:
        out["label"] = data["label"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("isSensitiveField") is not None:
        out["is_sensitive_field"] = data["isSensitiveField"]
    else:
        out["is_sensitive_field"] = False
    if data.get("connectorSuppliedValues") is not None:
        import capo_appflow.types.connector_supplied_value_list

        out["connector_supplied_values"] = (
            capo_appflow.types.connector_supplied_value_list.deserialize_json(
                data["connectorSuppliedValues"]
            )
        )
    return out
