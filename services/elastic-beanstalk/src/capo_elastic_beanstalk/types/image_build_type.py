"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ImageBuildType``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_beanstalk._protocol.xml import Element

ImageBuildType: TypeAlias = Literal[
    "docker",
    "buildpack",
]


# --- awsQuery ser/de ---
def to_query_text(value: ImageBuildType) -> str:
    return value


def from_query_text(text: str) -> ImageBuildType:
    return cast(ImageBuildType, text)


def serialize_query(
    value: ImageBuildType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ImageBuildType:
    return from_query_text(el.text or "")
