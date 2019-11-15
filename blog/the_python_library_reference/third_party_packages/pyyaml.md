## Installation

```
pip install pyyaml
```

## Example

- `dummy.yaml` sample file

    ```yaml
    GridType: PassCount
    Name: Default
    Scale:
    - UpperLimit: 1
        Color: PC1
    - UpperLimit: 2
        Color: PC2
    ```

- Load `dummy.yaml`

    ```python
    >>> import yaml
    >>> yml = yaml.load(open('dummy.yaml'), Loader=yaml.FullLoader)
    >>> type(yml)
    <class 'dict'>
    >>> yml
    {'GridType': 'PassCount', 'Name': 'Default', 'Scale': [{'UpperLimit': 1, 'Color': 'PC1'}, {'UpperLimit': 2, 'Color': 'PC2'}]}
    ```
