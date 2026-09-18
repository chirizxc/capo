# Getting Started

## Installation

```
pip install capo-app-mesh
```

## Usage

```python
from capo_app_mesh import AsyncAppMeshClient


async def main():
    async with AsyncAppMeshClient() as app_mesh:
        # Example: call the list_tags_for_resource operation
        response = await app_mesh.list_tags_for_resource()
        print(response["tags"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_app_mesh import AsyncAppMeshClient


async def main():
    async with AsyncAppMeshClient() as app_mesh:
        # Example: paginate over list_tags_for_resource
        async for item in app_mesh.iter_list_tags_for_resource():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_app_mesh import AsyncAppMeshClient
from capo_app_mesh.error import BadRequestException


async def main():
    async with AsyncAppMeshClient() as app_mesh:
        try:
            await app_mesh.list_tags_for_resource()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_app_mesh import AsyncAppMeshClient


async def main():
    async with AsyncAppMeshClient() as app_mesh:
        # Default: 3 attempts for every operation
        response = await app_mesh.list_tags_for_resource()

        # Override per operation
        response = await app_mesh.list_tags_for_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await app_mesh.list_tags_for_resource(config_overrides={"retry_max_attempts": 1})
```
