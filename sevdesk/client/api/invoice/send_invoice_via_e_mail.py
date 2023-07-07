from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.send_invoice_via_e_mail_json_body import SendInvoiceViaEMailJsonBody
from ...models.send_invoice_via_e_mail_response_201 import (
    SendInvoiceViaEMailResponse201,
)
from ...types import Response


def _get_kwargs(
    document_id: int,
    *,
    client: Client,
    json_body: SendInvoiceViaEMailJsonBody,
) -> Dict[str, Any]:
    url = "{}/Invoice/{DocumentId}/sendViaEmail".format(
        client.base_url, DocumentId=document_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, SendInvoiceViaEMailResponse201]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = SendInvoiceViaEMailResponse201.from_dict(response.json())

        return response_201
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
) -> Response[Union[Any, SendInvoiceViaEMailResponse201]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    document_id: int,
    *,
    client: Client,
    json_body: SendInvoiceViaEMailJsonBody,
) -> Response[Union[Any, SendInvoiceViaEMailResponse201]]:
    """Send invoice via email

     This endpoint sends the specified invoice to a customer via email. This will automatically mark the
    invoice as sent. Please note, that in production an invoice is not allowed to be changed after this
    happened!

    Args:
        document_id (int):
        json_body (SendInvoiceViaEMailJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SendInvoiceViaEMailResponse201]]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    document_id: int,
    *,
    client: Client,
    json_body: SendInvoiceViaEMailJsonBody,
) -> Optional[Union[Any, SendInvoiceViaEMailResponse201]]:
    """Send invoice via email

     This endpoint sends the specified invoice to a customer via email. This will automatically mark the
    invoice as sent. Please note, that in production an invoice is not allowed to be changed after this
    happened!

    Args:
        document_id (int):
        json_body (SendInvoiceViaEMailJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SendInvoiceViaEMailResponse201]
    """

    return sync_detailed(
        document_id=document_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    document_id: int,
    *,
    client: Client,
    json_body: SendInvoiceViaEMailJsonBody,
) -> Response[Union[Any, SendInvoiceViaEMailResponse201]]:
    """Send invoice via email

     This endpoint sends the specified invoice to a customer via email. This will automatically mark the
    invoice as sent. Please note, that in production an invoice is not allowed to be changed after this
    happened!

    Args:
        document_id (int):
        json_body (SendInvoiceViaEMailJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SendInvoiceViaEMailResponse201]]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    document_id: int,
    *,
    client: Client,
    json_body: SendInvoiceViaEMailJsonBody,
) -> Optional[Union[Any, SendInvoiceViaEMailResponse201]]:
    """Send invoice via email

     This endpoint sends the specified invoice to a customer via email. This will automatically mark the
    invoice as sent. Please note, that in production an invoice is not allowed to be changed after this
    happened!

    Args:
        document_id (int):
        json_body (SendInvoiceViaEMailJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SendInvoiceViaEMailResponse201]
    """

    return (
        await asyncio_detailed(
            document_id=document_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
