"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ExportStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bcm_data_exports.types.execution_status_reason
    import capo_bcm_data_exports.types.export_status_code


class ExportStatus(TypedDict, closed=True):
    status_code: NotRequired[
        "capo_bcm_data_exports.types.export_status_code.ExportStatusCode"
    ]
    """<p>The status code for the request.</p>"""
    status_reason: NotRequired[
        "capo_bcm_data_exports.types.execution_status_reason.ExecutionStatusReason"
    ]
    """<p>The description for the status code.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the export was created.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the export was updated.</p>"""
    last_refreshed_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the export was last generated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportStatus) -> dict:
    out: dict = {}
    if "status_code" in value:
        import capo_bcm_data_exports.types.export_status_code

        out["StatusCode"] = (
            capo_bcm_data_exports.types.export_status_code.serialize_aws_json_1_1(
                value["status_code"]
            )
        )
    if "status_reason" in value:
        import capo_bcm_data_exports.types.execution_status_reason

        out["StatusReason"] = (
            capo_bcm_data_exports.types.execution_status_reason.serialize_aws_json_1_1(
                value["status_reason"]
            )
        )
    if "created_at" in value:
        import capo_bcm_data_exports._protocol.serialize

        out["CreatedAt"] = capo_bcm_data_exports._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_bcm_data_exports._protocol.serialize

        out["LastUpdatedAt"] = capo_bcm_data_exports._protocol.serialize.fmt_date_time(
            value["last_updated_at"]
        )
    if "last_refreshed_at" in value:
        import capo_bcm_data_exports._protocol.serialize

        out["LastRefreshedAt"] = (
            capo_bcm_data_exports._protocol.serialize.fmt_date_time(
                value["last_refreshed_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportStatus:
    out: ExportStatus = {}  # type: ignore[typeddict-item]
    if data.get("StatusCode") is not None:
        import capo_bcm_data_exports.types.export_status_code

        out["status_code"] = (
            capo_bcm_data_exports.types.export_status_code.deserialize_aws_json_1_1(
                data["StatusCode"]
            )
        )
    if data.get("StatusReason") is not None:
        import capo_bcm_data_exports.types.execution_status_reason

        out["status_reason"] = (
            capo_bcm_data_exports.types.execution_status_reason.deserialize_aws_json_1_1(
                data["StatusReason"]
            )
        )
    if data.get("CreatedAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["CreatedAt"].replace("Z", "+00:00")
        )
    if data.get("LastUpdatedAt") is not None:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromisoformat(
            data["LastUpdatedAt"].replace("Z", "+00:00")
        )
    if data.get("LastRefreshedAt") is not None:
        import datetime

        out["last_refreshed_at"] = datetime.datetime.fromisoformat(
            data["LastRefreshedAt"].replace("Z", "+00:00")
        )
    return out
