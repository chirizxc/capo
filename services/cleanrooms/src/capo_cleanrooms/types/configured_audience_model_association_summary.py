"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredAudienceModelAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.collaboration_arn
    import capo_cleanrooms.types.configured_audience_model_arn
    import capo_cleanrooms.types.configured_audience_model_association_arn
    import capo_cleanrooms.types.configured_audience_model_association_name
    import capo_cleanrooms.types.membership_arn
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.uuid


class ConfiguredAudienceModelAssociationSummary(TypedDict, closed=True):
    membership_id: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    """<p>A unique identifier of the membership that contains the configured audience model association.</p>"""
    membership_arn: "capo_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The Amazon Resource Name (ARN) of the membership that contains the configured audience model association.</p>"""
    collaboration_arn: "capo_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The Amazon Resource Name (ARN) of the collaboration that contains the configured audience model association.</p>"""
    collaboration_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>A unique identifier of the collaboration that configured audience model is associated with.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the configured audience model association was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the configured audience model association was updated.</p>"""
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>A unique identifier of the configured audience model association.</p>"""
    arn: "capo_cleanrooms.types.configured_audience_model_association_arn.ConfiguredAudienceModelAssociationArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model association.</p>"""
    name: "capo_cleanrooms.types.configured_audience_model_association_name.ConfiguredAudienceModelAssociationName"
    """<p>The name of the configured audience model association.</p>"""
    configured_audience_model_arn: (
        "capo_cleanrooms.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    )
    """<p>The Amazon Resource Name (ARN) of the configured audience model that was used for this configured audience model association.</p>"""
    description: NotRequired[
        "capo_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the configured audience model association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredAudienceModelAssociationSummary) -> dict:
    out: dict = {}
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    out["collaborationArn"] = value["collaboration_arn"]
    out["collaborationId"] = value["collaboration_id"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["configuredAudienceModelArn"] = value["configured_audience_model_arn"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ConfiguredAudienceModelAssociationSummary:
    out: ConfiguredAudienceModelAssociationSummary = {}  # type: ignore[typeddict-item]
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.membership_id required"
        )
    if data.get("membershipArn") is not None:
        out["membership_arn"] = data["membershipArn"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.membership_arn required"
        )
    if data.get("collaborationArn") is not None:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.collaboration_arn required"
        )
    if data.get("collaborationId") is not None:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.collaboration_id required"
        )
    if data.get("createTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.create_time required"
        )
    if data.get("updateTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["update_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.update_time required"
        )
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.id required"
        )
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.arn required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.name required"
        )
    if data.get("configuredAudienceModelArn") is not None:
        out["configured_audience_model_arn"] = data["configuredAudienceModelArn"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelAssociationSummary.configured_audience_model_arn required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
