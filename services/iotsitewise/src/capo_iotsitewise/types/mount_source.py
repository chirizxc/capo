"""Generated from Smithy shape ``com.amazonaws.iotsitewise#MountSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.s3_access_point_source


class _MountSource_s3AccessPoint(TypedDict, closed=True):
    s3AccessPoint: "capo_iotsitewise.types.s3_access_point_source.S3AccessPointSource"


MountSource: TypeAlias = _MountSource_s3AccessPoint


# --- restJson1 ser/de ---
def serialize_json(value: MountSource) -> dict:
    if "s3AccessPoint" in value:
        import capo_iotsitewise.types.s3_access_point_source

        return {
            "s3AccessPoint": capo_iotsitewise.types.s3_access_point_source.serialize_json(
                value["s3AccessPoint"]
            )
        }
    else:
        raise SerializationError("MountSource: no variant present")


def deserialize_json(data: dict) -> MountSource:
    if data.get("s3AccessPoint") is not None:
        import capo_iotsitewise.types.s3_access_point_source

        return {
            "s3AccessPoint": capo_iotsitewise.types.s3_access_point_source.deserialize_json(
                data["s3AccessPoint"]
            )
        }
    else:
        raise DeserializationError("MountSource: no recognized variant key")
