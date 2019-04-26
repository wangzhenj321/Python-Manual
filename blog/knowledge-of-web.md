# HTTP

## HTTP message (Request or Response)

The request/response message consists of the following:

- Request line, such as `GET /logo.gif HTTP/1.1` or Status line, such as `HTTP/1.1 200 OK`
- Headers
- An empty line
- Optional HTTP message body data

The request/status line and headers must all end with `<CR><LF>` (that is, a carriage return followed by a line feed). The empty line must consist of only `<CR><LF>` and no other whitespace.

## References

1. [What is HTTP, Structure of HTTP Request and Response?](https://www.webnots.com/what-is-http/)
