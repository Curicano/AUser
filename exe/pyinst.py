import PyInstaller.__main__
PyInstaller.__main__.run([
    "main.py",
    "-i=..\..\image\logo.ico",
    "--distpath=exe",
    "--workpath=exe\Temp",
    "--specpath=exe\Temp",
    "-w",
    "-F",
    "-n=AUser",
    "--uac-admin",
    "--add-data=..\..\image;image",
    "--version-file=..\..\exe\\file_version.py"
])
