# What is this repository

Pythonの`traceback`の使い方について学ぶためのリポジトリです:
- [traceback --- スタックトレースの表示または取得 — Python 3.13.0 ドキュメント](https://docs.python.org/ja/3/library/traceback.html)


(`0x`の箇所は念の為ダミーの値を入れていますが、実際は生のオブジェクトのidが入力されます)

# When using just `print` in `./not_use_traceback.py`

```python
Hello from traceback-tmp!
A ValueError occurred
##########
division by zero
##########
math domain error
##########
HTTPConnectionPool(host='invalid-url', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x75***>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))
##########
```

# When using `traceback.print_exc()` in `./hello.py`

```python
Hello from traceback-tmp!
Exception caught in raise_value_error:
Traceback (most recent call last):
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/hello.py", line 8, in wrapper
    func(*args, **kwargs)
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/hello.py", line 17, in raise_value_error
    raise ValueError("A ValueError occurred")
ValueError: A ValueError occurred
##########
Exception caught in divide_by_zero:
Traceback (most recent call last):
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/hello.py", line 8, in wrapper
    func(*args, **kwargs)
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/hello.py", line 21, in divide_by_zero
    result = 1 / 0
             ~~^~~
ZeroDivisionError: division by zero
##########
Exception caught in math_domain_error:
Traceback (most recent call last):
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/hello.py", line 8, in wrapper
    func(*args, **kwargs)
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/hello.py", line 25, in math_domain_error
    result = math.sqrt(-1)
             ^^^^^^^^^^^^^
ValueError: math domain error
##########
Exception caught in simulate_connection_error:
Traceback (most recent call last):
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/.venv/lib/python3.12/site-packages/urllib3/connection.py", line 199, in _new_conn
    sock = connection.create_connection(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/.venv/lib/python3.12/site-packages/urllib3/util/connection.py", line 60, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<ROOT_DIRECTORY_PATH>/.local/share/uv/python/cpython-3.12.5-linux-x86_64-gnu/lib/python3.12/socket.py", line 976, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
socket.gaierror: [Errno -3] Temporary failure in name resolution

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/.venv/lib/python3.12/site-packages/urllib3/connectionpool.py", line 789, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/.venv/lib/python3.12/site-packages/urllib3/connectionpool.py", line 495, in _make_request
    conn.request(
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/.venv/lib/python3.12/site-packages/urllib3/connection.py", line 441, in request
    self.endheaders()
  File "<ROOT_DIRECTORY_PATH>/.local/share/uv/python/cpython-3.12.5-linux-x86_64-gnu/lib/python3.12/http/client.py", line 1331, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "<ROOT_DIRECTORY_PATH>/.local/share/uv/python/cpython-3.12.5-linux-x86_64-gnu/lib/python3.12/http/client.py", line 1091, in _send_output
    self.send(msg)
  File "<ROOT_DIRECTORY_PATH>/.local/share/uv/python/cpython-3.12.5-linux-x86_64-gnu/lib/python3.12/http/client.py", line 1035, in send
    self.connect()
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/.venv/lib/python3.12/site-packages/urllib3/connection.py", line 279, in connect
    self.sock = self._new_conn()
                ^^^^^^^^^^^^^^^^
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/.venv/lib/python3.12/site-packages/urllib3/connection.py", line 206, in _new_conn
    raise NameResolutionError(self.host, self, e) from e
urllib3.exceptions.NameResolutionError: <urllib3.connection.HTTPConnection object at 0x99***>: Failed to resolve 'invalid-url' ([Errno -3] Temporary failure in name resolution)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/.venv/lib/python3.12/site-packages/requests/adapters.py", line 667, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/.venv/lib/python3.12/site-packages/urllib3/connectionpool.py", line 843, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/.venv/lib/python3.12/site-packages/urllib3/util/retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='invalid-url', port=80): Max retries exceeded with url: / (Caused by NameResolutionError("<urllib3.connection.HTTPConnection object at 0x99***>: Failed to resolve 'invalid-url' ([Errno -3] Temporary failure in name resolution)"))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/hello.py", line 8, in wrapper
    func(*args, **kwargs)
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/hello.py", line 33, in simulate_connection_error
    requests.get('http://invalid-url')
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/.venv/lib/python3.12/site-packages/requests/api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/.venv/lib/python3.12/site-packages/requests/api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/.venv/lib/python3.12/site-packages/requests/sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/.venv/lib/python3.12/site-packages/requests/sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<CURRENT_DIRECTRY_PATH>traceback_tmp/.venv/lib/python3.12/site-packages/requests/adapters.py", line 700, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='invalid-url', port=80): Max retries exceeded with url: / (Caused by NameResolutionError("<urllib3.connection.HTTPConnection object at 0x99***>: Failed to resolve 'invalid-url' ([Errno -3] Temporary failure in name resolution)"))
##########
```
