"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#RestoreTableFromRecoveryPointRequest``."""

from typing_extensions import NotRequired, TypedDict

from capo_redshift_serverless.errors import DeserializationError


class RestoreTableFromRecoveryPointRequest(TypedDict, closed=True):
    namespace_name: "str"
    """<p>Namespace of the recovery point to restore from.</p>"""
    workgroup_name: "str"
    """<p>The workgroup to restore the table to.</p>"""
    recovery_point_id: "str"
    """<p>The ID of the recovery point to restore the table from.</p>"""
    source_database_name: "str"
    """<p>The name of the source database that contains the table being restored.</p>"""
    source_schema_name: NotRequired["str"]
    """<p>The name of the source schema that contains the table being restored.</p>"""
    source_table_name: "str"
    """<p>The name of the source table being restored.</p>"""
    target_database_name: NotRequired["str"]
    """<p>The name of the database to restore the table to.</p>"""
    target_schema_name: NotRequired["str"]
    """<p>The name of the schema to restore the table to.</p>"""
    new_table_name: "str"
    """<p>The name of the table to create from the restore operation.</p>"""
    activate_case_sensitive_identifier: NotRequired["bool"]
    """<p>Indicates whether name identifiers for database, schema, and table are case sensitive. If true, the names are case sensitive. If false, the names are not case sensitive. The default is false.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreTableFromRecoveryPointRequest) -> dict:
    out: dict = {}
    out["namespaceName"] = value["namespace_name"]
    out["workgroupName"] = value["workgroup_name"]
    out["recoveryPointId"] = value["recovery_point_id"]
    out["sourceDatabaseName"] = value["source_database_name"]
    if "source_schema_name" in value:
        out["sourceSchemaName"] = value["source_schema_name"]
    out["sourceTableName"] = value["source_table_name"]
    if "target_database_name" in value:
        out["targetDatabaseName"] = value["target_database_name"]
    if "target_schema_name" in value:
        out["targetSchemaName"] = value["target_schema_name"]
    out["newTableName"] = value["new_table_name"]
    if "activate_case_sensitive_identifier" in value:
        out["activateCaseSensitiveIdentifier"] = value[
            "activate_case_sensitive_identifier"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreTableFromRecoveryPointRequest:
    out: RestoreTableFromRecoveryPointRequest = {}  # type: ignore[typeddict-item]
    if data.get("namespaceName") is not None:
        out["namespace_name"] = data["namespaceName"]
    else:
        raise DeserializationError(
            "RestoreTableFromRecoveryPointRequest.namespace_name required"
        )
    if data.get("workgroupName") is not None:
        out["workgroup_name"] = data["workgroupName"]
    else:
        raise DeserializationError(
            "RestoreTableFromRecoveryPointRequest.workgroup_name required"
        )
    if data.get("recoveryPointId") is not None:
        out["recovery_point_id"] = data["recoveryPointId"]
    else:
        raise DeserializationError(
            "RestoreTableFromRecoveryPointRequest.recovery_point_id required"
        )
    if data.get("sourceDatabaseName") is not None:
        out["source_database_name"] = data["sourceDatabaseName"]
    else:
        raise DeserializationError(
            "RestoreTableFromRecoveryPointRequest.source_database_name required"
        )
    if data.get("sourceSchemaName") is not None:
        out["source_schema_name"] = data["sourceSchemaName"]
    if data.get("sourceTableName") is not None:
        out["source_table_name"] = data["sourceTableName"]
    else:
        raise DeserializationError(
            "RestoreTableFromRecoveryPointRequest.source_table_name required"
        )
    if data.get("targetDatabaseName") is not None:
        out["target_database_name"] = data["targetDatabaseName"]
    if data.get("targetSchemaName") is not None:
        out["target_schema_name"] = data["targetSchemaName"]
    if data.get("newTableName") is not None:
        out["new_table_name"] = data["newTableName"]
    else:
        raise DeserializationError(
            "RestoreTableFromRecoveryPointRequest.new_table_name required"
        )
    if data.get("activateCaseSensitiveIdentifier") is not None:
        out["activate_case_sensitive_identifier"] = data[
            "activateCaseSensitiveIdentifier"
        ]
    return out
