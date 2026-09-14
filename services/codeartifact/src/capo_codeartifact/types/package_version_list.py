"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeartifact.types.package_version

PackageVersionList: TypeAlias = list[
    "capo_codeartifact.types.package_version.PackageVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionList) -> list:
    return list(value)


def deserialize_json(data: list) -> PackageVersionList:
    return [item for item in data if item is not None]
