"""Generated from Smithy shape ``com.amazonaws.iotsitewise#FileFormat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.annotation
    import capo_iotsitewise.types.csv
    import capo_iotsitewise.types.mp4
    import capo_iotsitewise.types.parquet


class FileFormat(TypedDict, closed=True):
    csv: NotRequired["capo_iotsitewise.types.csv.Csv"]
    """<p>The file is in .CSV format.</p>"""
    parquet: NotRequired["capo_iotsitewise.types.parquet.Parquet"]
    """<p>The file is in parquet format.</p>"""
    mp4: NotRequired["capo_iotsitewise.types.mp4.Mp4"]
    """<p>The MP4 format configuration.</p>"""
    annotation: NotRequired["capo_iotsitewise.types.annotation.Annotation"]
    """<p>The annotation format configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileFormat) -> dict:
    out: dict = {}
    if "csv" in value:
        import capo_iotsitewise.types.csv

        out["csv"] = capo_iotsitewise.types.csv.serialize_json(value["csv"])
    if "parquet" in value:
        import capo_iotsitewise.types.parquet

        out["parquet"] = capo_iotsitewise.types.parquet.serialize_json(value["parquet"])
    if "mp4" in value:
        import capo_iotsitewise.types.mp4

        out["mp4"] = capo_iotsitewise.types.mp4.serialize_json(value["mp4"])
    if "annotation" in value:
        import capo_iotsitewise.types.annotation

        out["annotation"] = capo_iotsitewise.types.annotation.serialize_json(
            value["annotation"]
        )
    return out


def deserialize_json(data: dict) -> FileFormat:
    out: FileFormat = {}  # type: ignore[typeddict-item]
    if data.get("csv") is not None:
        import capo_iotsitewise.types.csv

        out["csv"] = capo_iotsitewise.types.csv.deserialize_json(data["csv"])
    if data.get("parquet") is not None:
        import capo_iotsitewise.types.parquet

        out["parquet"] = capo_iotsitewise.types.parquet.deserialize_json(
            data["parquet"]
        )
    if data.get("mp4") is not None:
        import capo_iotsitewise.types.mp4

        out["mp4"] = capo_iotsitewise.types.mp4.deserialize_json(data["mp4"])
    if data.get("annotation") is not None:
        import capo_iotsitewise.types.annotation

        out["annotation"] = capo_iotsitewise.types.annotation.deserialize_json(
            data["annotation"]
        )
    return out
