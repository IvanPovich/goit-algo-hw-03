import argparse
from copy_files import copy_files

def main():
  parser = argparse.ArgumentParser(description="Рекурсивне копіювання і сортування файлів за розширенням")
  parser.add_argument("src_dir", help="Шлях до вихідної директорії")
  parser.add_argument("dest_dir", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням dist)")
  args = parser.parse_args()

  copy_files(args.src_dir, args.dest_dir)

if __name__ == "__main__":
  main()