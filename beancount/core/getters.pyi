# Stubs for beancount.core.getters (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional, Tuple, Set, Iterable, TypeVar, List, Dict, Callable
from datetime import date

from beancount.core.data import Transaction, Pad, Commodity

T = TypeVar('T')

Directive = Any

class GetAccounts:
    def get_accounts_use_map(self, entries: List[Directive]) -> Tuple[Dict[str, date], Dict[str, date]]: ...
    def get_entry_accounts(self, entry: Directive) -> Set[str]: ...
    def Transaction(_, entry: Transaction) -> Iterable[str]: ...
    def Pad(_, entry: Pad) -> Iterable[Tuple[str, str]]: ...
    Open = ...  # type: Callable[[Directive], Tuple[str]]
    Close = ...  # type: Callable[[Directive], Tuple[str]]
    Balance = ...  # type: Callable[[Directive], Tuple[str]]
    Note = ...  # type: Callable[[Directive], Tuple[str]]
    Document = ...  # type: Callable[[Directive], Tuple[str]]
    # TODO: the following Callable should return Tuple[()] instead instead
    Commodity = ...  # type: Callable[[Directive], Tuple]
    Event = ...  # type: Callable[[Directive], Tuple]
    Query = ...  # type: Callable[[Directive], Tuple]
    Price = ...  # type: Callable[[Directive], Tuple]
    Custom = ...  # type: Callable[[Directive], Tuple]

def get_accounts_use_map(entries: List[Directive]) -> Tuple[Dict[str, date], Dict[str, date]]: ...
def get_accounts(entries: List[Directive]) -> Set[str]: ...
def get_entry_accounts(entry: Directive) -> Set[str]: ...
def get_account_components(entries: List[Directive]) -> List[str]: ...
def get_all_tags(entries: List[Directive]) -> List[str]: ...
def get_all_payees(entries: List[Directive]) -> List[str]: ...
def get_leveln_parent_accounts(account_names: List[str], level: int, nrepeats: int = ...) -> List[str]: ...
def get_min_max_dates(entries: List[Directive], types: Tuple[Directive,...] = ...) -> Tuple[date, date]: ...
def get_active_years(entries: List[Directive]) -> Iterable[int]: ...
def get_account_open_close(entries: List[Directive]) -> Dict[str, Tuple[Directive, Directive]]: ...
def get_commodity_map(entries: List[Directive], create_missing: bool = ...) -> Dict[str, Commodity]: ...
def get_values_meta(name_to_entries_map: Dict[T, Directive], *meta_keys: str, default: Optional[str] = ...) -> Dict[T, Directive]: ...
