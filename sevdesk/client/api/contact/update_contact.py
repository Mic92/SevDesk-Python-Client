from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.contact_model import ContactModel
from ...models.update_contact_response_200 import UpdateContactResponse200
from ...types import Response


def _get_kwargs(
    contact_id: int,
    *,
    client: Client,
    json_body: ContactModel,
) -> Dict[str, Any]:
    url = "{}/Contact/{contactId}".format(client.base_url, contactId=contact_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[UpdateContactResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateContactResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[UpdateContactResponse200]:
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
    json_body: ContactModel,
) -> Response[UpdateContactResponse200]:
    """Update an existing contact

    Args:
        contact_id (int):
        json_body (ContactModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateContactResponse200]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        client=client,
        json_body=json_body,
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
    json_body: ContactModel,
) -> Optional[UpdateContactResponse200]:
    """Update an existing contact

    Args:
        contact_id (int):
        json_body (ContactModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateContactResponse200
    """

    return sync_detailed(
        contact_id=contact_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    contact_id: int,
    *,
    client: Client,
    json_body: ContactModel,
) -> Response[UpdateContactResponse200]:
    """Update an existing contact

    Args:
        contact_id (int):
        json_body (ContactModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateContactResponse200]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    contact_id: int,
    *,
    client: Client,
    json_body: ContactModel,
) -> Optional[UpdateContactResponse200]:
    """Update an existing contact

    Args:
        contact_id (int):
        json_body (ContactModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateContactResponse200
    """

    return (
        await asyncio_detailed(
            contact_id=contact_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
