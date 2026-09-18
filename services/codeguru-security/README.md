# Getting Started

## Installation

```
pip install capo-codeguru-security
```

## Usage

```python
from capo_codeguru_security import AsyncCodeGuruSecurityClient


async def main():
    async with AsyncCodeGuruSecurityClient() as code_guru_security:
        # Example: call the batch_get_findings operation
        response = await code_guru_security.batch_get_findings()
        print(response["findings"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_codeguru_security import AsyncCodeGuruSecurityClient


async def main():
    async with AsyncCodeGuruSecurityClient() as code_guru_security:
        # Example: paginate over get_findings
        async for item in code_guru_security.iter_get_findings():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_codeguru_security import AsyncCodeGuruSecurityClient
from capo_codeguru_security.error import AccessDeniedException


async def main():
    async with AsyncCodeGuruSecurityClient() as code_guru_security:
        try:
            await code_guru_security.batch_get_findings()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_codeguru_security import AsyncCodeGuruSecurityClient


async def main():
    async with AsyncCodeGuruSecurityClient() as code_guru_security:
        # Default: 3 attempts for every operation
        response = await code_guru_security.batch_get_findings()

        # Override per operation
        response = await code_guru_security.batch_get_findings(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await code_guru_security.batch_get_findings(config_overrides={"retry_max_attempts": 1})
```
