from hashlib import sha256
from importlib.metadata import distributions
from importlib.util import find_spec
from pathlib import Path
import sys
import tomllib

from PyInstaller.utils.hooks import collect_all, collect_data_files, copy_metadata

root = Path(SPECPATH)
package = Path(find_spec("lv_chordia").origin).parent
config = package / "config" / "checkpoints.toml"
entries = tomllib.loads(config.read_text(encoding="utf-8"))["models"]["lv_chordia"]["artifacts"]
weights = Path(sys.prefix) / "share" / "lv-chordia" / "weights"
if not weights.is_dir():
    weights = package.parent / "weights"

datas = collect_data_files("lv_chordia") + copy_metadata("cadence-chord-worker", recursive=True)

# Recursive metadata collection omits CUDA toolkit dependencies behind extras markers.
for distribution in distributions():
    name = distribution.metadata["Name"]
    if name.lower().startswith("nvidia-"):
        datas += copy_metadata(name)

for entry in entries:
    checkpoint = weights / entry["name"]
    if not checkpoint.is_file():
        raise RuntimeError(f"Missing checkpoint: {checkpoint}")
    with checkpoint.open("rb") as handle:
        digest = sha256(handle.read()).hexdigest()
    if digest != entry["sha256"]:
        raise RuntimeError(f"Checkpoint checksum mismatch: {checkpoint}")
    datas.append((str(checkpoint), "share/lv-chordia/weights"))

librosa_data, librosa_binaries, librosa_imports = collect_all("librosa")
a = Analysis(
    [str(root / "worker.py")],
    pathex=[str(root)],
    binaries=librosa_binaries,
    datas=datas + librosa_data,
    hiddenimports=librosa_imports,
    runtime_hooks=[str(root / "frozen_resources.py")],
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="chord-worker",
    console=True,
)
coll = COLLECT(exe, a.binaries, a.datas, name="chord-worker")
