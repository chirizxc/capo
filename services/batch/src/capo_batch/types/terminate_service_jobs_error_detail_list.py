"""Generated from Smithy shape ``com.amazonaws.batch#TerminateServiceJobsErrorDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.terminate_service_jobs_error_detail

TerminateServiceJobsErrorDetailList: TypeAlias = list[
    "capo_batch.types.terminate_service_jobs_error_detail.TerminateServiceJobsErrorDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: TerminateServiceJobsErrorDetailList) -> list:
    import capo_batch.types.terminate_service_jobs_error_detail

    out: list = []
    for item in value:
        out.append(
            capo_batch.types.terminate_service_jobs_error_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TerminateServiceJobsErrorDetailList:
    import capo_batch.types.terminate_service_jobs_error_detail

    out: TerminateServiceJobsErrorDetailList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_batch.types.terminate_service_jobs_error_detail.deserialize_json(item)
        )
    return out
