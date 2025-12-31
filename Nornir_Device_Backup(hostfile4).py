from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from datetime import datetime
from pathlib import Path

BACKUP_DIR = Path("backups")

def backup_device(task):
    backup_data = task.host.data.get("backup")
    if not backup_data:
        return

    BACKUP_DIR.mkdir(exist_ok=True)
    device_dir = BACKUP_DIR / task.host.name
    device_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    for command in backup_data.get("commands", []):
        result = task.run(
            task=send_command,
            command=command
        )

        safe_cmd = command.replace(" ", "_")
        file_path = device_dir / f"{safe_cmd}_{timestamp}.txt"

        file_path.write_text(result.result)

nr = InitNornir(config_file="config.yaml")
nr.run(task=backup_device)
