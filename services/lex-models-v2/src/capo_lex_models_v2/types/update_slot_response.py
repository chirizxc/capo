"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateSlotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.built_in_or_custom_slot_type_id
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.multiple_values_setting
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.obfuscation_setting
    import capo_lex_models_v2.types.slot_value_elicitation_setting
    import capo_lex_models_v2.types.sub_slot_setting
    import capo_lex_models_v2.types.timestamp


class UpdateSlotResponse(TypedDict, closed=True):
    slot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the slot that was updated.</p>"""
    slot_name: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>The updated name of the slot.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The updated description of the bot.</p>"""
    slot_type_id: NotRequired[
        "capo_lex_models_v2.types.built_in_or_custom_slot_type_id.BuiltInOrCustomSlotTypeId"
    ]
    """<p>The updated identifier of the slot type that provides values for the slot.</p>"""
    value_elicitation_setting: NotRequired[
        "capo_lex_models_v2.types.slot_value_elicitation_setting.SlotValueElicitationSetting"
    ]
    """<p>The updated prompts that Amazon Lex sends to the user to elicit a response that provides a value for the slot.</p>"""
    obfuscation_setting: NotRequired[
        "capo_lex_models_v2.types.obfuscation_setting.ObfuscationSetting"
    ]
    """<p>The updated setting that determines whether the slot value is obfuscated in the Amazon CloudWatch logs.</p>"""
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot that contains the slot.</p>"""
    bot_version: NotRequired[
        "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The version of the bot that contains the slot. Will always be <code>DRAFT</code>.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The locale that contains the slot.</p>"""
    intent_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The intent that contains the slot.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The timestamp of the date and time that the slot was created.</p>"""
    last_updated_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The timestamp of the date and time that the slot was last updated.</p>"""
    multiple_values_setting: NotRequired[
        "capo_lex_models_v2.types.multiple_values_setting.MultipleValuesSetting"
    ]
    """<p>Indicates whether the slot accepts multiple values in one response.</p>"""
    sub_slot_setting: NotRequired[
        "capo_lex_models_v2.types.sub_slot_setting.SubSlotSetting"
    ]
    """<p>Specifications for the constituent sub slots and the expression for the composite slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSlotResponse) -> dict:
    out: dict = {}
    if "slot_id" in value:
        out["slotId"] = value["slot_id"]
    if "slot_name" in value:
        out["slotName"] = value["slot_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "slot_type_id" in value:
        out["slotTypeId"] = value["slot_type_id"]
    if "value_elicitation_setting" in value:
        import capo_lex_models_v2.types.slot_value_elicitation_setting

        out["valueElicitationSetting"] = (
            capo_lex_models_v2.types.slot_value_elicitation_setting.serialize_json(
                value["value_elicitation_setting"]
            )
        )
    if "obfuscation_setting" in value:
        import capo_lex_models_v2.types.obfuscation_setting

        out["obfuscationSetting"] = (
            capo_lex_models_v2.types.obfuscation_setting.serialize_json(
                value["obfuscation_setting"]
            )
        )
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "intent_id" in value:
        out["intentId"] = value["intent_id"]
    if "creation_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["creationDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["last_updated_date_time"]
        )
    if "multiple_values_setting" in value:
        import capo_lex_models_v2.types.multiple_values_setting

        out["multipleValuesSetting"] = (
            capo_lex_models_v2.types.multiple_values_setting.serialize_json(
                value["multiple_values_setting"]
            )
        )
    if "sub_slot_setting" in value:
        import capo_lex_models_v2.types.sub_slot_setting

        out["subSlotSetting"] = (
            capo_lex_models_v2.types.sub_slot_setting.serialize_json(
                value["sub_slot_setting"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSlotResponse:
    out: UpdateSlotResponse = {}  # type: ignore[typeddict-item]
    if data.get("slotId") is not None:
        out["slot_id"] = data["slotId"]
    if data.get("slotName") is not None:
        out["slot_name"] = data["slotName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("slotTypeId") is not None:
        out["slot_type_id"] = data["slotTypeId"]
    if data.get("valueElicitationSetting") is not None:
        import capo_lex_models_v2.types.slot_value_elicitation_setting

        out["value_elicitation_setting"] = (
            capo_lex_models_v2.types.slot_value_elicitation_setting.deserialize_json(
                data["valueElicitationSetting"]
            )
        )
    if data.get("obfuscationSetting") is not None:
        import capo_lex_models_v2.types.obfuscation_setting

        out["obfuscation_setting"] = (
            capo_lex_models_v2.types.obfuscation_setting.deserialize_json(
                data["obfuscationSetting"]
            )
        )
    if data.get("botId") is not None:
        out["bot_id"] = data["botId"]
    if data.get("botVersion") is not None:
        out["bot_version"] = data["botVersion"]
    if data.get("localeId") is not None:
        out["locale_id"] = data["localeId"]
    if data.get("intentId") is not None:
        out["intent_id"] = data["intentId"]
    if data.get("creationDateTime") is not None:
        import capo_lex_models_v2.types.timestamp

        out["creation_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    if data.get("lastUpdatedDateTime") is not None:
        import capo_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    if data.get("multipleValuesSetting") is not None:
        import capo_lex_models_v2.types.multiple_values_setting

        out["multiple_values_setting"] = (
            capo_lex_models_v2.types.multiple_values_setting.deserialize_json(
                data["multipleValuesSetting"]
            )
        )
    if data.get("subSlotSetting") is not None:
        import capo_lex_models_v2.types.sub_slot_setting

        out["sub_slot_setting"] = (
            capo_lex_models_v2.types.sub_slot_setting.deserialize_json(
                data["subSlotSetting"]
            )
        )
    return out
