# HTTP

## HTTP message (Request or Response)

The request/response message consists of the following:

- Request line, such as `GET /logo.gif HTTP/1.1` or Status line, such as `HTTP/1.1 200 OK`
- Headers
- An empty line
- Optional HTTP message body data

The request/status line and headers must all end with `<CR><LF>` (that is, a carriage return followed by a line feed). The empty line must consist of only `<CR><LF>` and no other whitespace.

## HTTP header fields

### Request fields

| Header field name | Description | Example |
| --- | --- | --- |
| Accept | Media type(s) that is/are acceptable for the response. | `Accept: text/html` |
| Accept-Charset | Character sets that are acceptable. | `Accept-Charset: utf-8` |
| Accept-Encoding |	List of acceptable encodings. |	`Accept-Encoding: gzip, deflate` |
| Content-Length | The length of the request body in octets (8-bit bytes). | `Content-Length: 348` |
| Content-Type | The Media type of the body of the request (used with POST and PUT requests). | `Content-Type: application/x-www-form-urlencoded` |
| Host | The domain name of the server, and the TCP port number on which the server is listening. | `Host: en.wikipedia.org:8080` |

> [四种常见的 POST 提交数据方式](https://imququ.com/post/four-ways-to-post-data-in-http.html)
> 
> 1. `Content-Type: application/x-www-form-urlencoded;charset=utf-8`
> 2. `Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryrGKCBY7qhFd3TrwA`
> 3. `Content-Type: application/json;charset=utf-8`
> 4. `Content-Type: text/xml`

### Response fields

| Header field name | Description | Example |
| --- | --- | --- |
| Content-Encoding | The type of encoding used on the data. |	`Content-Encoding: gzip` |
| Content-Type | The MIME type of this content | `Content-Type: text/html; charset=utf-8` |
| Transfer-Encoding | The form of encoding used to safely transfer the entity to the user. | `Transfer-Encoding: chunked` |

> `Transfer-Encoding`: refer to https://imququ.com/post/transfer-encoding-header-in-http.html

## HTTP status codes

- 1xx (Informational): The request was received, continuing process
- 2xx (Successful): The request was successfully received, understood, and accepted
- 3xx (Redirection): Further action needs to be taken in order to complete the request
- 4xx (Client Error): The request contains bad syntax or cannot be fulfilled
- 5xx (Server Error): The server failed to fulfill an apparently valid request

## References

1. [What is HTTP, Structure of HTTP Request and Response?](https://www.webnots.com/what-is-http/)
2. [HTTP message body](https://en.wikipedia.org/wiki/HTTP_message_body)
3. [List of HTTP header fields](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)
4. [List of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
5. [HTTP](https://developer.mozilla.org/zh-CN/docs/Web/HTTP)
