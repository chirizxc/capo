# Getting Started

## Installation

```
pip install capo-lex-model-building-service
```

## Usage

```python
from capo_lex_model_building_service import AsyncLexModelBuildingServiceClient


async def main():
    async with AsyncLexModelBuildingServiceClient() as lex_model_building_service:
        # Example: call the create_bot_version operation
        response = await lex_model_building_service.create_bot_version()
        print(response["name"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_lex_model_building_service import AsyncLexModelBuildingServiceClient


async def main():
    async with AsyncLexModelBuildingServiceClient() as lex_model_building_service:
        # Example: paginate over get_bot_aliases
        async for item in lex_model_building_service.iter_get_bot_aliases():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_lex_model_building_service import AsyncLexModelBuildingServiceClient
from capo_lex_model_building_service.error import BadRequestException


async def main():
    async with AsyncLexModelBuildingServiceClient() as lex_model_building_service:
        try:
            await lex_model_building_service.create_bot_version()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_lex_model_building_service import AsyncLexModelBuildingServiceClient


async def main():
    async with AsyncLexModelBuildingServiceClient() as lex_model_building_service:
        # Default: 3 attempts for every operation
        response = await lex_model_building_service.create_bot_version()

        # Override per operation
        response = await lex_model_building_service.create_bot_version(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await lex_model_building_service.create_bot_version(config_overrides={"retry_max_attempts": 1})
```
