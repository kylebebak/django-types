from django.core.management.base import CommandParser
from typing import (
    List,
    Tuple,
)


def has_bom(fn: str) -> bool: ...


def is_writable(path: str) -> bool: ...


class Command:
    def add_arguments(self, parser: CommandParser) -> None: ...
    def compile_messages(self, locations: List[Tuple[str, str]]) -> None: ...
    def handle(self, **options) -> None: ...