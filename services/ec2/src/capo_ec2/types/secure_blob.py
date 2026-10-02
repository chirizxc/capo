"""Generated from Smithy shape ``com.amazonaws.ec2#SecureBlob``."""

import base64
from typing import TypeAlias

from capo_ec2._protocol.xml import Element

SecureBlob: TypeAlias = bytes


# --- ec2Query ser/de ---
def to_ec2_query_text(value: SecureBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def from_ec2_query_text(text: str) -> SecureBlob:
    return base64.b64decode(text)


def serialize_ec2_query(
    value: SecureBlob, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SecureBlob:
    return from_ec2_query_text(el.text or "")
