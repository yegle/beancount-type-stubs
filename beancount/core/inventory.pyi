# Stubs for beancount.core.inventory (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional, Union, Dict, List, Set, Tuple
from decimal import Decimal

from beancount.utils import misc_utils
from beancount.core.position import Position, Cost
from beancount.core.display_context import DisplayFormatter
from beancount.core.amount import Amount

class Booking(misc_utils.Enum):
    CREATED = ...  # type: int
    REDUCED = ...  # type: int
    AUGMENTED = ...  # type: int
    IGNORED = ...  # type: int

class Inventory(list):
    def __init__(self, positions: Optional[List[Position]] = ...) -> None: ...
    def to_string(self, dformat: DisplayFormatter = ..., parens: bool = ...) -> str: ...
    def is_empty(self) -> bool: ...
    def __bool__(self): ...
    def __copy__(self) -> 'Inventory': ...
    def __eq__(self, other: Inventory) -> bool: ...
    def is_small(self, tolerances: Union[Decimal, Dict[str, Decimal]], default_tolerances: Optional[Dict[str, Decimal]] = ...) -> bool: ...
    def is_mixed(self) -> bool: ...
    def is_reduced_by(self, ramount: Amount) -> bool: ...
    def __neg__(self) -> Inventory: ...
    def __mul__(self, scalar: Decimal) -> Inventory: ...
    def currencies(self) -> Set[str]: ...
    def cost_currencies(self) -> Set[str]: ...
    def currency_pairs(self) -> Set[Union[None, Tuple[str, str]]]: ...
    def get_positions(self) -> List[Position]: ...
    def get_units(self, currency: str) -> Amount: ...
    def segregate_units(self, currencies: str) -> Dict[str, Inventory]: ...
    def units(self) -> Inventory: ...
    def cost(self) -> Inventory: ...
    def average(self) -> Inventory: ...
    def add_amount(self, units: Amount, cost: Optional[Cost] = ...) -> Tuple[Position, Booking]: ...
    def add_position(self, position: Position) -> Tuple[Position, Booking]: ...
    def add_inventory(self, other: Inventory) -> Inventory: ...
    def __add__(self, other: Inventory) -> Inventory: ...
    __iadd__ = ...  # type: Callable[[Inventory, Inventory], Inventory]
    @staticmethod
    def from_string(string: str) -> Inventory: ...

from_string = ...  # type: Callable[[str], Inventory]

def check_invariants(inv: Inventory) -> bool: ...
def get_tolerance(tolerances: Dict[str, Decimal], default_tolerances: Dict[str, Decimal], currency: str) -> Decimal: ...
