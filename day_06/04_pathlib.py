from pathlib import Path

ruta_carpeta = Path('/Users/glenn/PycharmProjects/PythonProject/day_06/File2.txt')

print(ruta_carpeta.name)
print(ruta_carpeta.stem)
print(ruta_carpeta.suffix)
print(ruta_carpeta.cwd())
print(ruta_carpeta.exists())
print(ruta_carpeta.read_text())