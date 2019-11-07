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
