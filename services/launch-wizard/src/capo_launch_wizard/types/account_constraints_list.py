"""Generated from Smithy shape ``com.amazonaws.launchwizard#AccountConstraintsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_launch_wizard.types.account_constraint

AccountConstraintsList: TypeAlias = list[
    "capo_launch_wizard.types.account_constraint.AccountConstraint"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountConstraintsList) -> list:
    import capo_launch_wizard.types.account_constraint

    out: list = []
    for item in value:
        out.append(capo_launch_wizard.types.account_constraint.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountConstraintsList:
    import capo_launch_wizard.types.account_constraint

    out: AccountConstraintsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_launch_wizard.types.account_constraint.deserialize_json(item))
    return out
