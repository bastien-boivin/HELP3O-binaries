# PyHELP Fortran Binaries

Pre-built HELP3O Fortran extension binaries maintained for the HydroModPy ecosystem and available for anyone who needs ready-to-use shared libraries.

## Purpose

This repository automates the compilation of the original `HELP3O.FOR` source so HydroModPy and other tools that rely on HELP3O can download a matching binary without compiling locally. Each workflow run creates a dated GitHub Release (for example `v2025.10`) that bundles all supported platform builds.

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
- `HELP3O.cpython-311-x86_64-linux-gnu.so` – Linux, Python 3.11
- `HELP3O.cpython-312-macosx_arm64.so` – macOS ARM, Python 3.12
- `HELP3O.cp313-win_amd64.pyd` – Windows, Python 3.13

## Downloading Binaries

Every release attaches the compiled files so they can be fetched directly, reused by HydroModPy, or integrated into other tooling that expects a pre-built HELP3O module. Visit the [Releases page](https://github.com/bastien-boivin/HELP3O-binaries/releases) and download the asset that matches your Python version, platform and architecture. The checksums listed alongside each asset can be used to verify the download.

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

## Publishing A New Release (maintainers)

Only maintainers with write access to this repository can publish a new set of binaries:

1. Ensure the latest changes are pushed to `main`.
2. Open GitHub → **Actions** → workflow **Build HELP3O Binaries** → **Run workflow** (keep the default branch).
3. Wait for all matrix jobs to succeed; the workflow will automatically create a release tagged `vYYYY.MM` (or append `-RUN` if one already exists) and attach the 12 binaries.
4. Share the release URL with downstream projects such as HydroModPy so they can retrieve the new artifacts.

## Contributing

Issues and pull requests that improve portability, add platforms, or enhance the release automation are welcome. Please coordinate before introducing breaking changes to the workflow matrix.

## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for the full text. Original HELP3O Fortran sources remain under the PyHELP project’s licensing terms.

## Credits

- HELP3O Fortran source courtesy of the PyHELP project
- Continuous integration and release automation by GitHub Actions
