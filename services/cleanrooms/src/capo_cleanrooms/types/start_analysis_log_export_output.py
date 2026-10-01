"""Generated from Smithy shape ``com.amazonaws.cleanrooms#StartAnalysisLogExportOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_log_export


class StartAnalysisLogExportOutput(TypedDict, closed=True):
    analysis_log_export: "capo_cleanrooms.types.analysis_log_export.AnalysisLogExport"
    """<p>The analysis log export that was started. The <code>status</code> is <code>IN_PROGRESS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAnalysisLogExportOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.analysis_log_export

    out["analysisLogExport"] = capo_cleanrooms.types.analysis_log_export.serialize_json(
        value["analysis_log_export"]
    )
    return out


def deserialize_json(data: dict) -> StartAnalysisLogExportOutput:
    out: StartAnalysisLogExportOutput = {}  # type: ignore[typeddict-item]
    if data.get("analysisLogExport") is not None:
        import capo_cleanrooms.types.analysis_log_export

        out["analysis_log_export"] = (
            capo_cleanrooms.types.analysis_log_export.deserialize_json(
                data["analysisLogExport"]
            )
        )
    else:
        raise DeserializationError(
            "StartAnalysisLogExportOutput.analysis_log_export required"
        )
    return out
