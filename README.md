# pyscan

A small dependency-free scanner for Python source files.

## Features

- Walk Python files recursively
- Collect imports and definitions
- Count lines and functions
- Produce JSON-friendly reports
- Read-only analysis

## Usage

```python
from pyscan import scan_source

report = scan_source("def hello():\n    return 'world'\n")
print(report)
```

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

## Credits

https://guns.lol/meduu
