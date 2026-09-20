from pathlib import Path
import subprocess


def create_backup(uri: str, database: str, output_dir: str) -> str:
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["mongodump", f"--uri={uri}", f"--db={database}", f"--out={path}"],
        check=True,
        capture_output=True,
        text=True,
    )
    return str(path / database)


def restore_backup(uri: str, database: str, backup_path: str) -> None:
    source = Path(backup_path)
    if source.name != database:
        raise ValueError("O caminho do backup deve apontar para a pasta do banco informado")
    subprocess.run(
        ["mongorestore", f"--uri={uri}", "--drop", str(source)],
        check=True,
        capture_output=True,
        text=True,
    )
