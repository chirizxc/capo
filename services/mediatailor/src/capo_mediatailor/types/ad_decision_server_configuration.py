"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdDecisionServerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.http_request
    import capo_mediatailor.types.vast_response


class AdDecisionServerConfiguration(TypedDict, closed=True):
    http_request: NotRequired["capo_mediatailor.types.http_request.HttpRequest"]
    """<p>The HTTP request configuration parameters for the ad decision server.</p>"""
    vast_response: NotRequired["capo_mediatailor.types.vast_response.VastResponse"]
    """<p>The settings that control how MediaTailor processes VAST responses from the ad decision server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdDecisionServerConfiguration) -> dict:
    out: dict = {}
    if "http_request" in value:
        import capo_mediatailor.types.http_request

        out["HttpRequest"] = capo_mediatailor.types.http_request.serialize_json(
            value["http_request"]
        )
    if "vast_response" in value:
        import capo_mediatailor.types.vast_response

        out["VastResponse"] = capo_mediatailor.types.vast_response.serialize_json(
            value["vast_response"]
        )
    return out


def deserialize_json(data: dict) -> AdDecisionServerConfiguration:
    out: AdDecisionServerConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("HttpRequest") is not None:
        import capo_mediatailor.types.http_request

        out["http_request"] = capo_mediatailor.types.http_request.deserialize_json(
            data["HttpRequest"]
        )
    if data.get("VastResponse") is not None:
        import capo_mediatailor.types.vast_response

        out["vast_response"] = capo_mediatailor.types.vast_response.deserialize_json(
            data["VastResponse"]
        )
    return out
