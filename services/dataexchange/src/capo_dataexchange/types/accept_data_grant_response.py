"""Generated from Smithy shape ``com.amazonaws.dataexchange#AcceptDataGrantResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dataexchange.types.arn
    import capo_dataexchange.types.data_grant_acceptance_state
    import capo_dataexchange.types.data_grant_description
    import capo_dataexchange.types.data_grant_name
    import capo_dataexchange.types.grant_distribution_scope
    import capo_dataexchange.types.id
    import capo_dataexchange.types.receiver_principal
    import capo_dataexchange.types.sender_principal
    import capo_dataexchange.types.timestamp


class AcceptDataGrantResponse(TypedDict, closed=True):
    name: "capo_dataexchange.types.data_grant_name.DataGrantName"
    """<p>The name of the accepted data grant.</p>"""
    sender_principal: NotRequired[
        "capo_dataexchange.types.sender_principal.SenderPrincipal"
    ]
    """<p>The Amazon Web Services account ID of the data grant sender.</p>"""
    receiver_principal: "capo_dataexchange.types.receiver_principal.ReceiverPrincipal"
    """<p>The Amazon Web Services account ID of the data grant receiver.</p>"""
    description: NotRequired[
        "capo_dataexchange.types.data_grant_description.DataGrantDescription"
    ]
    """<p>The description of the accepted data grant.</p>"""
    acceptance_state: (
        "capo_dataexchange.types.data_grant_acceptance_state.DataGrantAcceptanceState"
    )
    """<p>The acceptance state of the data grant.</p>"""
    accepted_at: NotRequired["capo_dataexchange.types.timestamp.Timestamp"]
    """<p>The timestamp of when the data grant was accepted.</p>"""
    ends_at: NotRequired["capo_dataexchange.types.timestamp.Timestamp"]
    """<p>The timestamp of when access to the associated data set ends.</p>"""
    grant_distribution_scope: (
        "capo_dataexchange.types.grant_distribution_scope.GrantDistributionScope"
    )
    """<p>The distribution scope for the data grant.</p>"""
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The ID of the data set associated to the data grant.</p>"""
    id: "capo_dataexchange.types.id.Id"
    """<p>The ID of the data grant.</p>"""
    arn: "capo_dataexchange.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the accepted data grant.</p>"""
    created_at: "capo_dataexchange.types.timestamp.Timestamp"
    """<p>The timestamp of when the data grant was created.</p>"""
    updated_at: "capo_dataexchange.types.timestamp.Timestamp"
    """<p>The timestamp of when the data grant was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptDataGrantResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "sender_principal" in value:
        out["SenderPrincipal"] = value["sender_principal"]
    out["ReceiverPrincipal"] = value["receiver_principal"]
    if "description" in value:
        out["Description"] = value["description"]
    out["AcceptanceState"] = value["acceptance_state"]
    if "accepted_at" in value:
        import capo_dataexchange.types.timestamp

        out["AcceptedAt"] = capo_dataexchange.types.timestamp.serialize_json(
            value["accepted_at"]
        )
    if "ends_at" in value:
        import capo_dataexchange.types.timestamp

        out["EndsAt"] = capo_dataexchange.types.timestamp.serialize_json(
            value["ends_at"]
        )
    out["GrantDistributionScope"] = value["grant_distribution_scope"]
    out["DataSetId"] = value["data_set_id"]
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    import capo_dataexchange.types.timestamp

    out["CreatedAt"] = capo_dataexchange.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_dataexchange.types.timestamp

    out["UpdatedAt"] = capo_dataexchange.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> AcceptDataGrantResponse:
    out: AcceptDataGrantResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("AcceptDataGrantResponse.name required")
    if data.get("SenderPrincipal") is not None:
        out["sender_principal"] = data["SenderPrincipal"]
    if data.get("ReceiverPrincipal") is not None:
        out["receiver_principal"] = data["ReceiverPrincipal"]
    else:
        raise DeserializationError(
            "AcceptDataGrantResponse.receiver_principal required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("AcceptanceState") is not None:
        out["acceptance_state"] = data["AcceptanceState"]
    else:
        raise DeserializationError("AcceptDataGrantResponse.acceptance_state required")
    if data.get("AcceptedAt") is not None:
        import capo_dataexchange.types.timestamp

        out["accepted_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["AcceptedAt"]
        )
    if data.get("EndsAt") is not None:
        import capo_dataexchange.types.timestamp

        out["ends_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["EndsAt"]
        )
    if data.get("GrantDistributionScope") is not None:
        out["grant_distribution_scope"] = data["GrantDistributionScope"]
    else:
        raise DeserializationError(
            "AcceptDataGrantResponse.grant_distribution_scope required"
        )
    if data.get("DataSetId") is not None:
        out["data_set_id"] = data["DataSetId"]
    else:
        raise DeserializationError("AcceptDataGrantResponse.data_set_id required")
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("AcceptDataGrantResponse.id required")
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("AcceptDataGrantResponse.arn required")
    if data.get("CreatedAt") is not None:
        import capo_dataexchange.types.timestamp

        out["created_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("AcceptDataGrantResponse.created_at required")
    if data.get("UpdatedAt") is not None:
        import capo_dataexchange.types.timestamp

        out["updated_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    else:
        raise DeserializationError("AcceptDataGrantResponse.updated_at required")
    return out
