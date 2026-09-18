"""Generated from Smithy shape ``com.amazonaws.mediaconnect#TransportStreamProgram``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_transport_stream


class TransportStreamProgram(TypedDict, closed=True):
    pcr_pid: NotRequired["int"]
    """<p> The Program Clock Reference (PCR) Packet ID (PID) as it is reported in the Program Association Table.</p>"""
    program_name: NotRequired["str"]
    """<p> The program name as it is reported in the Program Association Table.</p>"""
    program_number: NotRequired["int"]
    """<p> The program number as it is reported in the Program Association Table.</p>"""
    program_pid: NotRequired["int"]
    """<p> The program Packet ID (PID) as it is reported in the Program Association Table.</p>"""
    streams: NotRequired[
        "capo_mediaconnect.types.__list_of_transport_stream.__listOfTransportStream"
    ]
    """<p> The list of elementary transport streams in the program. The list includes video, audio, and data streams.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransportStreamProgram) -> dict:
    out: dict = {}
    if "pcr_pid" in value:
        out["pcrPid"] = value["pcr_pid"]
    if "program_name" in value:
        out["programName"] = value["program_name"]
    if "program_number" in value:
        out["programNumber"] = value["program_number"]
    if "program_pid" in value:
        out["programPid"] = value["program_pid"]
    if "streams" in value:
        import capo_mediaconnect.types.__list_of_transport_stream

        out["streams"] = (
            capo_mediaconnect.types.__list_of_transport_stream.serialize_json(
                value["streams"]
            )
        )
    return out


def deserialize_json(data: dict) -> TransportStreamProgram:
    out: TransportStreamProgram = {}  # type: ignore[typeddict-item]
    if data.get("pcrPid") is not None:
        out["pcr_pid"] = data["pcrPid"]
    if data.get("programName") is not None:
        out["program_name"] = data["programName"]
    if data.get("programNumber") is not None:
        out["program_number"] = data["programNumber"]
    if data.get("programPid") is not None:
        out["program_pid"] = data["programPid"]
    if data.get("streams") is not None:
        import capo_mediaconnect.types.__list_of_transport_stream

        out["streams"] = (
            capo_mediaconnect.types.__list_of_transport_stream.deserialize_json(
                data["streams"]
            )
        )
    return out
