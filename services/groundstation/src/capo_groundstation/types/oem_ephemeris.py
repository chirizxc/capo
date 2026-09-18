"""Generated from Smithy shape ``com.amazonaws.groundstation#OEMEphemeris``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.s3_object
    import capo_groundstation.types.unbounded_string


class OEMEphemeris(TypedDict, closed=True):
    s3_object: NotRequired["capo_groundstation.types.s3_object.S3Object"]
    """<p>The Amazon S3 object that contains the ephemeris data.</p>"""
    oem_data: NotRequired["capo_groundstation.types.unbounded_string.UnboundedString"]
    """<p>OEM data that you provide directly instead of using an Amazon S3 object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OEMEphemeris) -> dict:
    out: dict = {}
    if "s3_object" in value:
        import capo_groundstation.types.s3_object

        out["s3Object"] = capo_groundstation.types.s3_object.serialize_json(
            value["s3_object"]
        )
    if "oem_data" in value:
        out["oemData"] = value["oem_data"]
    return out


def deserialize_json(data: dict) -> OEMEphemeris:
    out: OEMEphemeris = {}  # type: ignore[typeddict-item]
    if data.get("s3Object") is not None:
        import capo_groundstation.types.s3_object

        out["s3_object"] = capo_groundstation.types.s3_object.deserialize_json(
            data["s3Object"]
        )
    if data.get("oemData") is not None:
        out["oem_data"] = data["oemData"]
    return out
