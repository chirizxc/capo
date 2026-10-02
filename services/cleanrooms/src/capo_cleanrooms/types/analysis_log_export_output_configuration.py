"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisLogExportOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_log_export_s3_output_configuration


class AnalysisLogExportOutputConfiguration(TypedDict, closed=True):
    s3: "capo_cleanrooms.types.analysis_log_export_s3_output_configuration.AnalysisLogExportS3OutputConfiguration"
    """<p>Required configuration for an analysis log export with an <code>s3</code> output type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisLogExportOutputConfiguration) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.analysis_log_export_s3_output_configuration

    out["s3"] = (
        capo_cleanrooms.types.analysis_log_export_s3_output_configuration.serialize_json(
            value["s3"]
        )
    )
    return out


def deserialize_json(data: dict) -> AnalysisLogExportOutputConfiguration:
    out: AnalysisLogExportOutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("s3") is not None:
        import capo_cleanrooms.types.analysis_log_export_s3_output_configuration

        out["s3"] = (
            capo_cleanrooms.types.analysis_log_export_s3_output_configuration.deserialize_json(
                data["s3"]
            )
        )
    else:
        raise DeserializationError("AnalysisLogExportOutputConfiguration.s3 required")
    return out
