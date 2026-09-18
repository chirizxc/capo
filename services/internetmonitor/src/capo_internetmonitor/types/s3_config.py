"""Generated from Smithy shape ``com.amazonaws.internetmonitor#S3Config``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.log_delivery_status


class S3Config(TypedDict, closed=True):
    bucket_name: NotRequired["str"]
    """<p>The Amazon S3 bucket name.</p>"""
    bucket_prefix: NotRequired["str"]
    """<p>The Amazon S3 bucket prefix.</p>"""
    log_delivery_status: NotRequired[
        "capo_internetmonitor.types.log_delivery_status.LogDeliveryStatus"
    ]
    """<p>The status of publishing Internet Monitor internet measurements to an Amazon S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Config) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["BucketName"] = value["bucket_name"]
    if "bucket_prefix" in value:
        out["BucketPrefix"] = value["bucket_prefix"]
    if "log_delivery_status" in value:
        out["LogDeliveryStatus"] = value["log_delivery_status"]
    return out


def deserialize_json(data: dict) -> S3Config:
    out: S3Config = {}  # type: ignore[typeddict-item]
    if data.get("BucketName") is not None:
        out["bucket_name"] = data["BucketName"]
    if data.get("BucketPrefix") is not None:
        out["bucket_prefix"] = data["BucketPrefix"]
    if data.get("LogDeliveryStatus") is not None:
        out["log_delivery_status"] = data["LogDeliveryStatus"]
    return out
