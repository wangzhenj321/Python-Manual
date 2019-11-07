There are two kinds of date and time objects: "naive" and "aware".

The `datetime` module exports the following constants:

- `datetime.MINYEAR`
- `datetime.MAXYEAR`    

## Available Types

Subclass relationships:

```
object
    timedelta
    tzinfo
        timezone
    time
    date
        datetime
```

- Objects of these types are immutable.
- Objects of the `date` type are always naive.
- An object of type `time` or `datetime` may be naive or aware.
- The distinction between naive and aware doesn't apply to `timedelta` objects.

## `timedelta` Objects

```
class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
```

- Arguments may be integers or floats, and may be positive or negative.
- Only days, seconds and microseconds are stored internally.

Class attributes are:

- `timedelta.min`
- `timedelta.max`
- `timedelta.resolution`

Instance attributes (read-only):

- `days`
- `seconds`
- `microseconds`

Instance methods:

- `timedelta.total_seconds()`

## `date` Objects

```
class datetime.date(year, month, day)
```

- **POSIX timestamp**
    The Unix epoch (or Unix time or POSIX time or Unix timestamp) is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT), not counting leap seconds (in ISO 8601: 1970-01-01T00:00:00Z). Literally speaking the epoch is Unix time 0 (midnight 1/1/1970), but 'epoch' is often used as a synonym for Unix time. Some systems store epoch dates as a signed 32-bit integer, which might cause problems on January 19, 2038 (known as the Year 2038 problem or Y2038).

- **proleptic Gregorian ordinal**
    January 1 of year 1 has ordinal 1.

- **ISO 8601 strings**

Class methods:

- `date.today()`
- `date.fromtimestamp(timestamp)`
- `date.fromordinal(ordinal)`
- `date.fromisoformat(date_string)`

Class attributes:

- `date.min`
- `date.max`
- `date.resolution`

Instance attributes (read-only):

- `date.year`
- `date.month`
- `date.day`

Instance methods:

- `date.replace(year=self.year, month=self.month, day=self.day)`
- `date.timetuple()`
- `date.toordinal()`
- `date.weekday()` :vs: `date.isoweekday()`
- `date.isocalendar()`
- `date.isoformat()` :vs: `date.__str__()`
- `date.ctime()`
- `date.strftime(format)` :vs: `date.__format__(format)`

## `datetime` Objects

```
class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
```

Class methods:

- `datetime.today()` :vs: `datetime.now(tz=None)` :vs: `datetime.utcnow()`
- `datetime.fromtimestamp(timestamp, tz=None)` :vs: `datetime.utcfromtimestamp(timestamp)`
- `datetime.fromordinal(ordinal)`
- `datetime.fromisoformat(date_string)` :vs: `datetime.strptime(date_string, format)`
- `datetime.combine(date, time, tzinfo=self.tzinfo)`

Class attributes:

- `datetime.min`
- `datetime.max`
- `datetime.resolution`

Instance attributes (read-only):

- `datetime.year`
- `datetime.month`
- `datetime.day`
- `datetime.hour`
- `datetime.minute`
- `datetime.second`
- `datetime.microsecond`
- `datetime.tzinfo`
- `datetime.fold`

Instance methods:

- `datetime.date()`
- `datetime.time()` :vs: `datetime.timetz()`
- `datetime.replace(year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, * fold=0)`
- `datetime.astimezone(tz=None)`
- `datetime.utcoffset()`
- `datetime.dst()`
- `datetime.tzname()`
- `datetime.timetuple()` :vs: `datetime.utctimetuple()`
- `datetime.toordinal()`
- `datetime.timestamp()`
- `datetime.weekday()` :vs: `datetime.isoweekday()`
- `datetime.isocalendar()`
- `datetime.isoformat(sep='T', timespec='auto')` :vs: `datetime.__str__()`
- `datetime.ctime()`
- `datetime.strftime(format)` :vs: `datetime.__format__(format)`

## `time` Objects

```
class datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
```

Class methods:

- `time.fromisoformat(time_string)`

Class attributes:

- `time.min`
- `time.max`
- `time.resolution`

Instance attributes (read-only):

- `time.hour`
- `time.minute`
- `time.second`
- `time.microsecond`
- `time.tzinfo`
- `time.fold`

Instance methods:

- `time.replace(hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, * fold=0)`
- `time.isoformat(timespec='auto')` :vs: `time.__str__()`
- `time.strftime(format)` :vs: `time.__format__(format)`
- `time.utcoffset()`
- `time.dst()`
- `time.tzname()`

## `tzinfo` Objects

## `timezone` Objects

```
class datetime.timezone(offset, name=None)
```

Class attributes:

- `timezone.utc`

Instance methods:

- `timezone.utcoffset(dt)`
- `timezone.tzname(dt)`
- `timezone.dst(dt)`
- `timezone.fromutc(dt)`

## `strftime()` and `strptime()` Behavior

## Examples

## References

1. [datetime — Basic date and time types](https://docs.python.org/3.7/library/datetime.html#)
