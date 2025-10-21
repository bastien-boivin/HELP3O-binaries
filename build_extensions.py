#!/usr/bin/env python
"""
Utility to build HELP3O.FOR as a Python extension.
Compatible with numpy.f2py and meson.
"""
import subprocess
import sys
import platform
from pathlib import Path

def build_help3o():
    """Compile HELP3O.FOR using numpy.f2py."""
    fortran_source = Path(__file__).parent / "HELP3O.FOR"

    if not fortran_source.exists():
        raise FileNotFoundError(f"HELP3O.FOR not found: {fortran_source}")

    print(f"Compiling {fortran_source}...")
    print(f"Python version: {sys.version}")
    print(f"Platform: {platform.system()}")

    # Build with f2py
    cmd = [
        sys.executable, '-m', 'numpy.f2py',
        '-c', '-m', 'HELP3O',
        str(fortran_source),
    ]

    # Add static linking flags for macOS to avoid runtime GCC dependencies
    if platform.system() == 'Darwin':
        # Static link GCC libraries so users don't need to install GCC
        static_flags = '-static-libgfortran -static-libquadmath -static-libgcc'
        cmd.extend(['--f90flags=' + static_flags])
        cmd.extend(['--f77flags=' + static_flags])
        print(f"macOS detected: adding static linking flags")

    print(f"Command: {' '.join(cmd)}")
    
    try:
        subprocess.run(cmd, check=True)
        print("Compilation succeeded.")
        
        # Locate the generated .so/.pyd file
        import glob
        binaries = glob.glob("HELP3O.*.so") + glob.glob("HELP3O.*.pyd")
        if binaries:
            print(f"Binary created: {binaries[0]}")
        else:
            print("Warning: binary file not found.")
            
    except subprocess.CalledProcessError as e:
        print(f"Compilation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    build_help3o()
