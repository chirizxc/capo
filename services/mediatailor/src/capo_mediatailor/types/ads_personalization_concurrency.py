"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdsPersonalizationConcurrency``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__boolean
    import capo_mediatailor.types.__integer


class AdsPersonalizationConcurrency(TypedDict, closed=True):
    max_concurrent_ads_requests: NotRequired[
        "capo_mediatailor.types.__integer.__integer"
    ]
    """<p>The maximum number of simultaneous requests that MediaTailor makes to the ad decision server per manifest request. The default is 1.</p>"""
    enable_vod_vast_parallelization: NotRequired[
        "capo_mediatailor.types.__boolean.__boolean"
    ]
    """<p>Enables parallel processing of ad decision server requests in VOD workflows when the ADS returns VAST responses. The default is false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdsPersonalizationConcurrency) -> dict:
    out: dict = {}
    if "max_concurrent_ads_requests" in value:
        out["MaxConcurrentAdsRequests"] = value["max_concurrent_ads_requests"]
    if "enable_vod_vast_parallelization" in value:
        out["EnableVodVastParallelization"] = value["enable_vod_vast_parallelization"]
    return out


def deserialize_json(data: dict) -> AdsPersonalizationConcurrency:
    out: AdsPersonalizationConcurrency = {}  # type: ignore[typeddict-item]
    if data.get("MaxConcurrentAdsRequests") is not None:
        out["max_concurrent_ads_requests"] = data["MaxConcurrentAdsRequests"]
    if data.get("EnableVodVastParallelization") is not None:
        out["enable_vod_vast_parallelization"] = data["EnableVodVastParallelization"]
    return out
