"""Generated from Smithy shape ``com.amazonaws.invoicing#ProcurementPortalEnv``."""

from typing import Literal, TypeAlias, cast

"""<p>The environment of a procurement portal supplier. <code>PROD</code> indicates the production environment. <code>TEST</code> indicates the sandbox or test environment.</p>"""
ProcurementPortalEnv: TypeAlias = Literal[
    "PROD",
    "TEST",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProcurementPortalEnv) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProcurementPortalEnv:
    return cast(ProcurementPortalEnv, data)
