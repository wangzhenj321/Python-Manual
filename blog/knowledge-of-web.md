# HTTP

## HTTP Request Structure from Client

A simple request message from a client computer consists of the following components:

- A request line to get a required resource, for example a request GET /content/page1.html is requesting a resource called /content/page1.html from the server.

- Headers (Example – Accept-Language: EN).

- An empty line.

- A message body which is optional.

All the lines should end with a carriage return and line feed. The empty line should only contains carriage return and line feed without any spaces.

## HTTP Response Structure from Web Server

A simple response from the server contains the following components:

- HTTP Status Code (For example HTTP/1.1 301 Moved Permanently, means the requested resource was permanently moved and redirecting to some other resource).

- Headers (Example – Content-Type: html)

- An empty line.

- A message body which is optional.

All the lines in the server response should end with a carriage return and line feed. Similar to request, the empty line in a response also should only have carriage return and line feed without any spaces.
