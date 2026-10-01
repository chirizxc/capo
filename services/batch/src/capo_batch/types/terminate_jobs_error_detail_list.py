"""Generated from Smithy shape ``com.amazonaws.batch#TerminateJobsErrorDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.terminate_jobs_error_detail

TerminateJobsErrorDetailList: TypeAlias = list[
    "capo_batch.types.terminate_jobs_error_detail.TerminateJobsErrorDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: TerminateJobsErrorDetailList) -> list:
    import capo_batch.types.terminate_jobs_error_detail

    out: list = []
    for item in value:
        out.append(capo_batch.types.terminate_jobs_error_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> TerminateJobsErrorDetailList:
    import capo_batch.types.terminate_jobs_error_detail

    out: TerminateJobsErrorDetailList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_batch.types.terminate_jobs_error_detail.deserialize_json(item))
    return out
