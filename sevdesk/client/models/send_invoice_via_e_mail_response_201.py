from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_model import EmailModel


T = TypeVar("T", bound="SendInvoiceViaEMailResponse201")


@attr.s(auto_attribs=True)
class SendInvoiceViaEMailResponse201:
    """
    Attributes:
        objects (Union[Unset, List['EmailModel']]):
    """

    objects: Union[Unset, List["EmailModel"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        objects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.objects, Unset):
            objects = []
            for objects_item_data in self.objects:
                objects_item = objects_item_data.to_dict()

                objects.append(objects_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objects is not UNSET:
            field_dict["objects"] = objects

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.email_model import EmailModel

        d = src_dict.copy()
        objects = []
        _objects = d.pop("objects", UNSET)
        for objects_item_data in _objects or []:
            objects_item = EmailModel.from_dict(objects_item_data)

            objects.append(objects_item)

        send_invoice_via_e_mail_response_201 = cls(
            objects=objects,
        )

        send_invoice_via_e_mail_response_201.additional_properties = d
        return send_invoice_via_e_mail_response_201

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
