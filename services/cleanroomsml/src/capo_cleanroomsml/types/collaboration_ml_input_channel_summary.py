"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CollaborationMLInputChannelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.account_id
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn_list
    import capo_cleanroomsml.types.ml_input_channel_arn
    import capo_cleanroomsml.types.ml_input_channel_status
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.payer_configuration
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.uuid


class CollaborationMLInputChannelSummary(TypedDict, closed=True):
    create_time: "datetime.datetime"
    """<p>The time at which the ML input channel was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the ML input channel was updated.</p>"""
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the membership that contains the ML input channel.</p>"""
    collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the ML input channel.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the ML input channel.</p>"""
    configured_model_algorithm_associations: "capo_cleanroomsml.types.configured_model_algorithm_association_arn_list.ConfiguredModelAlgorithmAssociationArnList"
    """<p>The associated configured model algorithms used to create the ML input channel.</p>"""
    ml_input_channel_arn: (
        "capo_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn"
    )
    """<p>The Amazon Resource Name (ARN) of the ML input channel.</p>"""
    status: "capo_cleanroomsml.types.ml_input_channel_status.MLInputChannelStatus"
    """<p>The status of the ML input channel.</p>"""
    creator_account_id: "capo_cleanroomsml.types.account_id.AccountId"
    """<p>The account ID of the member who created the ML input channel.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the ML input channel.</p>"""
    payer_configuration: NotRequired[
        "capo_cleanroomsml.types.payer_configuration.PayerConfiguration"
    ]
    """<p>The payer configuration for the ML input channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationMLInputChannelSummary) -> dict:
    out: dict = {}
    import capo_cleanroomsml._protocol.serialize

    out["createTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["create_time"]
    )
    import capo_cleanroomsml._protocol.serialize

    out["updateTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["update_time"]
    )
    out["membershipIdentifier"] = value["membership_identifier"]
    out["collaborationIdentifier"] = value["collaboration_identifier"]
    out["name"] = value["name"]
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn_list

    out["configuredModelAlgorithmAssociations"] = (
        capo_cleanroomsml.types.configured_model_algorithm_association_arn_list.serialize_json(
            value["configured_model_algorithm_associations"]
        )
    )
    out["mlInputChannelArn"] = value["ml_input_channel_arn"]
    import capo_cleanroomsml.types.ml_input_channel_status

    out["status"] = capo_cleanroomsml.types.ml_input_channel_status.serialize_json(
        value["status"]
    )
    out["creatorAccountId"] = value["creator_account_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "payer_configuration" in value:
        import capo_cleanroomsml.types.payer_configuration

        out["payerConfiguration"] = (
            capo_cleanroomsml.types.payer_configuration.serialize_json(
                value["payer_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CollaborationMLInputChannelSummary:
    out: CollaborationMLInputChannelSummary = {}  # type: ignore[typeddict-item]
    if data.get("createTime") is not None:
        import datetime

        out["create_time"] = datetime.datetime.fromisoformat(
            data["createTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError(
            "CollaborationMLInputChannelSummary.create_time required"
        )
    if data.get("updateTime") is not None:
        import datetime

        out["update_time"] = datetime.datetime.fromisoformat(
            data["updateTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError(
            "CollaborationMLInputChannelSummary.update_time required"
        )
    if data.get("membershipIdentifier") is not None:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        raise DeserializationError(
            "CollaborationMLInputChannelSummary.membership_identifier required"
        )
    if data.get("collaborationIdentifier") is not None:
        out["collaboration_identifier"] = data["collaborationIdentifier"]
    else:
        raise DeserializationError(
            "CollaborationMLInputChannelSummary.collaboration_identifier required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CollaborationMLInputChannelSummary.name required")
    if data.get("configuredModelAlgorithmAssociations") is not None:
        import capo_cleanroomsml.types.configured_model_algorithm_association_arn_list

        out["configured_model_algorithm_associations"] = (
            capo_cleanroomsml.types.configured_model_algorithm_association_arn_list.deserialize_json(
                data["configuredModelAlgorithmAssociations"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationMLInputChannelSummary.configured_model_algorithm_associations required"
        )
    if data.get("mlInputChannelArn") is not None:
        out["ml_input_channel_arn"] = data["mlInputChannelArn"]
    else:
        raise DeserializationError(
            "CollaborationMLInputChannelSummary.ml_input_channel_arn required"
        )
    if data.get("status") is not None:
        import capo_cleanroomsml.types.ml_input_channel_status

        out["status"] = (
            capo_cleanroomsml.types.ml_input_channel_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CollaborationMLInputChannelSummary.status required")
    if data.get("creatorAccountId") is not None:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        raise DeserializationError(
            "CollaborationMLInputChannelSummary.creator_account_id required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("payerConfiguration") is not None:
        import capo_cleanroomsml.types.payer_configuration

        out["payer_configuration"] = (
            capo_cleanroomsml.types.payer_configuration.deserialize_json(
                data["payerConfiguration"]
            )
        )
    return out
