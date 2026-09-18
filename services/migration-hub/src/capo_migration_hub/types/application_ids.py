"""Generated from Smithy shape ``com.amazonaws.migrationhub#ApplicationIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migration_hub.types.application_id

ApplicationIds: TypeAlias = list[
    "capo_migration_hub.types.application_id.ApplicationId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ApplicationIds:
    return [item for item in data if item is not None]
