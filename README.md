-   Problem statement

1.  Set up two local Python servers.

2.  On one of the servers, over the course of 10 minutes,
    generate 100 binary files of random sizes ranging from 1kb to 1Mb
    at random time intervals ranging from 1ms to 1s, encoded int16.

3.  Transfer those binary files as they are being generated
    from the first server to the second server over HTTP
    using Python's async io functionality, thereby effectively implementing
    data streaming from one server to the other.

-   Starting the server andn the client

```
% python server.py
```

and

```
% python client.py
```

in different terminals.

The client creates a file in the `in` directory and sends the data to the server. The server saves the file in the `out` directory.

-   Run tests

```
% python tests.py
```
