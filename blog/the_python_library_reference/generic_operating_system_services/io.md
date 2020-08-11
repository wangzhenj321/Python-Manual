## Overview

There are three main types of I/O:

1. text I/O

    Text I/O expects and produces `str` objects. This means that whenever the backing store is natively made of bytes (such as in the case of a file), encoding and decoding of data is made transparently as well as optional translation of platform-specific newline characters.

2. binary I/O

    Binary I/O (also called buffered I/O) expects bytes-like objects and produces bytes objects. No encoding, decoding, or newline translation is performed. This category of streams can be used for all kinds of non-text data, and also when manual control over the handling of text data is desired.

3. raw I/O

    Raw I/O (also called unbuffered I/O) is generally used as a low-level building-block for binary and text streams; it is rarely useful to directly manipulate a raw stream from user code. Nevertheless, you can create a raw stream by opening a file in binary mode with buffering disabled.

A concrete object belonging to any of these categories is called a **file object**. Other common terms are **stream** and **file-like object**.

## Class hierarchy

| ABC | Inherits | Inherited by |
| --- | --- | --- |
| RawIOBase | IOBase | <ul><li>FileIO</li></ul> |
| BufferedIOBase | IOBase | <ul><li>BytesIO</li><li>BufferedReader</li><li>BufferedWriter</li><li>BufferedRandom</li><li>BufferedRWPair</li></ul> |
| TextIOBase | IOBase | <ul><li>TextIOWrapper</li><li>StringIO</li></ul> |
