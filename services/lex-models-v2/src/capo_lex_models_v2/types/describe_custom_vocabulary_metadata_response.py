"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeCustomVocabularyMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.custom_vocabulary_status
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.timestamp


class DescribeCustomVocabularyMetadataResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot that contains the custom vocabulary.</p>"""
    bot_version: NotRequired["capo_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The version of the bot that contains the custom vocabulary to describe.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The locale that contains the custom vocabulary to describe.</p>"""
    custom_vocabulary_status: NotRequired[
        "capo_lex_models_v2.types.custom_vocabulary_status.CustomVocabularyStatus"
    ]
    """<p>The status of the custom vocabulary. If the status is <code>Ready</code> the custom vocabulary is ready to use.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time that the custom vocabulary was created.</p>"""
    last_updated_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time that the custom vocabulary was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCustomVocabularyMetadataResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "custom_vocabulary_status" in value:
        import capo_lex_models_v2.types.custom_vocabulary_status

        out["customVocabularyStatus"] = (
            capo_lex_models_v2.types.custom_vocabulary_status.serialize_json(
                value["custom_vocabulary_status"]
            )
        )
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
    return out


def deserialize_json(data: dict) -> DescribeCustomVocabularyMetadataResponse:
    out: DescribeCustomVocabularyMetadataResponse = {}  # type: ignore[typeddict-item]
    if data.get("botId") is not None:
        out["bot_id"] = data["botId"]
    if data.get("botVersion") is not None:
        out["bot_version"] = data["botVersion"]
    if data.get("localeId") is not None:
        out["locale_id"] = data["localeId"]
    if data.get("customVocabularyStatus") is not None:
        import capo_lex_models_v2.types.custom_vocabulary_status

        out["custom_vocabulary_status"] = (
            capo_lex_models_v2.types.custom_vocabulary_status.deserialize_json(
                data["customVocabularyStatus"]
            )
        )
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
    return out
