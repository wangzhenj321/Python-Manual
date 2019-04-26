This module defines classes which implement the client side of the HTTP and HTTPS protocols. It is normally not used directly — the module [`urllib.request`](./urllib_request.md) uses it to handle URLs that use HTTP and HTTPS.

> The [Requests package](./requests.md) is recommended for a higher-level HTTP client interface.

> HTTPS support is only available if Python was compiled with SSL support (through the `ssl` module).

# Workflow

## Step 1: Create an `HTTPConnection` instance

```python
>>> conn = http.client.HTTPSConnection("www.python.org")
```

## Step 2: Send a request

```python
>>> conn.request("GET", "/")
```

## Step 3: Get the response

```python
>>> r1 = conn.getresponse()
```

# Attributes

## `class http.client.HTTPConnection` (`HTTPSConnection`)

- `HTTPConnection.request(method, url, body=None, headers={}, *, encode_chunked=False)`
- `HTTPConnection.getresponse()`
- `HTTPConnection.connect()`
- `HTTPConnection.close()`

## `class http.client.HTTPResponse`

- `HTTPResponse.read([amt])`
- `HTTPResponse.getheader(name, default=None)`
- `HTTPResponse.status`
- `HTTPResponse.reason`
