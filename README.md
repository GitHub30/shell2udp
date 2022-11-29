[![Python](https://img.shields.io/pypi/pyversions/shell2udp.svg)](https://badge.fury.io/py/shell2udp)
[![PyPI](https://badge.fury.io/py/shell2udp.svg)](https://badge.fury.io/py/shell2udp)

# shell2udp
UDP-server to execute shell commands. Designed for development, prototyping or remote control. Settings through two command line arguments, path and shell command. By default bind to :8080.

# Usage

```bash
shell2udp [options] ["shell command" for /] /path "shell command" /path2 "shell command2" ...
options:
    -p, --port NNNN : port for udp server ( default 8080 )
```

# Install

```bash
pip install shell2udp
```

# Examples

## Windows

```powershell
shell2udp 'shutdown -s -t 0'
```

```powershell
shell2udp 'shutdown -s -t 0' /beep "powershell -c echo `a"
```

```powershell
shell2udp --port 3306 /beep 'powershell -command [Console]::Beep(440,2000)'
```

### Dispatch

```powershell
[System.Net.Sockets.UdpClient]::New().Send("", 0, "localhost", 8080)
```

```powershell
[System.Net.Sockets.UdpClient]::New().Send([System.Text.Encoding]::UTF8.GetBytes("/beep"), 5, "localhost", 8080)
# [System.Text.Encoding]::UTF8.GetBytes("/beep").Length
```

## Linux

```bash
shell2udp 'notify-send Hello root'
```


```bash
shell2udp -p3000 'notify-send Hello root' /path 'canberra-gtk-play -i desktop-login'
```

```bash
shell2udp -p3000 /path 'canberra-gtk-play -i desktop-login'
```

### Dispatch

```bash
echo > /dev/udp/localhost/8080
```

```bash
echo /path > /dev/udp/localhost/8080
```

# Acknowledgements

https://github.com/msoap/shell2http

https://github.com/eshaan7/Flask-Shell2HTTP
