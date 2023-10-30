from cx_Freeze import setup, Executable

options = {
    "build_exe": {
        "packages": ["chess"],  # Add any additional packages your script uses
    }
}

executables = [
    Executable("SciFish.py"),
    Executable("eval.py")
]

setup(
    name="SciFish",
    version="1.0",
    description="Aspiring to be great",
    executables=executables
)
