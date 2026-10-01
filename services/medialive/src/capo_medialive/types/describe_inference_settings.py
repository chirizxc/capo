"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeInferenceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_audio_feed_input
    import capo_medialive.types.__list_of_enrichment_method
    import capo_medialive.types.__string


class DescribeInferenceSettings(TypedDict, closed=True):
    feed_arn: NotRequired["capo_medialive.types.__string.__string"]
    """The ARN of the feed resource that is associated with this channel. The feed is a resource in the Elemental Inference service."""
    audio_feed_inputs: NotRequired[
        "capo_medialive.types.__list_of_audio_feed_input.__listOfAudioFeedInput"
    ]
    """A list of audio feed inputs that map audio selectors in the channel to feed inputs on the associated Elemental Inference feed."""
    enrichment_methods: NotRequired[
        "capo_medialive.types.__list_of_enrichment_method.__listOfEnrichmentMethod"
    ]
    """The set of Contextual Metadata Enrichment methods enabled for this channel. Each method represents a specific way the channel uses the inference feed to augment its output with contextual metadata."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInferenceSettings) -> dict:
    out: dict = {}
    if "feed_arn" in value:
        out["feedArn"] = value["feed_arn"]
    if "audio_feed_inputs" in value:
        import capo_medialive.types.__list_of_audio_feed_input

        out["audioFeedInputs"] = (
            capo_medialive.types.__list_of_audio_feed_input.serialize_json(
                value["audio_feed_inputs"]
            )
        )
    if "enrichment_methods" in value:
        import capo_medialive.types.__list_of_enrichment_method

        out["enrichmentMethods"] = (
            capo_medialive.types.__list_of_enrichment_method.serialize_json(
                value["enrichment_methods"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeInferenceSettings:
    out: DescribeInferenceSettings = {}  # type: ignore[typeddict-item]
    if data.get("feedArn") is not None:
        out["feed_arn"] = data["feedArn"]
    if data.get("audioFeedInputs") is not None:
        import capo_medialive.types.__list_of_audio_feed_input

        out["audio_feed_inputs"] = (
            capo_medialive.types.__list_of_audio_feed_input.deserialize_json(
                data["audioFeedInputs"]
            )
        )
    if data.get("enrichmentMethods") is not None:
        import capo_medialive.types.__list_of_enrichment_method

        out["enrichment_methods"] = (
            capo_medialive.types.__list_of_enrichment_method.deserialize_json(
                data["enrichmentMethods"]
            )
        )
    return out
