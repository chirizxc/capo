"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DomainUseCase``."""

from typing import Literal, TypeAlias, cast

"""<p>The primary use case for the domain, which determines the default configuration and the engine modes that are available. Valid values are <code>SEARCH</code> (full-text search, e-commerce, content discovery, and hybrid and semantic search), <code>VECTOR</code> (k-NN and semantic search, and retrieval-augmented generation), <code>OBSERVABILITY</code> (logs, metrics, traces, and dashboards), and <code>MIXED</code> (a combination of search and analytics). If you don't specify a use case, <code>MIXED</code> is used.</p>"""
DomainUseCase: TypeAlias = Literal[
    "SEARCH",
    "VECTOR",
    "OBSERVABILITY",
    "MIXED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainUseCase) -> str:
    return value


def deserialize_json(data: str) -> DomainUseCase:
    return cast(DomainUseCase, data)
