#!/usr/bin/env python
"""
Utility to build HELP3O.FOR as a Python extension.
Compatible with numpy.f2py and meson.
"""
import os
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
    env = os.environ.copy()

    # Add static linking flags for macOS to avoid runtime GCC dependencies
    if platform.system() == 'Darwin':
        # Static link GCC libraries so users don't need to install GCC
        static_flags = '-static-libgfortran -static-libquadmath -static-libgcc'
        cmd.extend(['--f90flags=' + static_flags])
        cmd.extend(['--f77flags=' + static_flags])
        print(f"macOS detected: adding static linking flags")
    elif platform.system() == 'Windows':
        # Try to statically link the MinGW runtime to avoid shipping DLLs.
        # Some MinGW toolchains do not support -static-libssp, so rely on the default lib.
        static_link_flags = "-static -static-libgcc -static-libgfortran -static-libstdc++ -static-libquadmath"
        env["NPY_DISTUTILS_APPEND_FLAGS"] = "1"
        env["LDFLAGS"] = (env.get("LDFLAGS", "").strip() + " " + static_link_flags).strip()
        env["OPT"] = (env.get("OPT", "").strip() + " -static").strip()
        print("Windows detected: enabling static MinGW linking via LDFLAGS/OPT.")

    print(f"Command: {' '.join(cmd)}")
    
    try:
        subprocess.run(cmd, check=True, env=env)
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
