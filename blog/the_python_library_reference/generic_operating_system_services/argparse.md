The program defines what arguments it requires, and `argparse` will figure out how to parse those out of `sys.argv`.

> The `argparse` module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.

# Workflow

## Step 1: Creating a parser

The first step in using the `argparse` is creating an `ArgumentParser` object:

```python
>>> parser = argparse.ArgumentParser(description='Process some integers.')
```

## Step 2: Adding arguments

The calls to `add_argument()` tell the `ArgumentParser` how to take the strings on the command line and turn them into objects.

```python
>>> parser.add_argument('integers', metavar='N', type=int, nargs='+',
...                     help='an integer for the accumulator')
>>> parser.add_argument('--sum', dest='accumulate', action='store_const',
...                     const=sum, default=max,
...                     help='sum the integers (default: find the max)')
```

## Step 3: Parsing arguments

`ArgumentParser` parses arguments through the `parse_args()` method.

```python
>>> parser.parse_args(['--sum', '7', '-1', '42'])
Namespace(accumulate=<built-in function sum>, integers=[7, -1, 42])
```

# Attributes

## `class argparse.ArgumentParser`

Create a new `ArgumentParser` object.

> All parameters should be passed as keyword arguments.

| Parameters | Description |
| --- | --- |
| prog | The name of the program (default: `sys.argv[0]`) |
| usage | The string describing the program usage (default: generated from arguments added to parser) |
| description | Text to display before the argument help (default: none) |
| epilog | Text to display after the argument help (default: none) |
| parents | A list of ArgumentParser objects whose arguments should also be included |
| formatter_class | A class for customizing the help output |
| prefix_chars | The set of characters that prefix optional arguments (default: '-') |
| fromfile_prefix_chars | The set of characters that prefix files from which additional arguments should be read (default: None) |
| argument_default | The global default value for arguments (default: None) |
| conflict_handler | The strategy for resolving conflicting optionals (usually unnecessary) |
| add_help | Add a `-h/--help` option to the parser (default: True) |
| allow_abbrev | Allows long options to be abbreviated if the abbreviation is unambiguous. (default: True) |

## `ArgumentParser.add_argument`

Define how a single command-line argument should be parsed.

> When `parse_args()` is called, optional arguments will be identified by the `-` prefix, and the remaining arguments will be assumed to be positional.

| Parameters | Description |
| --- | --- |
| name or flags | Either a name or a list of option strings, e.g. `foo` or `-f, --foo`. |
| action | The basic type of action to be taken when this argument is encountered at the command line. |
| nargs | The number of command-line arguments that should be consumed. |
| const | A constant value required by some action and nargs selections. |
| default | The value produced if the argument is absent from the command line. |
| type | The type to which the command-line argument should be converted. |
| choices | A container of the allowable values for the argument. |
| required | Whether or not the command-line option may be omitted (optionals only). |
| help | A brief description of what the argument does. |
| metavar | A name for the argument in usage messages. |
| dest | The name of the attribute to be added to the object returned by `parse_args()`. |

## `ArgumentParser.parse_args`

Convert argument strings to objects and assign them as attributes of the namespace. Return the populated namespace.

| Parameters | Description |
| --- | --- |
| args | List of strings to parse. The default is taken from `sys.argv`. |
| namespace | An object to take the attributes. The default is a new empty `Namespace` object. |

## `class argparse.Namespace`

Simple class used by default by `parse_args()` to create an object holding attributes and return it.

**Example 1**

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> args = parser.parse_args(['--foo', 'BAR'])
>>> vars(args)
{'foo': 'BAR'}
```

**Example 2**

```python
>>> class C:
...     pass
...
>>> c = C()
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> parser.parse_args(args=['--foo', 'BAR'], namespace=c)
>>> c.foo
'BAR'
```
