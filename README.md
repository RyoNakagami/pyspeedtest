# pyspeedtest

This project is based on the original pyspeedtest by Matt Martz (licensed under the Apache License, Version 2.0).

Modifications and additional features © 2025 Ryo Nakagami.

## Description

`pyspeedtest` is a command-line tool for testing internet bandwidth using speedtest.net.
It retrieves server configurations, selects the best server based on latency,
and performs download and upload speed tests. Results can be displayed in various formats
such as simple text, CSV, or JSON.

## Installation

To install `pyspeedtest`, ensure you have Python 3.13 or higher installed. Then, use the following command:

```bash
uv tool install git+https://github.com/RyoNakagami/pyspeedtest
```

## Usage

Navigate to the `src/` directory and run the script:

```bash
uv run speedtest.py [options]
```

### Options

```bash
% uv run src/speedtest.py --help

 Usage: speedtest.py [OPTIONS]

 Run the full speedtest.net test

╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --no-download                                             Do not perform download test                         │
│ --no-upload                                               Do not perform upload test                           │
│ --single                --no-single                       Only use a single connection instead of multiple     │
│                                                           [default: no-single]                                 │
│ --bytes                                <TEXT INTEGER>...  Display values in bytes instead of bits              │
│                                                           [default: bit, 1]                                    │
│ --share                 --no-share                        Generate and provide a URL to the speedtest.net      │
│                                                           share results image                                  │
│                                                           [default: no-share]                                  │
│ --simple                --no-simple                       Suppress verbose output, only show basic information │
│                                                           [default: no-simple]                                 │
│ --json                                                    Output JSON                                          │
│ --server                               INTEGER            Specify a server ID to test against (multiple        │
│                                                           allowed)                                             │
│ --exclude                              INTEGER            Exclude a server from selection (multiple allowed)   │
│ --mini                                 TEXT               URL of the Speedtest Mini server                     │
│ --source                               TEXT               Source IP address to bind to                         │
│ --timeout                              FLOAT              HTTP timeout in seconds. Default 10 [default: 10.0]  │
│ --secure                --no-secure                       Use HTTPS instead of HTTP when communicating with    │
│                                                           speedtest.net operated servers                       │
│                                                           [default: no-secure]                                 │
│ --no-pre-allocate                                         Do not pre allocate upload data [default: True]      │
│ --version                                                 Show the version number and exit                     │
│ --install-completion                                      Install completion for the current shell.            │
│ --show-completion                                         Show completion for the current shell, to copy it or │
│                                                           customize the installation.                          │
│ --help                                                    Show this message and exit.                          │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Example

```bash
uv run speedtest.py --json
```

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear messages.
4. Submit a pull request.

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.

## References

- [Semantic Versioning](https://semver.org/)
- [Python Package Building Techniques for Regmonkeys > Versioning Policy](https://ryonakagami.github.io/python-statisticalpackage-techniques/posts/python-packaging-guide/versioning.html)
- [speedtest-cli](ttps://github.com/sivel/speedtest-cli)
