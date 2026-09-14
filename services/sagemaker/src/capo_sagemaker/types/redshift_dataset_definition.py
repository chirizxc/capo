"""Generated from Smithy shape ``com.amazonaws.sagemaker#RedshiftDatasetDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.redshift_cluster_id
    import capo_sagemaker.types.redshift_database
    import capo_sagemaker.types.redshift_query_string
    import capo_sagemaker.types.redshift_result_compression_type
    import capo_sagemaker.types.redshift_result_format
    import capo_sagemaker.types.redshift_user_name
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.s3_uri


class RedshiftDatasetDefinition(TypedDict, closed=True):
    cluster_id: NotRequired[
        "capo_sagemaker.types.redshift_cluster_id.RedshiftClusterId"
    ]
    database: NotRequired["capo_sagemaker.types.redshift_database.RedshiftDatabase"]
    db_user: NotRequired["capo_sagemaker.types.redshift_user_name.RedshiftUserName"]
    query_string: NotRequired[
        "capo_sagemaker.types.redshift_query_string.RedshiftQueryString"
    ]
    cluster_role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The IAM role attached to your Redshift cluster that Amazon SageMaker uses to generate datasets.</p>"""
    output_s3_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The location in Amazon S3 where the Redshift query results are stored.</p>"""
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt data from a Redshift execution.</p>"""
    output_format: NotRequired[
        "capo_sagemaker.types.redshift_result_format.RedshiftResultFormat"
    ]
    output_compression: NotRequired[
        "capo_sagemaker.types.redshift_result_compression_type.RedshiftResultCompressionType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftDatasetDefinition) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "database" in value:
        out["Database"] = value["database"]
    if "db_user" in value:
        out["DbUser"] = value["db_user"]
    if "query_string" in value:
        out["QueryString"] = value["query_string"]
    if "cluster_role_arn" in value:
        out["ClusterRoleArn"] = value["cluster_role_arn"]
    if "output_s3_uri" in value:
        out["OutputS3Uri"] = value["output_s3_uri"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "output_format" in value:
        import capo_sagemaker.types.redshift_result_format

        out["OutputFormat"] = (
            capo_sagemaker.types.redshift_result_format.serialize_aws_json_1_1(
                value["output_format"]
            )
        )
    if "output_compression" in value:
        import capo_sagemaker.types.redshift_result_compression_type

        out["OutputCompression"] = (
            capo_sagemaker.types.redshift_result_compression_type.serialize_aws_json_1_1(
                value["output_compression"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RedshiftDatasetDefinition:
    out: RedshiftDatasetDefinition = {}  # type: ignore[typeddict-item]
    if data.get("ClusterId") is not None:
        out["cluster_id"] = data["ClusterId"]
    if data.get("Database") is not None:
        out["database"] = data["Database"]
    if data.get("DbUser") is not None:
        out["db_user"] = data["DbUser"]
    if data.get("QueryString") is not None:
        out["query_string"] = data["QueryString"]
    if data.get("ClusterRoleArn") is not None:
        out["cluster_role_arn"] = data["ClusterRoleArn"]
    if data.get("OutputS3Uri") is not None:
        out["output_s3_uri"] = data["OutputS3Uri"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("OutputFormat") is not None:
        import capo_sagemaker.types.redshift_result_format

        out["output_format"] = (
            capo_sagemaker.types.redshift_result_format.deserialize_aws_json_1_1(
                data["OutputFormat"]
            )
        )
    if data.get("OutputCompression") is not None:
        import capo_sagemaker.types.redshift_result_compression_type

        out["output_compression"] = (
            capo_sagemaker.types.redshift_result_compression_type.deserialize_aws_json_1_1(
                data["OutputCompression"]
            )
        )
    return out
