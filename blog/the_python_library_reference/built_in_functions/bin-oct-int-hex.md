## Example 1

```python
bin_num = 0b10
oct_num = 0o10
hex_num = 0x10

print(bin_num)  # 2
print(oct_num)  # 8
print(hex_num)  # 16

print(type(bin_num))    # <class 'int'>
print(type(oct_num))    # <class 'int'>
print(type(hex_num))    # <class 'int'>
```

## Example 2

```python
i = 255

bin_str = bin(i)
oct_str = oct(i)
hex_str = hex(i)

print(bin_str)  # 0b11111111
print(oct_str)  # 0o377
print(hex_str)  # 0xff

print(type(bin_str))    # <class 'str'>
print(type(oct_str))    # <class 'str'>
print(type(hex_str))    # <class 'str'>
```

## References

1. [Pythonで2進数、8進数、16進数の数値・文字列を相互に変換](https://note.nkmk.me/python-bin-oct-hex-int-format/)
