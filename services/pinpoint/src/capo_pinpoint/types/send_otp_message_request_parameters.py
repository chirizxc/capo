"""Generated from Smithy shape ``com.amazonaws.pinpoint#SendOTPMessageRequestParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__integer
    import capo_pinpoint.types.__string


class SendOTPMessageRequestParameters(TypedDict, closed=True):
    allowed_attempts: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The attempts allowed to validate an OTP.</p>"""
    brand_name: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The brand name that will be substituted into the OTP message body. Should be owned by calling AWS account.</p>"""
    channel: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>Channel type for the OTP message. Supported values: [SMS].</p>"""
    code_length: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The number of characters in the generated OTP.</p>"""
    destination_identity: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The destination identity to send OTP to.</p>"""
    entity_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>A unique Entity ID received from DLT after entity registration is approved.</p>"""
    language: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The language to be used for the outgoing message body containing the OTP.</p>"""
    origination_identity: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The origination identity used to send OTP from.</p>"""
    reference_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>Developer-specified reference identifier. Required to match during OTP verification.</p>"""
    template_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>A unique Template ID received from DLT after entity registration is approved.</p>"""
    validity_period: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The time in minutes before the OTP is no longer valid.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendOTPMessageRequestParameters) -> dict:
    out: dict = {}
    if "allowed_attempts" in value:
        out["AllowedAttempts"] = value["allowed_attempts"]
    if "brand_name" in value:
        out["BrandName"] = value["brand_name"]
    if "channel" in value:
        out["Channel"] = value["channel"]
    if "code_length" in value:
        out["CodeLength"] = value["code_length"]
    if "destination_identity" in value:
        out["DestinationIdentity"] = value["destination_identity"]
    if "entity_id" in value:
        out["EntityId"] = value["entity_id"]
    if "language" in value:
        out["Language"] = value["language"]
    if "origination_identity" in value:
        out["OriginationIdentity"] = value["origination_identity"]
    if "reference_id" in value:
        out["ReferenceId"] = value["reference_id"]
    if "template_id" in value:
        out["TemplateId"] = value["template_id"]
    if "validity_period" in value:
        out["ValidityPeriod"] = value["validity_period"]
    return out


def deserialize_json(data: dict) -> SendOTPMessageRequestParameters:
    out: SendOTPMessageRequestParameters = {}  # type: ignore[typeddict-item]
    if data.get("AllowedAttempts") is not None:
        out["allowed_attempts"] = data["AllowedAttempts"]
    if data.get("BrandName") is not None:
        out["brand_name"] = data["BrandName"]
    if data.get("Channel") is not None:
        out["channel"] = data["Channel"]
    if data.get("CodeLength") is not None:
        out["code_length"] = data["CodeLength"]
    if data.get("DestinationIdentity") is not None:
        out["destination_identity"] = data["DestinationIdentity"]
    if data.get("EntityId") is not None:
        out["entity_id"] = data["EntityId"]
    if data.get("Language") is not None:
        out["language"] = data["Language"]
    if data.get("OriginationIdentity") is not None:
        out["origination_identity"] = data["OriginationIdentity"]
    if data.get("ReferenceId") is not None:
        out["reference_id"] = data["ReferenceId"]
    if data.get("TemplateId") is not None:
        out["template_id"] = data["TemplateId"]
    if data.get("ValidityPeriod") is not None:
        out["validity_period"] = data["ValidityPeriod"]
    return out
