# port_scanner

A lightweight TCP port scanner in Python (standard library only). Scans a range
of ports on a host and reports each as **open**, **closed**, or **filtered**.

## How it works

For each port, it runs a full **TCP connect scan** via `socket.connect_ex()`:

- The OS completes the three-way handshake (SYN → SYN-ACK → ACK).
- Port state is read from the result:
  - `0` → handshake completed → **open**
  - `ECONNREFUSED` (RST received) → **closed**
  - timeout (packet silently dropped) → **filtered**

A 1-second `settimeout` bounds how long a filtered port can stall the scan.

> This is a *connect* scan, not a half-open *SYN* scan — it needs no root, but it
> completes the full handshake (less stealthy). A SYN scan would need raw sockets.

## Usage

​```bash
python3 p_scanner.py <host> <start_port> <end_port> [--open]
​```

- `--open` — print only open ports.

### Examples

​```bash
python3 p_scanner.py scanme.nmap.org 20 100
python3 p_scanner.py 127.0.0.1 1 1024 --open
​```

### Example output

​```
port 22 is open!
port 80 is open!
port 443 is filtered
​```

## Limitations

- **A middlebox can forge results.** On a network with a transparent proxy or
  captive portal, the proxy may answer the handshake for every destination, so
  *every* port looks open. Validate against a known-closed localhost port
  (`127.0.0.1:54321`) to confirm the network isn't lying.
- Single-threaded — large ranges are
