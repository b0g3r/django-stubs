# Stubs for django.utils.timezone (Python 3.5)

from typing import Any, Optional, Union
from datetime import tzinfo, datetime, timedelta
from contextlib import ContextDecorator

class UTC(tzinfo):
    def utcoffset(self, dt: Optional[datetime]) -> Optional[timedelta]: ...
    def tzname(self, dt: Optional[datetime]) -> str: ...
    def dst(self, dt: Optional[datetime]) -> Optional[timedelta]: ...

class FixedOffset(tzinfo):
    def __init__(self, offset: int = None, name: str = None) -> None: ...
    def utcoffset(self, dt: Optional[datetime]) -> Optional[timedelta]: ...
    def tzname(self, dt: Optional[datetime]) -> str: ...
    def dst(self, dt: Optional[datetime]) -> Optional[timedelta]: ...

class ReferenceLocalTimezone(tzinfo):
    STDOFFSET = ...  # type: timedelta
    DSTOFFSET = ...  # type: timedelta
    DSTDIFF = ...  # type: timedelta
    def __init__(self) -> None: ...
    def utcoffset(self, dt: Optional[datetime]) -> Optional[timedelta]: ...
    def dst(self, dt: Optional[datetime]) -> Optional[timedelta]: ...
    def tzname(self, dt: Optional[datetime]) -> str: ...

class LocalTimezone(ReferenceLocalTimezone):
    def tzname(self, dt: Optional[datetime]) -> str: ...

utc = ...  # type: UTC

def get_fixed_timezone(offset: Union[timedelta, int]) -> tzinfo: ...
def get_default_timezone() -> tzinfo: ...
def get_default_timezone_name() -> str: ...
def get_current_timezone() -> tzinfo: ...
def get_current_timezone_name() -> str: ...
def activate(timezone: tzinfo) -> None: ...
def deactivate() -> None: ...

class override(ContextDecorator):
    timezone = ...  # type: tzinfo
    old_timezone = ...  # type: tzinfo
    def __init__(self, timezone: tzinfo) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: object, exc_value: object, traceback: object) -> None: ...

def localtime(value: datetime, timezone: tzinfo = None) -> datetime: ...
def now() -> datetime: ...
def is_aware(value: datetime) -> bool: ...
def is_naive(value: datetime) -> bool: ...
def make_aware(value: datetime, timezone: tzinfo = None, is_dst: bool = None) -> datetime: ...
def make_naive(value: datetime, timezone: tzinfo = None) -> datetime: ...