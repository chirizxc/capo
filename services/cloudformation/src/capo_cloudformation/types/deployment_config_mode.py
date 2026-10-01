"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeploymentConfigMode``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

DeploymentConfigMode: TypeAlias = Literal[
    "STANDARD",
    "EXPRESS",
]


# --- awsQuery ser/de ---
def to_query_text(value: DeploymentConfigMode) -> str:
    return value


def from_query_text(text: str) -> DeploymentConfigMode:
    return cast(DeploymentConfigMode, text)


def serialize_query(
    value: DeploymentConfigMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DeploymentConfigMode:
    return from_query_text(el.text or "")
