"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ManagedKnowledgeBaseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.bedrock_embedding_model_arn
    import capo_bedrock_agent.types.embedding_model_configuration
    import capo_bedrock_agent.types.embedding_model_type
    import capo_bedrock_agent.types.server_side_encryption_configuration
    import capo_bedrock_agent.types.supplemental_data_storage_configuration


class ManagedKnowledgeBaseConfiguration(TypedDict, closed=True):
    embedding_model_type: NotRequired[
        "capo_bedrock_agent.types.embedding_model_type.EmbeddingModelType"
    ]
    """<p>Choose CUSTOM to provide your own Bedrock embedding model ARN. Choose MANAGED to use a service-managed embedding model.</p>"""
    embedding_model_arn: NotRequired[
        "capo_bedrock_agent.types.bedrock_embedding_model_arn.BedrockEmbeddingModelArn"
    ]
    """<p>The ARN for the embeddings model.</p>"""
    embedding_model_configuration: NotRequired[
        "capo_bedrock_agent.types.embedding_model_configuration.EmbeddingModelConfiguration"
    ]
    """<p>The configuration details for the embeddings model. Not required when choosing the MANAGED embeddingModelType.</p>"""
    server_side_encryption_configuration: NotRequired[
        "capo_bedrock_agent.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    """<p>Contains the configuration for server-side encryption for your managed knowledge base.</p>"""
    supplemental_data_storage_configuration: NotRequired[
        "capo_bedrock_agent.types.supplemental_data_storage_configuration.SupplementalDataStorageConfiguration"
    ]
    """<p>Use this object to specify the Amazon S3 location that the knowledge base uses to process and ingest multimodal content. This field is required when you use a native multimodal embedding model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedKnowledgeBaseConfiguration) -> dict:
    out: dict = {}
    if "embedding_model_type" in value:
        import capo_bedrock_agent.types.embedding_model_type

        out["embeddingModelType"] = (
            capo_bedrock_agent.types.embedding_model_type.serialize_json(
                value["embedding_model_type"]
            )
        )
    if "embedding_model_arn" in value:
        out["embeddingModelArn"] = value["embedding_model_arn"]
    if "embedding_model_configuration" in value:
        import capo_bedrock_agent.types.embedding_model_configuration

        out["embeddingModelConfiguration"] = (
            capo_bedrock_agent.types.embedding_model_configuration.serialize_json(
                value["embedding_model_configuration"]
            )
        )
    if "server_side_encryption_configuration" in value:
        import capo_bedrock_agent.types.server_side_encryption_configuration

        out["serverSideEncryptionConfiguration"] = (
            capo_bedrock_agent.types.server_side_encryption_configuration.serialize_json(
                value["server_side_encryption_configuration"]
            )
        )
    if "supplemental_data_storage_configuration" in value:
        import capo_bedrock_agent.types.supplemental_data_storage_configuration

        out["supplementalDataStorageConfiguration"] = (
            capo_bedrock_agent.types.supplemental_data_storage_configuration.serialize_json(
                value["supplemental_data_storage_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManagedKnowledgeBaseConfiguration:
    out: ManagedKnowledgeBaseConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("embeddingModelType") is not None:
        import capo_bedrock_agent.types.embedding_model_type

        out["embedding_model_type"] = (
            capo_bedrock_agent.types.embedding_model_type.deserialize_json(
                data["embeddingModelType"]
            )
        )
    if data.get("embeddingModelArn") is not None:
        out["embedding_model_arn"] = data["embeddingModelArn"]
    if data.get("embeddingModelConfiguration") is not None:
        import capo_bedrock_agent.types.embedding_model_configuration

        out["embedding_model_configuration"] = (
            capo_bedrock_agent.types.embedding_model_configuration.deserialize_json(
                data["embeddingModelConfiguration"]
            )
        )
    if data.get("serverSideEncryptionConfiguration") is not None:
        import capo_bedrock_agent.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            capo_bedrock_agent.types.server_side_encryption_configuration.deserialize_json(
                data["serverSideEncryptionConfiguration"]
            )
        )
    if data.get("supplementalDataStorageConfiguration") is not None:
        import capo_bedrock_agent.types.supplemental_data_storage_configuration

        out["supplemental_data_storage_configuration"] = (
            capo_bedrock_agent.types.supplemental_data_storage_configuration.deserialize_json(
                data["supplementalDataStorageConfiguration"]
            )
        )
    return out
