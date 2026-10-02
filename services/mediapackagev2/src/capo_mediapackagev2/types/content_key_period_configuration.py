"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ContentKeyPeriodConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.content_key_period_timing


class ContentKeyPeriodConfiguration(TypedDict, closed=True):
    content_key_period_timing: NotRequired[
        "capo_mediapackagev2.types.content_key_period_timing.ContentKeyPeriodTiming"
    ]
    """<p>Specifies what timing information MediaPackage signals in the <code>ContentKeyPeriod</code> to your DRM key provider. If you don't specify a value, the default is <code>INDEX_ONLY</code>. Signaling start and end times (<code>START_END_ONLY</code> or <code>INDEX_WITH_START_END</code>) also requires key rotation to be enabled.</p> <p>The allowed values are:</p> <ul> <li> <p> <code>INDEX_ONLY</code> - Signals only the content key index. This is the default and matches the current behavior. It's supported for both SPEKE Version 2.0 and 2.1.</p> </li> <li> <p> <code>START_END_ONLY</code> - Signals only the start and end times the key is used for. Requires <code>SpekeVersion</code> <code>V2_1</code>.</p> </li> <li> <p> <code>INDEX_WITH_START_END</code> - Signals both the content key index and the start and end times the key is used for. Requires <code>SpekeVersion</code> <code>V2_1</code>.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentKeyPeriodConfiguration) -> dict:
    out: dict = {}
    if "content_key_period_timing" in value:
        import capo_mediapackagev2.types.content_key_period_timing

        out["ContentKeyPeriodTiming"] = (
            capo_mediapackagev2.types.content_key_period_timing.serialize_json(
                value["content_key_period_timing"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContentKeyPeriodConfiguration:
    out: ContentKeyPeriodConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ContentKeyPeriodTiming") is not None:
        import capo_mediapackagev2.types.content_key_period_timing

        out["content_key_period_timing"] = (
            capo_mediapackagev2.types.content_key_period_timing.deserialize_json(
                data["ContentKeyPeriodTiming"]
            )
        )
    return out
