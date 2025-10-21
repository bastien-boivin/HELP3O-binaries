#!/usr/bin/env python
"""
Utility to build HELP3O.FOR as a Python extension.
Compatible with numpy.f2py and meson.
"""
import subprocess
import sys
from pathlib import Path

def build_help3o():
    """Compile HELP3O.FOR using numpy.f2py."""
    fortran_source = Path(__file__).parent / "HELP3O.FOR"
    
    if not fortran_source.exists():
        raise FileNotFoundError(f"HELP3O.FOR not found: {fortran_source}")
    
    print(f"Compiling {fortran_source}...")
    print(f"Python version: {sys.version}")
    
    # Build with f2py
    cmd = [
        sys.executable, '-m', 'numpy.f2py',
        '-c', '-m', 'HELP3O',
        str(fortran_source),
    ]
    
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
