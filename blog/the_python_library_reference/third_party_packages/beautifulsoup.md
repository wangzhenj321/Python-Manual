**Table of Contents**

- [Installing a parser](#installing-a-parser)

- [Making the soup](#making-the-soup)

- [Kinds of objects](#kinds-of-objects)

- [Navigating the tree](#navigating-the-tree)

- [Searching the tree](#searching-the-tree)

## Installing a parser

1. HTML parser

    Beautiful Soup supports the HTML parser included in Python's standard library.

2. lxml parser

    ```
    pip install lxml
    ```

3. html5lib parser

    ```
    pip install html5lib
    ```

This table summarizes the typical usage of each parser library:

| Parser | Typical usage |
| --- | --- |
| Python's html.parser | `BeautifulSoup(markup, "html.parser")` |
| lxml's HTML parser | `BeautifulSoup(markup, "lxml")` |
| lxml's XML parser | `BeautifulSoup(markup, "lxml-xml")` `BeautifulSoup(markup, "xml")` |
| html5lib | `BeautifulSoup(markup, "html5lib")` |

## Making the soup

> Beautiful Soup then parses the document using the best available parser. It will use an HTML parser unless you specifically tell it to use an XML parser.

1. Pass in a string

    ```python
    soup = BeautifulSoup("<html>data</html>")
    ```

2. Pass an open filehandle

    ```python
    with open("index.html") as fp:
        soup = BeautifulSoup(fp)
    ```

## Kinds of objects

1. `Tag`

    - Name
    - Attributes
    
        > You can access a tag's attributes by treating the tag like a dictionary.
        
        ```python
        tag['id']
        # KeyError: 'id'
        print(tag.get('id'))
        # None
        ```

2. `NavigableString`

3. `BeautifulSoup`

4. `Comment`

## Navigating the tree

## Searching the tree

- `find_all()`

    > `find_all(name, attrs, recursive, string, limit, **kwargs)`
    
    - The `name` argument
    
        Pass in a value for `name` and you'll tell Beautiful Soup to only consider tags with certain names. Text strings will be ignored, as will tags whose names that don't match.
        
        ```python
        soup.find_all("title")
        # [<title>The Dormouse's story</title>]
        ```
    
    - The keyword arguments
    
        If you pass in a value for an argument called `id`, Beautiful Soup will filter against each tag's `id` attribute:
        
        ```python
        soup.find_all(id='link2')
        # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
        ```
        
        You can use these attributes in searches by putting them into a dictionary and passing the dictionary into `find_all()` as the `attrs` argument:
        
        ```python
        data_soup.find_all(attrs={"data-foo": "value"})
        # [<div data-foo="value">foo!</div>]
        ```
