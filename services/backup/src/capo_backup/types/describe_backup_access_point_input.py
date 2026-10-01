"""Generated from Smithy shape ``com.amazonaws.backup#DescribeBackupAccessPointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup.types.access_point_arn


class DescribeBackupAccessPointInput(TypedDict, closed=True):
    access_point_arn: "capo_backup.types.access_point_arn.AccessPointArn"
    """<p>The Amazon Resource Name (ARN) of the backup access point to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBackupAccessPointInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeBackupAccessPointInput:
    out: DescribeBackupAccessPointInput = {}  # type: ignore[typeddict-item]
    return out
