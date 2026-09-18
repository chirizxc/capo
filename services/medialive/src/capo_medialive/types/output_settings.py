"""Generated from Smithy shape ``com.amazonaws.medialive#OutputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.archive_output_settings
    import capo_medialive.types.cmaf_ingest_output_settings
    import capo_medialive.types.frame_capture_output_settings
    import capo_medialive.types.hls_output_settings
    import capo_medialive.types.media_connect_router_output_settings
    import capo_medialive.types.media_package_output_settings
    import capo_medialive.types.ms_smooth_output_settings
    import capo_medialive.types.multiplex_output_settings
    import capo_medialive.types.rtmp_output_settings
    import capo_medialive.types.srt_output_settings
    import capo_medialive.types.udp_output_settings


class OutputSettings(TypedDict, closed=True):
    archive_output_settings: NotRequired[
        "capo_medialive.types.archive_output_settings.ArchiveOutputSettings"
    ]
    frame_capture_output_settings: NotRequired[
        "capo_medialive.types.frame_capture_output_settings.FrameCaptureOutputSettings"
    ]
    hls_output_settings: NotRequired[
        "capo_medialive.types.hls_output_settings.HlsOutputSettings"
    ]
    media_package_output_settings: NotRequired[
        "capo_medialive.types.media_package_output_settings.MediaPackageOutputSettings"
    ]
    ms_smooth_output_settings: NotRequired[
        "capo_medialive.types.ms_smooth_output_settings.MsSmoothOutputSettings"
    ]
    multiplex_output_settings: NotRequired[
        "capo_medialive.types.multiplex_output_settings.MultiplexOutputSettings"
    ]
    rtmp_output_settings: NotRequired[
        "capo_medialive.types.rtmp_output_settings.RtmpOutputSettings"
    ]
    udp_output_settings: NotRequired[
        "capo_medialive.types.udp_output_settings.UdpOutputSettings"
    ]
    cmaf_ingest_output_settings: NotRequired[
        "capo_medialive.types.cmaf_ingest_output_settings.CmafIngestOutputSettings"
    ]
    srt_output_settings: NotRequired[
        "capo_medialive.types.srt_output_settings.SrtOutputSettings"
    ]
    media_connect_router_output_settings: NotRequired[
        "capo_medialive.types.media_connect_router_output_settings.MediaConnectRouterOutputSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: OutputSettings) -> dict:
    out: dict = {}
    if "archive_output_settings" in value:
        import capo_medialive.types.archive_output_settings

        out["archiveOutputSettings"] = (
            capo_medialive.types.archive_output_settings.serialize_json(
                value["archive_output_settings"]
            )
        )
    if "frame_capture_output_settings" in value:
        import capo_medialive.types.frame_capture_output_settings

        out["frameCaptureOutputSettings"] = (
            capo_medialive.types.frame_capture_output_settings.serialize_json(
                value["frame_capture_output_settings"]
            )
        )
    if "hls_output_settings" in value:
        import capo_medialive.types.hls_output_settings

        out["hlsOutputSettings"] = (
            capo_medialive.types.hls_output_settings.serialize_json(
                value["hls_output_settings"]
            )
        )
    if "media_package_output_settings" in value:
        import capo_medialive.types.media_package_output_settings

        out["mediaPackageOutputSettings"] = (
            capo_medialive.types.media_package_output_settings.serialize_json(
                value["media_package_output_settings"]
            )
        )
    if "ms_smooth_output_settings" in value:
        import capo_medialive.types.ms_smooth_output_settings

        out["msSmoothOutputSettings"] = (
            capo_medialive.types.ms_smooth_output_settings.serialize_json(
                value["ms_smooth_output_settings"]
            )
        )
    if "multiplex_output_settings" in value:
        import capo_medialive.types.multiplex_output_settings

        out["multiplexOutputSettings"] = (
            capo_medialive.types.multiplex_output_settings.serialize_json(
                value["multiplex_output_settings"]
            )
        )
    if "rtmp_output_settings" in value:
        import capo_medialive.types.rtmp_output_settings

        out["rtmpOutputSettings"] = (
            capo_medialive.types.rtmp_output_settings.serialize_json(
                value["rtmp_output_settings"]
            )
        )
    if "udp_output_settings" in value:
        import capo_medialive.types.udp_output_settings

        out["udpOutputSettings"] = (
            capo_medialive.types.udp_output_settings.serialize_json(
                value["udp_output_settings"]
            )
        )
    if "cmaf_ingest_output_settings" in value:
        import capo_medialive.types.cmaf_ingest_output_settings

        out["cmafIngestOutputSettings"] = (
            capo_medialive.types.cmaf_ingest_output_settings.serialize_json(
                value["cmaf_ingest_output_settings"]
            )
        )
    if "srt_output_settings" in value:
        import capo_medialive.types.srt_output_settings

        out["srtOutputSettings"] = (
            capo_medialive.types.srt_output_settings.serialize_json(
                value["srt_output_settings"]
            )
        )
    if "media_connect_router_output_settings" in value:
        import capo_medialive.types.media_connect_router_output_settings

        out["mediaConnectRouterOutputSettings"] = (
            capo_medialive.types.media_connect_router_output_settings.serialize_json(
                value["media_connect_router_output_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> OutputSettings:
    out: OutputSettings = {}  # type: ignore[typeddict-item]
    if data.get("archiveOutputSettings") is not None:
        import capo_medialive.types.archive_output_settings

        out["archive_output_settings"] = (
            capo_medialive.types.archive_output_settings.deserialize_json(
                data["archiveOutputSettings"]
            )
        )
    if data.get("frameCaptureOutputSettings") is not None:
        import capo_medialive.types.frame_capture_output_settings

        out["frame_capture_output_settings"] = (
            capo_medialive.types.frame_capture_output_settings.deserialize_json(
                data["frameCaptureOutputSettings"]
            )
        )
    if data.get("hlsOutputSettings") is not None:
        import capo_medialive.types.hls_output_settings

        out["hls_output_settings"] = (
            capo_medialive.types.hls_output_settings.deserialize_json(
                data["hlsOutputSettings"]
            )
        )
    if data.get("mediaPackageOutputSettings") is not None:
        import capo_medialive.types.media_package_output_settings

        out["media_package_output_settings"] = (
            capo_medialive.types.media_package_output_settings.deserialize_json(
                data["mediaPackageOutputSettings"]
            )
        )
    if data.get("msSmoothOutputSettings") is not None:
        import capo_medialive.types.ms_smooth_output_settings

        out["ms_smooth_output_settings"] = (
            capo_medialive.types.ms_smooth_output_settings.deserialize_json(
                data["msSmoothOutputSettings"]
            )
        )
    if data.get("multiplexOutputSettings") is not None:
        import capo_medialive.types.multiplex_output_settings

        out["multiplex_output_settings"] = (
            capo_medialive.types.multiplex_output_settings.deserialize_json(
                data["multiplexOutputSettings"]
            )
        )
    if data.get("rtmpOutputSettings") is not None:
        import capo_medialive.types.rtmp_output_settings

        out["rtmp_output_settings"] = (
            capo_medialive.types.rtmp_output_settings.deserialize_json(
                data["rtmpOutputSettings"]
            )
        )
    if data.get("udpOutputSettings") is not None:
        import capo_medialive.types.udp_output_settings

        out["udp_output_settings"] = (
            capo_medialive.types.udp_output_settings.deserialize_json(
                data["udpOutputSettings"]
            )
        )
    if data.get("cmafIngestOutputSettings") is not None:
        import capo_medialive.types.cmaf_ingest_output_settings

        out["cmaf_ingest_output_settings"] = (
            capo_medialive.types.cmaf_ingest_output_settings.deserialize_json(
                data["cmafIngestOutputSettings"]
            )
        )
    if data.get("srtOutputSettings") is not None:
        import capo_medialive.types.srt_output_settings

        out["srt_output_settings"] = (
            capo_medialive.types.srt_output_settings.deserialize_json(
                data["srtOutputSettings"]
            )
        )
    if data.get("mediaConnectRouterOutputSettings") is not None:
        import capo_medialive.types.media_connect_router_output_settings

        out["media_connect_router_output_settings"] = (
            capo_medialive.types.media_connect_router_output_settings.deserialize_json(
                data["mediaConnectRouterOutputSettings"]
            )
        )
    return out
