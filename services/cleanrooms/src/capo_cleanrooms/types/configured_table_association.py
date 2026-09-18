"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.configured_table_arn
    import capo_cleanrooms.types.configured_table_association_analysis_rule_type_list
    import capo_cleanrooms.types.configured_table_association_arn
    import capo_cleanrooms.types.membership_arn
    import capo_cleanrooms.types.role_arn
    import capo_cleanrooms.types.table_alias
    import capo_cleanrooms.types.table_description
    import capo_cleanrooms.types.uuid


class ConfiguredTableAssociation(TypedDict, closed=True):
    arn: "capo_cleanrooms.types.configured_table_association_arn.ConfiguredTableAssociationArn"
    """<p>The unique ARN for the configured table association.</p>"""
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the configured table association.</p>"""
    configured_table_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the configured table that the association refers to.</p>"""
    configured_table_arn: (
        "capo_cleanrooms.types.configured_table_arn.ConfiguredTableArn"
    )
    """<p>The unique ARN for the configured table that the association refers to.</p>"""
    membership_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the membership this configured table association belongs to.</p>"""
    membership_arn: "capo_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The unique ARN for the membership this configured table association belongs to.</p>"""
    role_arn: "capo_cleanrooms.types.role_arn.RoleArn"
    """<p>The service will assume this role to access catalog metadata and query the table.</p>"""
    name: "capo_cleanrooms.types.table_alias.TableAlias"
    """<p>The name of the configured table association, in lowercase. The table is identified by this name when running protected queries against the underlying data.</p>"""
    description: NotRequired["capo_cleanrooms.types.table_description.TableDescription"]
    """<p>A description of the configured table association.</p>"""
    analysis_rule_types: NotRequired[
        "capo_cleanrooms.types.configured_table_association_analysis_rule_type_list.ConfiguredTableAssociationAnalysisRuleTypeList"
    ]
    """<p> The analysis rule types for the configured table association.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the configured table association was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the configured table association was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAssociation) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    out["configuredTableId"] = value["configured_table_id"]
    out["configuredTableArn"] = value["configured_table_arn"]
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    out["roleArn"] = value["role_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "analysis_rule_types" in value:
        import capo_cleanrooms.types.configured_table_association_analysis_rule_type_list

        out["analysisRuleTypes"] = (
            capo_cleanrooms.types.configured_table_association_analysis_rule_type_list.serialize_json(
                value["analysis_rule_types"]
            )
        )
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> ConfiguredTableAssociation:
    out: ConfiguredTableAssociation = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ConfiguredTableAssociation.arn required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ConfiguredTableAssociation.id required")
    if data.get("configuredTableId") is not None:
        out["configured_table_id"] = data["configuredTableId"]
    else:
        raise DeserializationError(
            "ConfiguredTableAssociation.configured_table_id required"
        )
    if data.get("configuredTableArn") is not None:
        out["configured_table_arn"] = data["configuredTableArn"]
    else:
        raise DeserializationError(
            "ConfiguredTableAssociation.configured_table_arn required"
        )
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("ConfiguredTableAssociation.membership_id required")
    if data.get("membershipArn") is not None:
        out["membership_arn"] = data["membershipArn"]
    else:
        raise DeserializationError("ConfiguredTableAssociation.membership_arn required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("ConfiguredTableAssociation.role_arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ConfiguredTableAssociation.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("analysisRuleTypes") is not None:
        import capo_cleanrooms.types.configured_table_association_analysis_rule_type_list

        out["analysis_rule_types"] = (
            capo_cleanrooms.types.configured_table_association_analysis_rule_type_list.deserialize_json(
                data["analysisRuleTypes"]
            )
        )
    if data.get("createTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        raise DeserializationError("ConfiguredTableAssociation.create_time required")
    if data.get("updateTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["update_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError("ConfiguredTableAssociation.update_time required")
    return out
