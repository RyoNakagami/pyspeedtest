# pyspeedtest

## Description

`pyspeedtest` is a command-line tool for testing internet bandwidth using speedtest.net.
It retrieves server configurations, selects the best server based on latency,
and performs download and upload speed tests. Results can be displayed
in various formats such as simple text, CSV, or JSON.

## Installation

To install `pyspeedtest`, ensure you have Python 3.13 or higher installed.
Then, use the following command:

```bash
uv tool install git+https://github.com/RyoNakagami/pyspeedtest
```

## Usage

Navigate to the `src/` directory and run the script:

```bash
uv run speedtest.py [options]
```

### Options

- `--no-download`: Do not perform download test.
- `--no-upload`: Do not perform upload test.
- `--single`: Use a single connection for testing.
- `--bytes`: Display results in bytes instead of bits.
- `--share`: Generate a shareable URL for results.
- `--simple`: Display basic information only.
- `--csv`: Output results in CSV format.
- `--csv-delimiter`: Specify a delimiter for CSV output.
- `--csv-header`: Include headers in CSV output.
- `--json`: Output results in JSON format.
- `--list`: List available speedtest.net servers.
- `--server`: Specify server ID(s) to test against.
- `--exclude`: Exclude specific server ID(s).
- `--mini`: Use a Speedtest Mini server.
- `--source`: Specify source IP address.
- `--timeout`: Set HTTP timeout (default: 10 seconds).
- `--secure`: Use HTTPS for communication.
- `--no-pre-allocate`: Disable pre-allocation of upload data.
- `--version`: Display the script version and exit.

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
