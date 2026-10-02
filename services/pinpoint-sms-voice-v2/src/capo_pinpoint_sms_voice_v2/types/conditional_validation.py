"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ConditionalValidation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.select_choice_list


class ConditionalValidation(TypedDict, closed=True):
    min_length: NotRequired["int"]
    """<p>The minimum length for the field value when this rule applies.</p>"""
    max_length: NotRequired["int"]
    """<p>The maximum length for the field value when this rule applies.</p>"""
    pattern: NotRequired["str"]
    """<p>A regular expression that the field value must match when this rule applies.</p>"""
    allowed_values: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.select_choice_list.SelectChoiceList"
    ]
    """<p>The allowed values for a select field when this rule applies. A subset of the field's full option list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConditionalValidation) -> dict:
    out: dict = {}
    if "min_length" in value:
        out["MinLength"] = value["min_length"]
    if "max_length" in value:
        out["MaxLength"] = value["max_length"]
    if "pattern" in value:
        out["Pattern"] = value["pattern"]
    if "allowed_values" in value:
        import capo_pinpoint_sms_voice_v2.types.select_choice_list

        out["AllowedValues"] = (
            capo_pinpoint_sms_voice_v2.types.select_choice_list.serialize_aws_json_1_0(
                value["allowed_values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConditionalValidation:
    out: ConditionalValidation = {}  # type: ignore[typeddict-item]
    if data.get("MinLength") is not None:
        out["min_length"] = data["MinLength"]
    if data.get("MaxLength") is not None:
        out["max_length"] = data["MaxLength"]
    if data.get("Pattern") is not None:
        out["pattern"] = data["Pattern"]
    if data.get("AllowedValues") is not None:
        import capo_pinpoint_sms_voice_v2.types.select_choice_list

        out["allowed_values"] = (
            capo_pinpoint_sms_voice_v2.types.select_choice_list.deserialize_aws_json_1_0(
                data["AllowedValues"]
            )
        )
    return out
