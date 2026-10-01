"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#UpdateRevenueAttributionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_revenue_measurement.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_partnercentral_revenue_measurement.types.revenue_attribution_id
    import capo_partnercentral_revenue_measurement.types.revision_token


class UpdateRevenueAttributionOutput(TypedDict, closed=True):
    id: "capo_partnercentral_revenue_measurement.types.revenue_attribution_id.RevenueAttributionId"
    """<p>The unique identifier of the updated revenue attribution.</p>"""
    arn: "str"
    """<p>The Amazon Resource Name (ARN) of the updated revenue attribution.</p>"""
    description: NotRequired["str"]
    """<p>The updated description of the revenue attribution.</p>"""
    last_modified_date: "datetime.datetime"
    """<p>The date when the attribution was last modified.</p>"""
    latest_revision: NotRequired[
        "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
    ]
    """<p>The latest revision of the attribution after the update.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateRevenueAttributionOutput) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_partnercentral_revenue_measurement.types._prelude.timestamp

    out["LastModifiedDate"] = (
        capo_partnercentral_revenue_measurement.types._prelude.timestamp.serialize_cbor(
            value["last_modified_date"]
        )
    )
    if "latest_revision" in value:
        out["LatestRevision"] = value["latest_revision"]
    return out


def deserialize_cbor(data: dict) -> UpdateRevenueAttributionOutput:
    out: UpdateRevenueAttributionOutput = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdateRevenueAttributionOutput.id required")
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("UpdateRevenueAttributionOutput.arn required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("LastModifiedDate") is not None:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["last_modified_date"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.deserialize_cbor(
                data["LastModifiedDate"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRevenueAttributionOutput.last_modified_date required"
        )
    if data.get("LatestRevision") is not None:
        out["latest_revision"] = data["LatestRevision"]
    return out
