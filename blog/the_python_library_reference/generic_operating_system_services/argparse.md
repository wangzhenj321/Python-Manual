The program defines what arguments it requires, and `argparse` will figure out how to parse those out of `sys.argv`.

> The `argparse` module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.

## Example

### Step 1: Creating a parser

The first step in using the `argparse` is creating an `ArgumentParser` object:

```python
>>> parser = argparse.ArgumentParser(description='Process some integers.')
```

The `ArgumentParser` object will hold all the information necessary to parse the command line into Python data types.

### Step 2: Adding arguments

The calls to `add_argument()` tell the `ArgumentParser` how to take the strings on the command line and turn them into objects. This information is stored and used when `parse_args()` is called.

```python
>>> parser.add_argument('integers', metavar='N', type=int, nargs='+',
...                     help='an integer for the accumulator')
>>> parser.add_argument('--sum', dest='accumulate', action='store_const',
...                     const=sum, default=max,
...                     help='sum the integers (default: find the max)')
```

### Step 3: Parsing arguments

`ArgumentParser` parses arguments through the `parse_args()` method.

```python
>>> parser.parse_args(['--sum', '7', '-1', '42'])
Namespace(accumulate=<built-in function sum>, integers=[7, -1, 42])
```

In a script, `parse_args()` will typically be called with no arguments, and the `ArgumentParser` will automatically determine the command-line arguments from `sys.argv`.

## `argparse.ArgumentParser` objects

Create a new `ArgumentParser` object. All parameters should be passed as keyword arguments.

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

## The `ArgumentParser.add_argument()` method

Define how a single command-line argument should be parsed.

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

## The `ArgumentParser.parse_args()` method

Convert argument strings to objects and assign them as attributes of the namespace. Return the populated namespace.

| Parameters | Description |
| --- | --- |
| args | List of strings to parse. The default is taken from `sys.argv`. |
| namespace | An object to take the attributes. The default is a new empty `Namespace` object. |

### The `argparse.Namespace` object

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

## Other utilities

### Sub-commands: `ArgumentParser.add_subparsers()`

Many programs split up their functionality into a number of sub-commands, for example, the `svn` program can invoke sub-commands like `svn checkout`, `svn update`, and `svn commit`. Splitting up functionality this way can be a particularly good idea when a program performs several different functions which require different kinds of command-line arguments. `ArgumentParser` supports the creation of such sub-commands with the `add_subparsers()` method. The `add_subparsers()` method is normally called with no arguments and returns a special action object. This object has a single method, `add_parser()`, which takes a command name and any `ArgumentParser` constructor arguments, and returns an `ArgumentParser` object that can be modified as usual.

| Parameters | Description |
| --- | --- |
| title | title for the sub-parser group in help output; by default "subcommands" if description is provided, otherwise uses title for positional arguments |
| description | description for the sub-parser group in help output, by default `None` |
| prog | usage information that will be displayed with sub-command help, by default the name of the program and any positional arguments before the subparser argument |
| parser_class | class which will be used to create sub-parser instances, by default the class of the current parser (e.g. ArgumentParser) |
| action | the basic type of action to be taken when this argument is encountered at the command line |
| dest | name of the attribute under which sub-command name will be stored; by default `None` and no value is stored |
| required | Whether or not a subcommand must be provided, by default `False` (added in 3.7) |
| help | help for sub-parser group in help output, by default `None` |
| metavar | string presenting available sub-commands in help; by default it is None and presents sub-commands in form {cmd1, cmd2, ..} |

### Argument groups: `ArgumentParser.add_argument_group()`

By default, `ArgumentParser` groups command-line arguments into "positional arguments" and "optional arguments" when displaying help messages. When there is a better conceptual grouping of arguments than this default one, appropriate groups can be created using the `add_argument_group()` method. When an argument is added to the group, the parser treats it just like a normal argument, but displays the argument in a separate group for help messages. Note that any arguments not in your user-defined groups will end up back in the usual "positional arguments" and "optional arguments" sections.

### Parser defaults

- `ArgumentParser.set_defaults()`

- `ArgumentParser.get_default()`

### Printing help

- `ArgumentParser.print_help()`
