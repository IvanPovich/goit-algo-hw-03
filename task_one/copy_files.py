import os
import shutil

def copy_files(src_dir, dest_dir):
  if not os.path.exists(src_dir):
        print(f"Директорія {src_dir} не існує.")
        return

  try:
    for root, _, files in os.walk(src_dir):

      for file in files:
        file_extension = os.path.splitext(file)[1][1:]
        if not file_extension:
          file_extension = "no_extension"

        dest_sub_dir = os.path.join(dest_dir, file_extension)
        os.makedirs(dest_sub_dir, exist_ok=True)

        src_file = os.path.join(root, file)
        dest_file = os.path.join(dest_sub_dir, file)

        shutil.copy2(src_file, dest_file)
        print(f"файл {src_file} скопійовано в {dest_file}")

  except OSError as e:
    print(f"Помилка доступу до файлів {e}")
  except Exception as e:
    print(f"Виникла помилка {e}")