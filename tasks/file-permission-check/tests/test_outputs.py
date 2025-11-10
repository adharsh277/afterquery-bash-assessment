import subprocess
from pathlib import Path

def test_check_permissions_output():
    """
    Verifies that the user's script:
    1. Lists only files executable by the owner.
    2. Does not list non-executable files.
    3. Does not include directories.
    4. Outputs only filenames (no paths).
    5. Produces alphabetically sorted output (one per line).
    """
    workdir = Path("/app")
    script = workdir / "check_permissions.sh"

    # Create test files and directories
    (workdir / "run.sh").write_text("echo run")
    (workdir / "zeta.sh").write_text("echo zeta")
    (workdir / "data.txt").write_text("plain text")
    (workdir / "dir_test").mkdir(exist_ok=True)

    subprocess.run(["chmod", "700", "run.sh"])
    subprocess.run(["chmod", "700", "zeta.sh"])
    subprocess.run(["chmod", "600", "data.txt"])

    out = subprocess.check_output(["bash", str(script)]).decode().strip().split("\n")

    # 1. Executable files should appear
    assert "run.sh" in out
    assert "zeta.sh" in out

    # 2. Non-executable files should not appear
    assert "data.txt" not in out

    # 3. Directories should not appear
    assert "dir_test" not in out

    # 4. Output should contain only filenames (no paths)
    assert all("/" not in line for line in out)

    # 5. Output should be alphabetically sorted
    assert out == sorted(out)
