"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#IbmDb2LuwDataProviderSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.dms_ssl_mode_value
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.string


class IbmDb2LuwDataProviderSettings(TypedDict, closed=True):
    server_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name of the DB2 LUW server.</p>"""
    port: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The port value for the DB2 LUW data provider.</p>"""
    database_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The database name on the DB2 LUW data provider.</p>"""
    ssl_mode: NotRequired[
        "capo_database_migration_service.types.dms_ssl_mode_value.DmsSslModeValue"
    ]
    """<p>The SSL mode used to connect to the DB2 LUW data provider. The default value is <code>none</code>. Valid Values: <code>none</code> and <code>verify-ca</code>.</p>"""
    certificate_arn: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the certificate used for SSL connection.</p>"""
    encryption_algorithm: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p> The encryption algorithm used for securing the connection to the IBM DB2 LUW database server. You can provide an integer value corresponding to a specific encryption algorithm, or leave this parameter empty to use the default behavior. </p>"""
    security_mechanism: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p> The security mechanism used for authenticating the connection to the IBM DB2 LUW database server. You can provide an integer value corresponding to a specific security mechanism, or leave this parameter empty to use the default behavior. </p>"""
    s3_path: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The path for the Amazon S3 bucket that the application uses for accessing the user-defined schema.</p>"""
    s3_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The ARN for the role the application uses to access its Amazon S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IbmDb2LuwDataProviderSettings) -> dict:
    out: dict = {}
    if "server_name" in value:
        out["ServerName"] = value["server_name"]
    if "port" in value:
        out["Port"] = value["port"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "ssl_mode" in value:
        import capo_database_migration_service.types.dms_ssl_mode_value

        out["SslMode"] = (
            capo_database_migration_service.types.dms_ssl_mode_value.serialize_aws_json_1_1(
                value["ssl_mode"]
            )
        )
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "encryption_algorithm" in value:
        out["EncryptionAlgorithm"] = value["encryption_algorithm"]
    if "security_mechanism" in value:
        out["SecurityMechanism"] = value["security_mechanism"]
    if "s3_path" in value:
        out["S3Path"] = value["s3_path"]
    if "s3_access_role_arn" in value:
        out["S3AccessRoleArn"] = value["s3_access_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IbmDb2LuwDataProviderSettings:
    out: IbmDb2LuwDataProviderSettings = {}  # type: ignore[typeddict-item]
    if data.get("ServerName") is not None:
        out["server_name"] = data["ServerName"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    if data.get("SslMode") is not None:
        import capo_database_migration_service.types.dms_ssl_mode_value

        out["ssl_mode"] = (
            capo_database_migration_service.types.dms_ssl_mode_value.deserialize_aws_json_1_1(
                data["SslMode"]
            )
        )
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    if data.get("EncryptionAlgorithm") is not None:
        out["encryption_algorithm"] = data["EncryptionAlgorithm"]
    if data.get("SecurityMechanism") is not None:
        out["security_mechanism"] = data["SecurityMechanism"]
    if data.get("S3Path") is not None:
        out["s3_path"] = data["S3Path"]
    if data.get("S3AccessRoleArn") is not None:
        out["s3_access_role_arn"] = data["S3AccessRoleArn"]
    return out
