"""Generated from Smithy shape ``com.amazonaws.batch#CancelJobsErrorDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.cancel_jobs_error_detail

CancelJobsErrorDetailList: TypeAlias = list[
    "capo_batch.types.cancel_jobs_error_detail.CancelJobsErrorDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobsErrorDetailList) -> list:
    import capo_batch.types.cancel_jobs_error_detail

    out: list = []
    for item in value:
        out.append(capo_batch.types.cancel_jobs_error_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> CancelJobsErrorDetailList:
    import capo_batch.types.cancel_jobs_error_detail

    out: CancelJobsErrorDetailList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_batch.types.cancel_jobs_error_detail.deserialize_json(item))
    return out
