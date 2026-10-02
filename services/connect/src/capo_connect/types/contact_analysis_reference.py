"""Generated from Smithy shape ``com.amazonaws.connect#ContactAnalysisReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.analytics_mode
    import capo_connect.types.arn
    import capo_connect.types.nullable_boolean
    import capo_connect.types.reference_key
    import capo_connect.types.reference_status
    import capo_connect.types.reference_value


class ContactAnalysisReference(TypedDict, closed=True):
    name: NotRequired["capo_connect.types.reference_key.ReferenceKey"]
    """<p>Identifier of the contact analysis reference.</p>"""
    value: NotRequired["capo_connect.types.reference_value.ReferenceValue"]
    """<p>The location path of the contact analysis reference.</p>"""
    status: NotRequired["capo_connect.types.reference_status.ReferenceStatus"]
    """<p>Status of the contact analysis reference type.</p>"""
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the contact analysis reference.</p>"""
    analytics_mode: NotRequired["capo_connect.types.analytics_mode.AnalyticsMode"]
    """<p>The analytics mode of the contact analysis.</p>"""
    is_redacted: NotRequired["capo_connect.types.nullable_boolean.NullableBoolean"]
    """<p>Indicates whether sensitive data has been redacted from the contact analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactAnalysisReference) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    if "status" in value:
        import capo_connect.types.reference_status

        out["Status"] = capo_connect.types.reference_status.serialize_json(
            value["status"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "analytics_mode" in value:
        import capo_connect.types.analytics_mode

        out["AnalyticsMode"] = capo_connect.types.analytics_mode.serialize_json(
            value["analytics_mode"]
        )
    if "is_redacted" in value:
        out["IsRedacted"] = value["is_redacted"]
    return out


def deserialize_json(data: dict) -> ContactAnalysisReference:
    out: ContactAnalysisReference = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Status") is not None:
        import capo_connect.types.reference_status

        out["status"] = capo_connect.types.reference_status.deserialize_json(
            data["Status"]
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("AnalyticsMode") is not None:
        import capo_connect.types.analytics_mode

        out["analytics_mode"] = capo_connect.types.analytics_mode.deserialize_json(
            data["AnalyticsMode"]
        )
    if data.get("IsRedacted") is not None:
        out["is_redacted"] = data["IsRedacted"]
    return out
