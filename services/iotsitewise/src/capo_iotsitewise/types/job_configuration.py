"""Generated from Smithy shape ``com.amazonaws.iotsitewise#JobConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.file_format


class JobConfiguration(TypedDict, closed=True):
    file_format: NotRequired["capo_iotsitewise.types.file_format.FileFormat"]
    """<p>The file format of the data in S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobConfiguration) -> dict:
    out: dict = {}
    if "file_format" in value:
        import capo_iotsitewise.types.file_format

        out["fileFormat"] = capo_iotsitewise.types.file_format.serialize_json(
            value["file_format"]
        )
    return out


def deserialize_json(data: dict) -> JobConfiguration:
    out: JobConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("fileFormat") is not None:
        import capo_iotsitewise.types.file_format

        out["file_format"] = capo_iotsitewise.types.file_format.deserialize_json(
            data["fileFormat"]
        )
    return out
