import os
import sys

python_path = os.path.dirname(sys.executable)

python_version = sys.version

print(f'Путь к интерпретатору {python_path}, версия {python_version}')
