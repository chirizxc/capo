"""Generated from Smithy shape ``com.amazonaws.mediatailor#HlsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__string


class HlsConfiguration(TypedDict, closed=True):
    manifest_endpoint_prefix: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The URL that MediaTailor generates to initiate a playback session for devices that support Apple HLS. The session uses server-side reporting.</p>"""
    dual_stack_manifest_endpoint_prefix: NotRequired[
        "capo_mediatailor.types.__string.__string"
    ]
    """<p>The dual-stack (IPv4 and IPv6) URL that MediaTailor generates to initiate a playback session for devices that support Apple HLS. The session uses server-side reporting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HlsConfiguration) -> dict:
    out: dict = {}
    if "manifest_endpoint_prefix" in value:
        out["ManifestEndpointPrefix"] = value["manifest_endpoint_prefix"]
    if "dual_stack_manifest_endpoint_prefix" in value:
        out["DualStackManifestEndpointPrefix"] = value[
            "dual_stack_manifest_endpoint_prefix"
        ]
    return out


def deserialize_json(data: dict) -> HlsConfiguration:
    out: HlsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ManifestEndpointPrefix") is not None:
        out["manifest_endpoint_prefix"] = data["ManifestEndpointPrefix"]
    if data.get("DualStackManifestEndpointPrefix") is not None:
        out["dual_stack_manifest_endpoint_prefix"] = data[
            "DualStackManifestEndpointPrefix"
        ]
    return out
