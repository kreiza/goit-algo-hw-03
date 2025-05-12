import argparse
import os
import shutil


def copy_and_sort_files(source_dir, dest_dir="dist"):
    try:
        os.makedirs(dest_dir, exist_ok=True)
        _copy_recursive(source_dir, dest_dir)
    except Exception as e:
        print(f"[Помилка] {e}")


def _copy_recursive(current_dir, dest_dir):
    try:
        for entry in os.listdir(current_dir):
            path = os.path.join(current_dir, entry)
            if os.path.isdir(path):
                _copy_recursive(path, dest_dir)
            elif os.path.isfile(path):
                ext = os.path.splitext(entry)[1][1:] or "no_extension"
                target_folder = os.path.join(dest_dir, ext)
                os.makedirs(target_folder, exist_ok=True)
                shutil.copy2(path, os.path.join(target_folder, entry))
                print(f"[✓] Копійовано: {path} → {target_folder}")
    except PermissionError:
        print(f"[Пропущено] Немає доступу до: {current_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Копіювання і сортування файлів за розширенням."
    )
    parser.add_argument("source", help="Шлях до вихідної директорії")
    parser.add_argument(
        "dest",
        nargs="?",
        default="dist",
        help="Шлях до директорії призначення (за замовчуванням dist)",
    )
    args = parser.parse_args()

    copy_and_sort_files(args.source, args.dest)
