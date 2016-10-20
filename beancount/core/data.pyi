# Stubs for beancount.core.data (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple
from datetime import date
from decimal import Decimal
from typing import (Any, Optional, List, Dict, NamedTuple, Set, Union, Tuple,
                    Iterable)

from beancount.core.amount import Amount
from beancount.core.position import Cost
from beancount.core.position import CostSpec
from beancount.utils import misc_utils

METADATA = Dict[str, Any]
Directive = Any

def new_directive(clsname: str, fields: List[str]) -> Directive: ...

class Booking(misc_utils.Enum):
    STRICT = ...  # type: str
    NONE = ...  # type: str
    AVERAGE = ...  # type: str
    FIFO = ...  # type: str
    LIFO = ...  # type: str

Open = NamedTuple('Open', [
    ('meta', METADATA),
    ('date', date),
    ('account', str),
    ('currencies', Optional[List[str]]),
    ('booking', Optional[Booking]),
])

Close = NamedTuple('Close', [
    ('meta', METADATA),
    ('date', date),
    ('account', str),
])

Commodity = NamedTuple('Commodity', [
    ('meta', METADATA),
    ('date', date),
    ('currency', str),
])

Pad = NamedTuple('Pad', [
    ('meta', METADATA),
    ('date', date),
    ('account', str),
    ('source_account', str),
])

Balance = NamedTuple('Balance', [
    ('meta', METADATA),
    ('date', date),
    ('account', str),
    ('amount', Amount),
    ('diff_amount', Amount),
    ('tolerance', Decimal),
])

Transaction = NamedTuple('Transaction', [
    ('meta', METADATA),
    ('date', date),
    ('flag', str),
    ('payee', Optional[str]),
    ('narration', str),
    ('tags', Optional[Set[str]]),
    ('links', Optional[Set[str]]),
    ('postings', List['Posting']),
])

Note = NamedTuple('Note', [
    ('meta', METADATA),
    ('date', date),
    ('account', str),
    ('comment', str),
])

Event = NamedTuple('Event', [
    ('meta', METADATA),
    ('date', date),
    ('type', str),
    ('description', str),
])

Query = NamedTuple('Query', [
    ('meta', METADATA),
    ('date', date),
    ('name', str),
    ('query_string', str),
])

Price = NamedTuple('Price', [
    ('meta', METADATA),
    ('date', date),
    ('currency', str),
    ('amount', Amount),
])

Document = NamedTuple('Document', [
    ('meta', METADATA),
    ('date', date),
    ('account', str),
    ('filename', str),
])

Custom = NamedTuple('Custom', [
    ('meta', METADATA),
    ('date', date),
    ('type', str),
    ('values', List[Any]),
])

ALL_DIRECTIVES = ...  # type: List[Directive]

Posting = NamedTuple('Posting', [
    ('meta', METADATA),
    ('date', date),
    ('entry', Transaction),
    ('account', str),
    ('units', Amount),
    ('cost', Union[Cost, CostSpec]),
    ('price', Amount),
    ('flag', Optional[str]),
])

def new_metadata(filename: str, lineno: int, kvlist: Optional[METADATA] = ...) -> METADATA: ...

TxnPosting = NamedTuple('TxnPosting', [
    ('txn', Transaction),
    ('posting', Posting),
])

def create_simple_posting(entry: Transaction, account: str, number: Union[Decimal, str], currency: str) -> Posting: ...
def create_simple_posting_with_cost(entry: Transaction, account: str, number: Union[Decimal, str], currency: str, cost_number: Union[Decimal, str], cost_currency: str) -> Posting: ...

NoneType = ...  # type: Any

def sanity_check_types(entry: Directive): ...
def posting_has_conversion(posting: Posting) -> bool: ...
def transaction_has_conversion(transaction: Transaction): ...
def get_entry(posting_or_entry: Union[TxnPosting, Transaction]): ...

SORT_ORDER = ...  # type: Dict[Any, int]

def entry_sortkey(entry: Directive) -> Tuple[date, int, int]: ...
def sorted(entries: List[Directive]) -> List[Any]: ...
def posting_sortkey(entry: Directive) -> Tuple[date, int, int]: ...
def filter_txns(entries: List[Directive]) -> Iterable[Transaction]: ...
def has_entry_account_component(entry: Directive, component: str) -> bool: ...
def find_closest(entries: List[Directive], filename: str, lineno: int) -> Directive: ...
def iter_entry_dates(entries: List[Directive], date_begin: date, date_end: date) -> Iterable[Directive]: ...
