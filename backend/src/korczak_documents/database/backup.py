from pathlib import Path
import subprocess


def create_backup(uri: str, database: str, output_dir: str) -> str:
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["mongodump", f"--uri={uri}", f"--db={database}", f"--out={path}"],
        check=True,
        capture_output=True,
        text=True,
    )
    return str(path)


def restore_backup(uri: str, database: str, backup_path: str) -> None:
    subprocess.run(
        ["mongorestore", f"--uri={uri}", f"--nsFrom={database}.*", f"--nsTo={database}.*", backup_path],
        check=True,
        capture_output=True,
        text=True,
    )
