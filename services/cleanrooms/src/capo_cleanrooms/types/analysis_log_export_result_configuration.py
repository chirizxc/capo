"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisLogExportResultConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_log_export_output_configuration


class AnalysisLogExportResultConfiguration(TypedDict, closed=True):
    output_configuration: "capo_cleanrooms.types.analysis_log_export_output_configuration.AnalysisLogExportOutputConfiguration"
    """<p>The configuration for analysis log export results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisLogExportResultConfiguration) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.analysis_log_export_output_configuration

    out["outputConfiguration"] = (
        capo_cleanrooms.types.analysis_log_export_output_configuration.serialize_json(
            value["output_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> AnalysisLogExportResultConfiguration:
    out: AnalysisLogExportResultConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("outputConfiguration") is not None:
        import capo_cleanrooms.types.analysis_log_export_output_configuration

        out["output_configuration"] = (
            capo_cleanrooms.types.analysis_log_export_output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "AnalysisLogExportResultConfiguration.output_configuration required"
        )
    return out
