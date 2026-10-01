"""Generated from Smithy shape ``com.amazonaws.quicksight#KnowledgeBaseSearchFilterName``."""

from typing import Literal, TypeAlias, cast

"""<p>The name of a field that you can use to filter knowledge base search results. Valid values include:</p> <ul> <li> <p> <code>DATASOURCE_ARN</code> – The Amazon Resource Name (ARN) of the associated data source.</p> </li> <li> <p> <code>DIRECT_QUICKSIGHT_OWNER</code> – An Amazon QuickSight user or group with direct owner permissions.</p> </li> <li> <p> <code>DIRECT_QUICKSIGHT_SOLE_OWNER</code> – An Amazon QuickSight user or group that is the sole direct owner.</p> </li> <li> <p> <code>DIRECT_QUICKSIGHT_VIEWER_OR_OWNER</code> – An Amazon QuickSight user or group with direct viewer or owner permissions.</p> </li> <li> <p> <code>KNOWLEDGE_BASE_ID</code> – The unique identifier of the knowledge base.</p> </li> <li> <p> <code>KNOWLEDGE_BASE_NAME</code> – The display name of the knowledge base.</p> </li> <li> <p> <code>KNOWLEDGE_BASE_SIZE_BYTES</code> – The size of the knowledge base in bytes.</p> </li> <li> <p> <code>PRIMARY_OWNER</code> – The Amazon Resource Name (ARN) of the primary owner of the knowledge base.</p> </li> </ul>"""
KnowledgeBaseSearchFilterName: TypeAlias = Literal[
    "KNOWLEDGE_BASE_ID",
    "KNOWLEDGE_BASE_NAME",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "KNOWLEDGE_BASE_SIZE_BYTES",
    "PRIMARY_OWNER",
    "DATASOURCE_ARN",
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseSearchFilterName) -> str:
    return value


def deserialize_json(data: str) -> KnowledgeBaseSearchFilterName:
    return cast(KnowledgeBaseSearchFilterName, data)
