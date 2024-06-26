from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.get_contact_by_id_response_200 import GetContactByIdResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    contact_id: int,
    *,
    client: Client,
    embed: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/Contact/{contactId}".format(client.base_url, contactId=contact_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["embed"] = embed

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, GetContactByIdResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetContactByIdResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, GetContactByIdResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    contact_id: int,
    *,
    client: Client,
    embed: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, GetContactByIdResponse200]]:
    """Find contact by ID

    Args:
        contact_id (int):
        embed (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetContactByIdResponse200]]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        client=client,
        embed=embed,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    contact_id: int,
    *,
    client: Client,
    embed: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, GetContactByIdResponse200]]:
    """Find contact by ID

    Args:
        contact_id (int):
        embed (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetContactByIdResponse200]
    """

    return sync_detailed(
        contact_id=contact_id,
        client=client,
        embed=embed,
    ).parsed


async def asyncio_detailed(
    contact_id: int,
    *,
    client: Client,
    embed: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, GetContactByIdResponse200]]:
    """Find contact by ID

    Args:
        contact_id (int):
        embed (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetContactByIdResponse200]]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        client=client,
        embed=embed,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    contact_id: int,
    *,
    client: Client,
    embed: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, GetContactByIdResponse200]]:
    """Find contact by ID

    Args:
        contact_id (int):
        embed (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetContactByIdResponse200]
    """

    return (
        await asyncio_detailed(
            contact_id=contact_id,
            client=client,
            embed=embed,
        )
    ).parsed
