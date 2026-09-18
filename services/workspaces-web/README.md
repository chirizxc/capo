# Getting Started

## Installation

```
pip install capo-workspaces-web
```

## Usage

```python
from capo_workspaces_web import AsyncWorkSpacesWebClient


async def main():
    async with AsyncWorkSpacesWebClient() as work_spaces_web:
        # Example: call the expire_session operation
        response = await work_spaces_web.expire_session()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_workspaces_web import AsyncWorkSpacesWebClient


async def main():
    async with AsyncWorkSpacesWebClient() as work_spaces_web:
        # Example: paginate over list_sessions
        async for item in work_spaces_web.iter_list_sessions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_workspaces_web import AsyncWorkSpacesWebClient
from capo_workspaces_web.error import AccessDeniedException


async def main():
    async with AsyncWorkSpacesWebClient() as work_spaces_web:
        try:
            await work_spaces_web.expire_session()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_workspaces_web import AsyncWorkSpacesWebClient


async def main():
    async with AsyncWorkSpacesWebClient() as work_spaces_web:
        # Default: 3 attempts for every operation
        response = await work_spaces_web.expire_session()

        # Override per operation
        response = await work_spaces_web.expire_session(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await work_spaces_web.expire_session(config_overrides={"retry_max_attempts": 1})
```
