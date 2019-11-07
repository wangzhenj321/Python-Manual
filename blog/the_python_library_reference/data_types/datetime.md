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

## `time` Objects

## `tzinfo` Objects

## `timezone` Objects
