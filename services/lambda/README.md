# Getting Started

## Installation

```
pip install capo-lambda
```

## Usage

```python
from capo_lambda import AsyncLambdaClient


async def main():
    async with AsyncLambdaClient() as lambda_:
        # Example: call the delete_function operation
        response = await lambda_.delete_function()
        print(response["status_code"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_lambda import AsyncLambdaClient


async def main():
    async with AsyncLambdaClient() as lambda_:
        # Example: paginate over list_capacity_providers
        async for item in lambda_.iter_list_capacity_providers():
            print(item)
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks, or the whole body as `bytes`, for the streaming parameter.

```python
from capo_lambda import AsyncLambdaClient


async def main():
    async with AsyncLambdaClient() as lambda_:
        # Example: call invoke_async with a streaming request body
        async def chunks():
            yield b'Hello, World!'

        response = await lambda_.invoke_async(invoke_args=chunks())
        print(response)

        # Or pass the whole body as bytes
        response = await lambda_.invoke_async(invoke_args=b'Hello, World!')
        print(response)
```

## Waiters

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_until_` prefixed method.

```python
from capo_lambda import AsyncLambdaClient


async def main():
    async with AsyncLambdaClient() as lambda_:
        # Example: wait for function_exists
        await lambda_.wait_until_function_exists(max_wait_time=300)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_lambda import AsyncLambdaClient
from capo_lambda.error import InvalidParameterValueException


async def main():
    async with AsyncLambdaClient() as lambda_:
        try:
            await lambda_.delete_function()
        except InvalidParameterValueException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_lambda import AsyncLambdaClient


async def main():
    async with AsyncLambdaClient() as lambda_:
        # Default: 3 attempts for every operation
        response = await lambda_.delete_function()

        # Override per operation
        response = await lambda_.delete_function(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await lambda_.delete_function(config_overrides={"retry_max_attempts": 1})
```
