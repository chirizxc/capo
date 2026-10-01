"""Generated from Smithy shape ``com.amazonaws.s3control#S3AnnotationDirective``."""

from typing import Literal, TypeAlias, cast

from capo_s3_control._protocol.xml import Element, SubElement

S3AnnotationDirective: TypeAlias = Literal[
    "COPY",
    "EXCLUDE",
]


# --- restXml ser/de ---
def to_xml_text(value: S3AnnotationDirective) -> str:
    return value


def from_xml_text(text: str) -> S3AnnotationDirective:
    return cast(S3AnnotationDirective, text)


def serialize_xml(value: S3AnnotationDirective, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> S3AnnotationDirective:
    return from_xml_text(el.text or "")
