import os
import platform
import shutil
from pathlib import Path

def get_external_drive_path():
    system = platform.system()

    if system == "Windows":
        # Scan all drives for "My Passport"
        from string import ascii_uppercase
        for drive in ascii_uppercase:
            path = Path(f"{drive}:/")
            if path.exists() and "My Passport" in os.popen(f'dir "{path}"').read():
                return path / "NexusBackup"
        return None

    elif system == "Darwin":  # macOS
        path = Path("/Volumes/My Passport/NexusBackup")
        return path if path.parent.exists() else None

    else:
        print("❌ Unsupported OS:", system)
        return None

def transfer_data():
    source = Path(__file__).resolve().parent / "data"
    destination = get_external_drive_path()

    if not source.exists():
        print("❌ Source folder 'data/' not found.")
        return

    if not destination:
        print("❌ External drive 'My Passport' not found.")
        return

    destination.mkdir(parents=True, exist_ok=True)
    print(f"📦 Transferring from: {source}")
    print(f"📁 To: {destination}")

    try:
        shutil.copytree(source, destination / "data", dirs_exist_ok=True)
        print("✅ Transfer complete!")
    except Exception as e:
        print("❌ Transfer failed:", e)

if __name__ == "__main__":
    transfer_data()
