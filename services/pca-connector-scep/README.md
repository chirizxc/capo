# Getting Started

## Installation

```
pip install capo-pca-connector-scep
```

## Usage

```python
from capo_pca_connector_scep import AsyncPcaConnectorScepClient


async def main():
    async with AsyncPcaConnectorScepClient() as pca_connector_scep:
        # Example: call the list_tags_for_resource operation
        response = await pca_connector_scep.list_tags_for_resource()
        print(response["tags"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_pca_connector_scep import AsyncPcaConnectorScepClient


async def main():
    async with AsyncPcaConnectorScepClient() as pca_connector_scep:
        # Example: paginate over list_challenge_metadata
        async for item in pca_connector_scep.iter_list_challenge_metadata():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_pca_connector_scep import AsyncPcaConnectorScepClient
from capo_pca_connector_scep.error import AccessDeniedException


async def main():
    async with AsyncPcaConnectorScepClient() as pca_connector_scep:
        try:
            await pca_connector_scep.list_tags_for_resource()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_pca_connector_scep import AsyncPcaConnectorScepClient


async def main():
    async with AsyncPcaConnectorScepClient() as pca_connector_scep:
        # Default: 3 attempts for every operation
        response = await pca_connector_scep.list_tags_for_resource()

        # Override per operation
        response = await pca_connector_scep.list_tags_for_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await pca_connector_scep.list_tags_for_resource(config_overrides={"retry_max_attempts": 1})
```
