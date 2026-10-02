"""Generated from Smithy shape ``com.amazonaws.backup#DeleteBackupAccessPointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup.types.access_point_arn


class DeleteBackupAccessPointInput(TypedDict, closed=True):
    access_point_arn: "capo_backup.types.access_point_arn.AccessPointArn"
    """<p>The Amazon Resource Name (ARN) of the backup access point to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBackupAccessPointInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBackupAccessPointInput:
    out: DeleteBackupAccessPointInput = {}  # type: ignore[typeddict-item]
    return out
