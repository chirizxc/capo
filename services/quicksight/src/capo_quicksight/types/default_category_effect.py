"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultCategoryEffect``."""

from typing import Literal, TypeAlias, cast

"""<p>The default effect that Amazon Quick applies to capabilities in a governed category when you do not explicitly list those capabilities in <code>Capabilities</code>. Valid values:</p> <ul> <li> <p> <code>DENY_BY_DEFAULT</code> – Amazon Quick denies any capability access in the given category that the profile does not explicitly set to <code>ALLOW</code>.</p> </li> </ul>"""
DefaultCategoryEffect: TypeAlias = Literal["DENY_BY_DEFAULT",]


# --- restJson1 ser/de ---
def serialize_json(value: DefaultCategoryEffect) -> str:
    return value


def deserialize_json(data: str) -> DefaultCategoryEffect:
    return cast(DefaultCategoryEffect, data)
