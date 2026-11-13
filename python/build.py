"""Build on the target OS using this interpreter's installed dependencies."""

from pathlib import Path
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parent
    subprocess.run(
        [
            sys.executable, "-m", "PyInstaller",
            "--noconfirm", "--clean",
            "--distpath", str(root / "dist"),
            "--workpath", str(root / "build"),
            str(root / "chord-worker.spec"),
        ],
        cwd=root,
        check=True,
    )


if __name__ == "__main__":
    main()
