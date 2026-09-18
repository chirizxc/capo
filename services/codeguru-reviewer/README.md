# Getting Started

## Installation

```
pip install capo-codeguru-reviewer
```

## Usage

```python
from capo_codeguru_reviewer import AsyncCodeGuruReviewerClient


async def main():
    async with AsyncCodeGuruReviewerClient() as code_guru_reviewer:
        # Example: call the associate_repository operation
        response = await code_guru_reviewer.associate_repository()
        print(response["repository_association"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_codeguru_reviewer import AsyncCodeGuruReviewerClient


async def main():
    async with AsyncCodeGuruReviewerClient() as code_guru_reviewer:
        # Example: paginate over list_code_reviews
        async for item in code_guru_reviewer.iter_list_code_reviews():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_codeguru_reviewer import AsyncCodeGuruReviewerClient
from capo_codeguru_reviewer.error import AccessDeniedException


async def main():
    async with AsyncCodeGuruReviewerClient() as code_guru_reviewer:
        try:
            await code_guru_reviewer.associate_repository()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_codeguru_reviewer import AsyncCodeGuruReviewerClient


async def main():
    async with AsyncCodeGuruReviewerClient() as code_guru_reviewer:
        # Default: 3 attempts for every operation
        response = await code_guru_reviewer.associate_repository()

        # Override per operation
        response = await code_guru_reviewer.associate_repository(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await code_guru_reviewer.associate_repository(config_overrides={"retry_max_attempts": 1})
```
