# PyHELP Fortran Binaries

Pre-built HELP3O Fortran extension binaries maintained for the HydroModPy ecosystem and available for anyone who needs ready-to-use wheels or shared objects.

## Purpose

This repository automates the compilation of the original `HELP3O.FOR` source so that HydroModPy installations—and any other projects that rely on HELP3O—can download a matching binary without compiling locally. Each tagged release on GitHub publishes the generated artifacts.

## Supported Platforms

- **Linux** (x86_64, manylinux2014)
  - Python 3.11, 3.12, 3.13
- **macOS** (Intel x86_64 and Apple Silicon arm64)
  - Python 3.11, 3.12, 3.13
- **Windows** (x86_64)
  - Python 3.11, 3.12, 3.13

## Binary Naming Convention

Compiled libraries follow standard CPython extension naming:

```
HELP3O.<python_tag>-<platform>.{so|pyd}
```

Examples:
- `HELP3O.cp311-cp311-linux_x86_64.so` – Linux, Python 3.11
- `HELP3O.cp312-cp312-macosx_11_0_arm64.so` – macOS ARM, Python 3.12
- `HELP3O.cp313-cp313-win_amd64.pyd` – Windows, Python 3.13

## Downloading Binaries

Every release attaches the compiled files so they can be fetched directly, reused by HydroModPy, or integrated into other tooling that expects a pre-built HELP3O module.

```bash
# Download the binary that matches your Python version and platform
wget https://github.com/bastien-boivin/HELP3O-binaries/releases/download/v1.0.0/HELP3O.cp311-cp311-linux_x86_64.so

# Make it available to your Python environment
mv HELP3O.*.so /path/to/your/project/
```

## Building Locally

```bash
# Install Python dependencies
pip install numpy

# Install a Fortran compiler
# Linux: sudo apt-get install gfortran
# macOS: brew install gcc
# Windows: choco install mingw

# Build the extension in-place
python build_extensions.py
```

## Contributing

Issues and pull requests that improve portability, add platforms, or enhance the release automation are welcome. Please coordinate before introducing breaking changes to the workflow matrix.

## License

Distributes the HELP3O binaries under the same license as the original PyHELP project. Refer to `LICENSE` for details.

## Credits

- HELP3O Fortran source courtesy of the PyHELP project
- Continuous integration and release automation by GitHub Actions
