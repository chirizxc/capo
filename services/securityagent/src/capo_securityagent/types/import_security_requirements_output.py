"""Generated from Smithy shape ``com.amazonaws.securityagent#ImportSecurityRequirementsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.security_requirement_pack_id
    import capo_securityagent.types.security_requirement_pack_import_status


class ImportSecurityRequirementsOutput(TypedDict, closed=True):
    pack_id: "capo_securityagent.types.security_requirement_pack_id.SecurityRequirementPackId"
    """<p>The unique identifier of the security requirement pack.</p>"""
    import_status: "capo_securityagent.types.security_requirement_pack_import_status.SecurityRequirementPackImportStatus"
    """<p>The status of the import workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportSecurityRequirementsOutput) -> dict:
    out: dict = {}
    out["packId"] = value["pack_id"]
    import capo_securityagent.types.security_requirement_pack_import_status

    out["importStatus"] = (
        capo_securityagent.types.security_requirement_pack_import_status.serialize_json(
            value["import_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> ImportSecurityRequirementsOutput:
    out: ImportSecurityRequirementsOutput = {}  # type: ignore[typeddict-item]
    if data.get("packId") is not None:
        out["pack_id"] = data["packId"]
    else:
        raise DeserializationError("ImportSecurityRequirementsOutput.pack_id required")
    if data.get("importStatus") is not None:
        import capo_securityagent.types.security_requirement_pack_import_status

        out["import_status"] = (
            capo_securityagent.types.security_requirement_pack_import_status.deserialize_json(
                data["importStatus"]
            )
        )
    else:
        raise DeserializationError(
            "ImportSecurityRequirementsOutput.import_status required"
        )
    return out
