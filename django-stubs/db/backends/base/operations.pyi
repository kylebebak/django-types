from datetime import (
    date,
    datetime,
    time,
    timedelta,
)
from decimal import Decimal
from django.contrib.auth.models import (
    Group,
    User,
)
from django.contrib.sites.models import Site
from django.core.management.color import Style
from django.db import DefaultConnectionProxy
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.sqlite3.base import DatabaseWrapper
from django.db.backends.utils import CursorWrapper
from django.db.models.base import Model
from django.db.models.expressions import Expression
from django.db.models.fields import Field
from django.db.models.sql.compiler import SQLCompiler
from typing import (
    Any,
    List,
    Optional,
    Set,
    Tuple,
    Type,
    Union,
)


class BaseDatabaseOperations:
    def __init__(
        self,
        connection: Union[DefaultConnectionProxy, backends.base.base.BaseDatabaseWrapper]
    ) -> None: ...
    def _get_limit_offset_params(self, low_mark: int, high_mark: Optional[int]) -> Tuple[int, int]: ...
    def adapt_datefield_value(self, value: Optional[date]) -> Optional[str]: ...
    def adapt_decimalfield_value(
        self,
        value: Optional[Decimal],
        max_digits: Optional[int] = ...,
        decimal_places: Optional[int] = ...
    ) -> Optional[str]: ...
    def adapt_ipaddressfield_value(self, value: Optional[str]) -> Optional[str]: ...
    def adapt_timefield_value(self, value: Optional[Union[datetime, time]]) -> Optional[str]: ...
    def adapt_unknown_value(self, value: Union[date, time, int, Decimal]) -> Union[str, int]: ...
    def autoinc_sql(self, table: str, column: str) -> None: ...
    def binary_placeholder_sql(self, value: Optional[memoryview]) -> str: ...
    def combine_expression(self, connector: str, sub_expressions: List[str]) -> str: ...
    def compiler(self, compiler_name: str) -> Type[SQLCompiler]: ...
    def convert_durationfield_value(
        self,
        value: Optional[float],
        expression: Expression,
        connection: DatabaseWrapper
    ) -> Optional[timedelta]: ...
    def date_extract_sql(self, lookup_type: None, field_name: None): ...
    def datetime_cast_date_sql(self, field_name: None, tzname: None): ...
    def datetime_trunc_sql(self, lookup_type: None, field_name: None, tzname: None): ...
    def distinct_sql(self, fields: List[str], params: None) -> Tuple[List[str], List[Any]]: ...
    def end_transaction_sql(self, success: bool = ...) -> str: ...
    def execute_sql_flush(self, using: str, sql_list: List[str]) -> None: ...
    def explain_query_prefix(self, format: None = ..., **options): ...
    def field_cast_sql(self, db_type: Optional[str], internal_type: str) -> str: ...
    def force_no_ordering(self) -> List[Any]: ...
    def get_db_converters(self, expression: Expression) -> List[Any]: ...
    def last_insert_id(self, cursor: CursorWrapper, table_name: str, pk_name: str) -> int: ...
    def limit_offset_sql(self, low_mark: int, high_mark: Optional[int]) -> str: ...
    def lookup_cast(self, lookup_type: str, internal_type: str = ...) -> str: ...
    def max_in_list_size(self) -> None: ...
    def max_name_length(self) -> None: ...
    def modify_insert_params(self, placeholder: str, params: Any) -> Any: ...
    def prep_for_like_query(self, x: str) -> str: ...
    def process_clob(self, value: str) -> str: ...
    def random_function_sql(self) -> str: ...
    def savepoint_commit_sql(self, sid: str) -> str: ...
    def savepoint_create_sql(self, sid: str) -> str: ...
    def savepoint_rollback_sql(self, sid: str) -> str: ...
    def sequence_reset_by_name_sql(self, style: None, sequences: List[Any]) -> List[Any]: ...
    def sequence_reset_sql(
        self,
        style: Style,
        model_list: Union[Set[Type[Model]], List[Type[Model]], Set[Type[Union[Group, User]]], List[Type[Site]]]
    ) -> List[Any]: ...
    def set_time_zone_sql(self) -> str: ...
    def tablespace_sql(self, tablespace: str, inline: bool = ...) -> str: ...
    def time_extract_sql(self, lookup_type: None, field_name: None): ...
    def time_trunc_sql(self, lookup_type: None, field_name: None): ...
    def unification_cast_sql(self, output_field: Field) -> str: ...
    def validate_autopk_value(self, value: int) -> int: ...
    def window_frame_rows_start_end(self, start: None = ..., end: None = ...): ...
    def year_lookup_bounds_for_date_field(self, value: int) -> List[str]: ...
    def year_lookup_bounds_for_datetime_field(self, value: int) -> List[str]: ...