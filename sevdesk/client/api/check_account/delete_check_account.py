from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.delete_check_account_response_200 import DeleteCheckAccountResponse200
from ...types import Response


def _get_kwargs(
    check_account_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/CheckAccount/{checkAccountId}".format(
        client.base_url, checkAccountId=check_account_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, DeleteCheckAccountResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeleteCheckAccountResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, DeleteCheckAccountResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    check_account_id: int,
    *,
    client: Client,
) -> Response[Union[Any, DeleteCheckAccountResponse200]]:
    """Deletes a check account

    Args:
        check_account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteCheckAccountResponse200]]
    """

    kwargs = _get_kwargs(
        check_account_id=check_account_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    check_account_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, DeleteCheckAccountResponse200]]:
    """Deletes a check account

    Args:
        check_account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteCheckAccountResponse200]
    """

    return sync_detailed(
        check_account_id=check_account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    check_account_id: int,
    *,
    client: Client,
) -> Response[Union[Any, DeleteCheckAccountResponse200]]:
    """Deletes a check account

    Args:
        check_account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteCheckAccountResponse200]]
    """

    kwargs = _get_kwargs(
        check_account_id=check_account_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    check_account_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, DeleteCheckAccountResponse200]]:
    """Deletes a check account

    Args:
        check_account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteCheckAccountResponse200]
    """

    return (
        await asyncio_detailed(
            check_account_id=check_account_id,
            client=client,
        )
    ).parsed
