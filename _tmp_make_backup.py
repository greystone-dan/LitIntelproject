from pathlib import Path
import zipfile
from datetime import datetime

root = Path('.').resolve()
backup_dir = root / 'backups'
backup_dir.mkdir(parents=True, exist_ok=True)
stamp = datetime.now().strftime('%Y%m%d-%H%M%S')
zip_path = backup_dir / f'AI-CaseLibrary-backup-{stamp}.zip'

exclude_roots = {'venv', '.git', 'backups', '__pycache__'}
exclude_parts = {'__pycache__'}

count = 0
with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED, allowZip64=True) as zf:
    for path in root.rglob('*'):
        rel = path.relative_to(root)
        if not rel.parts:
            continue
        if rel.parts[0] in exclude_roots:
            continue
        if any(part in exclude_parts for part in rel.parts):
            continue
        if path.is_file():
            zf.write(path, rel.as_posix())
            count += 1

print(f'backup_path={zip_path.relative_to(root).as_posix()}')
print(f'file_count={count}')
print(f'bytes={zip_path.stat().st_size}')
