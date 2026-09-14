"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#RelationshipSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.account_id
    import capo_partnercentral_channel.types.arn
    import capo_partnercentral_channel.types.association_type
    import capo_partnercentral_channel.types.catalog
    import capo_partnercentral_channel.types.date_time
    import capo_partnercentral_channel.types.program_management_account_id
    import capo_partnercentral_channel.types.relationship_display_name
    import capo_partnercentral_channel.types.relationship_id
    import capo_partnercentral_channel.types.revision
    import capo_partnercentral_channel.types.sector


class RelationshipSummary(TypedDict, closed=True):
    arn: NotRequired["capo_partnercentral_channel.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the relationship.</p>"""
    id: NotRequired["capo_partnercentral_channel.types.relationship_id.RelationshipId"]
    """<p>The unique identifier of the relationship.</p>"""
    revision: NotRequired["capo_partnercentral_channel.types.revision.Revision"]
    """<p>The current revision number of the relationship.</p>"""
    catalog: NotRequired["capo_partnercentral_channel.types.catalog.Catalog"]
    """<p>The catalog identifier associated with the relationship.</p>"""
    association_type: NotRequired[
        "capo_partnercentral_channel.types.association_type.AssociationType"
    ]
    """<p>The type of association for the relationship.</p>"""
    program_management_account_id: NotRequired[
        "capo_partnercentral_channel.types.program_management_account_id.ProgramManagementAccountId"
    ]
    """<p>The identifier of the program management account.</p>"""
    associated_account_id: NotRequired[
        "capo_partnercentral_channel.types.account_id.AccountId"
    ]
    """<p>The AWS account ID associated in this relationship.</p>"""
    display_name: NotRequired[
        "capo_partnercentral_channel.types.relationship_display_name.RelationshipDisplayName"
    ]
    """<p>The display name of the relationship.</p>"""
    sector: NotRequired["capo_partnercentral_channel.types.sector.Sector"]
    """<p>The business sector for the relationship.</p>"""
    created_at: NotRequired["capo_partnercentral_channel.types.date_time.DateTime"]
    """<p>The timestamp when the relationship was created.</p>"""
    updated_at: NotRequired["capo_partnercentral_channel.types.date_time.DateTime"]
    """<p>The timestamp when the relationship was last updated.</p>"""
    start_date: NotRequired["capo_partnercentral_channel.types.date_time.DateTime"]
    """<p>The start date of the relationship.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RelationshipSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "catalog" in value:
        out["catalog"] = value["catalog"]
    if "association_type" in value:
        import capo_partnercentral_channel.types.association_type

        out["associationType"] = (
            capo_partnercentral_channel.types.association_type.serialize_aws_json_1_0(
                value["association_type"]
            )
        )
    if "program_management_account_id" in value:
        out["programManagementAccountId"] = value["program_management_account_id"]
    if "associated_account_id" in value:
        out["associatedAccountId"] = value["associated_account_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "sector" in value:
        import capo_partnercentral_channel.types.sector

        out["sector"] = capo_partnercentral_channel.types.sector.serialize_aws_json_1_0(
            value["sector"]
        )
    if "created_at" in value:
        import capo_partnercentral_channel.types.date_time

        out["createdAt"] = (
            capo_partnercentral_channel.types.date_time.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_partnercentral_channel.types.date_time

        out["updatedAt"] = (
            capo_partnercentral_channel.types.date_time.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    if "start_date" in value:
        import capo_partnercentral_channel.types.date_time

        out["startDate"] = (
            capo_partnercentral_channel.types.date_time.serialize_aws_json_1_0(
                value["start_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RelationshipSummary:
    out: RelationshipSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    if data.get("associationType") is not None:
        import capo_partnercentral_channel.types.association_type

        out["association_type"] = (
            capo_partnercentral_channel.types.association_type.deserialize_aws_json_1_0(
                data["associationType"]
            )
        )
    if data.get("programManagementAccountId") is not None:
        out["program_management_account_id"] = data["programManagementAccountId"]
    if data.get("associatedAccountId") is not None:
        out["associated_account_id"] = data["associatedAccountId"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("sector") is not None:
        import capo_partnercentral_channel.types.sector

        out["sector"] = (
            capo_partnercentral_channel.types.sector.deserialize_aws_json_1_0(
                data["sector"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_partnercentral_channel.types.date_time

        out["created_at"] = (
            capo_partnercentral_channel.types.date_time.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_partnercentral_channel.types.date_time

        out["updated_at"] = (
            capo_partnercentral_channel.types.date_time.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    if data.get("startDate") is not None:
        import capo_partnercentral_channel.types.date_time

        out["start_date"] = (
            capo_partnercentral_channel.types.date_time.deserialize_aws_json_1_0(
                data["startDate"]
            )
        )
    return out
