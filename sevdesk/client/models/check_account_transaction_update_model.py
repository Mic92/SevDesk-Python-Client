import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.check_account_transaction_update_model_status import (
    CheckAccountTransactionUpdateModelStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_account_transaction_update_model_check_account import (
        CheckAccountTransactionUpdateModelCheckAccount,
    )
    from ..models.check_account_transaction_update_model_source_transaction import (
        CheckAccountTransactionUpdateModelSourceTransaction,
    )
    from ..models.check_account_transaction_update_model_target_transaction import (
        CheckAccountTransactionUpdateModelTargetTransaction,
    )


T = TypeVar("T", bound="CheckAccountTransactionUpdateModel")


@attr.s(auto_attribs=True)
class CheckAccountTransactionUpdateModel:
    """CheckAccountTransaction model. Responsible for the transactions on payment accounts.

    Attributes:
        value_date (Union[Unset, datetime.datetime]): Date the check account transaction was booked Example: 01.01.2022.
        entry_date (Union[Unset, datetime.datetime]): Date the check account transaction was imported Example:
            01.01.2022.
        paymt_purpose (Union[Unset, str]): the purpose of the transaction Example: salary.
        amount (Union[Unset, None, float]): Amount of the transaction Example: 100.
        payee_payer_name (Union[Unset, None, str]): Name of the payee/payer Example: Cercei Lannister.
        check_account (Union[Unset, CheckAccountTransactionUpdateModelCheckAccount]): The check account to which the
            transaction belongs
        status (Union[Unset, CheckAccountTransactionUpdateModelStatus]): Status of the check account transaction.<br>
                 100 <-> Created<br>
                 200 <-> Linked<br>
                 300 <-> Private<br>
                 400 <-> Booked
        enshrined (Union[Unset, None, datetime.datetime]): Defines if the transaction has been enshrined and can not be
            changed any more.
        source_transaction (Union[Unset, None, CheckAccountTransactionUpdateModelSourceTransaction]): The check account
            transaction serving as the source of the rebooking
        target_transaction (Union[Unset, None, CheckAccountTransactionUpdateModelTargetTransaction]): The check account
            transaction serving as the target of the rebooking
    """

    value_date: Union[Unset, datetime.datetime] = UNSET
    entry_date: Union[Unset, datetime.datetime] = UNSET
    paymt_purpose: Union[Unset, str] = UNSET
    amount: Union[Unset, None, float] = UNSET
    payee_payer_name: Union[Unset, None, str] = UNSET
    check_account: Union[
        Unset, "CheckAccountTransactionUpdateModelCheckAccount"
    ] = UNSET
    status: Union[Unset, CheckAccountTransactionUpdateModelStatus] = UNSET
    enshrined: Union[Unset, None, datetime.datetime] = UNSET
    source_transaction: Union[
        Unset, None, "CheckAccountTransactionUpdateModelSourceTransaction"
    ] = UNSET
    target_transaction: Union[
        Unset, None, "CheckAccountTransactionUpdateModelTargetTransaction"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value_date: Union[Unset, str] = UNSET
        if not isinstance(self.value_date, Unset):
            value_date = self.value_date.isoformat()

        entry_date: Union[Unset, str] = UNSET
        if not isinstance(self.entry_date, Unset):
            entry_date = self.entry_date.isoformat()

        paymt_purpose = self.paymt_purpose
        amount = self.amount
        payee_payer_name = self.payee_payer_name
        check_account: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.check_account, Unset):
            check_account = self.check_account.to_dict()

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        enshrined: Union[Unset, None, str] = UNSET
        if not isinstance(self.enshrined, Unset):
            enshrined = self.enshrined.isoformat() if self.enshrined else None

        source_transaction: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.source_transaction, Unset):
            source_transaction = (
                self.source_transaction.to_dict() if self.source_transaction else None
            )

        target_transaction: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.target_transaction, Unset):
            target_transaction = (
                self.target_transaction.to_dict() if self.target_transaction else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value_date is not UNSET:
            field_dict["valueDate"] = value_date
        if entry_date is not UNSET:
            field_dict["entryDate"] = entry_date
        if paymt_purpose is not UNSET:
            field_dict["paymtPurpose"] = paymt_purpose
        if amount is not UNSET:
            field_dict["amount"] = amount
        if payee_payer_name is not UNSET:
            field_dict["payeePayerName"] = payee_payer_name
        if check_account is not UNSET:
            field_dict["checkAccount"] = check_account
        if status is not UNSET:
            field_dict["status"] = status
        if enshrined is not UNSET:
            field_dict["enshrined"] = enshrined
        if source_transaction is not UNSET:
            field_dict["sourceTransaction"] = source_transaction
        if target_transaction is not UNSET:
            field_dict["targetTransaction"] = target_transaction

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.check_account_transaction_update_model_check_account import (
            CheckAccountTransactionUpdateModelCheckAccount,
        )
        from ..models.check_account_transaction_update_model_source_transaction import (
            CheckAccountTransactionUpdateModelSourceTransaction,
        )
        from ..models.check_account_transaction_update_model_target_transaction import (
            CheckAccountTransactionUpdateModelTargetTransaction,
        )

        d = src_dict.copy()
        _value_date = d.pop("valueDate", UNSET)
        value_date: Union[Unset, datetime.datetime]
        if isinstance(_value_date, Unset):
            value_date = UNSET
        else:
            value_date = isoparse(_value_date)

        _entry_date = d.pop("entryDate", UNSET)
        entry_date: Union[Unset, datetime.datetime]
        if isinstance(_entry_date, Unset):
            entry_date = UNSET
        else:
            entry_date = isoparse(_entry_date)

        paymt_purpose = d.pop("paymtPurpose", UNSET)

        amount = d.pop("amount", UNSET)

        payee_payer_name = d.pop("payeePayerName", UNSET)

        _check_account = d.pop("checkAccount", UNSET)
        check_account: Union[Unset, CheckAccountTransactionUpdateModelCheckAccount]
        if isinstance(_check_account, Unset):
            check_account = UNSET
        else:
            check_account = CheckAccountTransactionUpdateModelCheckAccount.from_dict(
                _check_account
            )

        _status = d.pop("status", UNSET)
        status: Union[Unset, CheckAccountTransactionUpdateModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CheckAccountTransactionUpdateModelStatus(_status)

        _enshrined = d.pop("enshrined", UNSET)
        enshrined: Union[Unset, None, datetime.datetime]
        if _enshrined is None:
            enshrined = None
        elif isinstance(_enshrined, Unset):
            enshrined = UNSET
        else:
            enshrined = isoparse(_enshrined)

        _source_transaction = d.pop("sourceTransaction", UNSET)
        source_transaction: Union[
            Unset, None, CheckAccountTransactionUpdateModelSourceTransaction
        ]
        if _source_transaction is None:
            source_transaction = None
        elif isinstance(_source_transaction, Unset):
            source_transaction = UNSET
        else:
            source_transaction = (
                CheckAccountTransactionUpdateModelSourceTransaction.from_dict(
                    _source_transaction
                )
            )

        _target_transaction = d.pop("targetTransaction", UNSET)
        target_transaction: Union[
            Unset, None, CheckAccountTransactionUpdateModelTargetTransaction
        ]
        if _target_transaction is None:
            target_transaction = None
        elif isinstance(_target_transaction, Unset):
            target_transaction = UNSET
        else:
            target_transaction = (
                CheckAccountTransactionUpdateModelTargetTransaction.from_dict(
                    _target_transaction
                )
            )

        check_account_transaction_update_model = cls(
            value_date=value_date,
            entry_date=entry_date,
            paymt_purpose=paymt_purpose,
            amount=amount,
            payee_payer_name=payee_payer_name,
            check_account=check_account,
            status=status,
            enshrined=enshrined,
            source_transaction=source_transaction,
            target_transaction=target_transaction,
        )

        check_account_transaction_update_model.additional_properties = d
        return check_account_transaction_update_model

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
