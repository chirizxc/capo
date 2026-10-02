"""Generated from Smithy shape ``com.amazonaws.wellarchitected#FieldErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.field_error_message
    import capo_wellarchitected.types.field_error_path

FieldErrors: TypeAlias = dict[
    "capo_wellarchitected.types.field_error_path.FieldErrorPath",
    "capo_wellarchitected.types.field_error_message.FieldErrorMessage",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FieldErrors) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> FieldErrors:
    out: FieldErrors = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
