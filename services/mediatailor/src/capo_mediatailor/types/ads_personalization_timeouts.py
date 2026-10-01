"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdsPersonalizationTimeouts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__integer


class AdsPersonalizationTimeouts(TypedDict, closed=True):
    ads_request_timeout_milliseconds: NotRequired[
        "capo_mediatailor.types.__integer.__integer"
    ]
    """<p>The maximum time, in milliseconds, that MediaTailor waits for a single ad decision server response during live or VOD playback. The default is 3000.</p>"""
    live_maximum_ads_personalization_time_milliseconds: NotRequired[
        "capo_mediatailor.types.__integer.__integer"
    ]
    """<p>The maximum total time, in milliseconds, that MediaTailor spends on ad decision server activity for live manifests, including making requests, waiting for responses, and following VAST wrapper redirects. The default is 10000.</p>"""
    vod_maximum_ads_personalization_time_milliseconds: NotRequired[
        "capo_mediatailor.types.__integer.__integer"
    ]
    """<p>The maximum total time, in milliseconds, that MediaTailor spends on ad decision server activity for VOD manifests, including making requests, waiting for responses, and following VAST wrapper redirects. The default is 10000.</p>"""
    prefetch_ads_request_timeout_milliseconds: NotRequired[
        "capo_mediatailor.types.__integer.__integer"
    ]
    """<p>The maximum time, in milliseconds, that MediaTailor waits for a single ad decision server response during prefetch retrieval. If not set, the value of AdsRequestTimeoutMilliseconds is used.</p>"""
    prefetch_maximum_ads_personalization_time_milliseconds: NotRequired[
        "capo_mediatailor.types.__integer.__integer"
    ]
    """<p>The maximum total time, in milliseconds, that MediaTailor spends on ad decision server activity during prefetch retrieval, including making requests, waiting for responses, and following VAST wrapper redirects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdsPersonalizationTimeouts) -> dict:
    out: dict = {}
    if "ads_request_timeout_milliseconds" in value:
        out["AdsRequestTimeoutMilliseconds"] = value["ads_request_timeout_milliseconds"]
    if "live_maximum_ads_personalization_time_milliseconds" in value:
        out["LiveMaximumAdsPersonalizationTimeMilliseconds"] = value[
            "live_maximum_ads_personalization_time_milliseconds"
        ]
    if "vod_maximum_ads_personalization_time_milliseconds" in value:
        out["VodMaximumAdsPersonalizationTimeMilliseconds"] = value[
            "vod_maximum_ads_personalization_time_milliseconds"
        ]
    if "prefetch_ads_request_timeout_milliseconds" in value:
        out["PrefetchAdsRequestTimeoutMilliseconds"] = value[
            "prefetch_ads_request_timeout_milliseconds"
        ]
    if "prefetch_maximum_ads_personalization_time_milliseconds" in value:
        out["PrefetchMaximumAdsPersonalizationTimeMilliseconds"] = value[
            "prefetch_maximum_ads_personalization_time_milliseconds"
        ]
    return out


def deserialize_json(data: dict) -> AdsPersonalizationTimeouts:
    out: AdsPersonalizationTimeouts = {}  # type: ignore[typeddict-item]
    if data.get("AdsRequestTimeoutMilliseconds") is not None:
        out["ads_request_timeout_milliseconds"] = data["AdsRequestTimeoutMilliseconds"]
    if data.get("LiveMaximumAdsPersonalizationTimeMilliseconds") is not None:
        out["live_maximum_ads_personalization_time_milliseconds"] = data[
            "LiveMaximumAdsPersonalizationTimeMilliseconds"
        ]
    if data.get("VodMaximumAdsPersonalizationTimeMilliseconds") is not None:
        out["vod_maximum_ads_personalization_time_milliseconds"] = data[
            "VodMaximumAdsPersonalizationTimeMilliseconds"
        ]
    if data.get("PrefetchAdsRequestTimeoutMilliseconds") is not None:
        out["prefetch_ads_request_timeout_milliseconds"] = data[
            "PrefetchAdsRequestTimeoutMilliseconds"
        ]
    if data.get("PrefetchMaximumAdsPersonalizationTimeMilliseconds") is not None:
        out["prefetch_maximum_ads_personalization_time_milliseconds"] = data[
            "PrefetchMaximumAdsPersonalizationTimeMilliseconds"
        ]
    return out
