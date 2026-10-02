"""Generated from Smithy shape ``com.amazonaws.connect#AnalyticsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.language_configuration
    import capo_connect.types.redaction_configuration
    import capo_connect.types.rules_configuration
    import capo_connect.types.sentiment_configuration
    import capo_connect.types.summary_configuration


class AnalyticsConfiguration(TypedDict, closed=True):
    language_configuration: (
        "capo_connect.types.language_configuration.LanguageConfiguration"
    )
    """<p>The language configuration for conversational analytics.</p>"""
    redaction_configuration: (
        "capo_connect.types.redaction_configuration.RedactionConfiguration"
    )
    """<p>The redaction configuration for conversational analytics.</p>"""
    sentiment_configuration: (
        "capo_connect.types.sentiment_configuration.SentimentConfiguration"
    )
    """<p>The sentiment configuration for conversational analytics.</p>"""
    summary_configuration: (
        "capo_connect.types.summary_configuration.SummaryConfiguration"
    )
    """<p>The summary configuration for conversational analytics.</p>"""
    rules_configuration: "capo_connect.types.rules_configuration.RulesConfiguration"
    """<p>The rules configuration for conversational analytics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsConfiguration) -> dict:
    out: dict = {}
    import capo_connect.types.language_configuration

    out["LanguageConfiguration"] = (
        capo_connect.types.language_configuration.serialize_json(
            value["language_configuration"]
        )
    )
    import capo_connect.types.redaction_configuration

    out["RedactionConfiguration"] = (
        capo_connect.types.redaction_configuration.serialize_json(
            value["redaction_configuration"]
        )
    )
    import capo_connect.types.sentiment_configuration

    out["SentimentConfiguration"] = (
        capo_connect.types.sentiment_configuration.serialize_json(
            value["sentiment_configuration"]
        )
    )
    import capo_connect.types.summary_configuration

    out["SummaryConfiguration"] = (
        capo_connect.types.summary_configuration.serialize_json(
            value["summary_configuration"]
        )
    )
    import capo_connect.types.rules_configuration

    out["RulesConfiguration"] = capo_connect.types.rules_configuration.serialize_json(
        value["rules_configuration"]
    )
    return out


def deserialize_json(data: dict) -> AnalyticsConfiguration:
    out: AnalyticsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("LanguageConfiguration") is not None:
        import capo_connect.types.language_configuration

        out["language_configuration"] = (
            capo_connect.types.language_configuration.deserialize_json(
                data["LanguageConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "AnalyticsConfiguration.language_configuration required"
        )
    if data.get("RedactionConfiguration") is not None:
        import capo_connect.types.redaction_configuration

        out["redaction_configuration"] = (
            capo_connect.types.redaction_configuration.deserialize_json(
                data["RedactionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "AnalyticsConfiguration.redaction_configuration required"
        )
    if data.get("SentimentConfiguration") is not None:
        import capo_connect.types.sentiment_configuration

        out["sentiment_configuration"] = (
            capo_connect.types.sentiment_configuration.deserialize_json(
                data["SentimentConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "AnalyticsConfiguration.sentiment_configuration required"
        )
    if data.get("SummaryConfiguration") is not None:
        import capo_connect.types.summary_configuration

        out["summary_configuration"] = (
            capo_connect.types.summary_configuration.deserialize_json(
                data["SummaryConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "AnalyticsConfiguration.summary_configuration required"
        )
    if data.get("RulesConfiguration") is not None:
        import capo_connect.types.rules_configuration

        out["rules_configuration"] = (
            capo_connect.types.rules_configuration.deserialize_json(
                data["RulesConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "AnalyticsConfiguration.rules_configuration required"
        )
    return out
