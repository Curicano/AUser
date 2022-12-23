import PyInstaller.__main__
PyInstaller.__main__.run([
    "D:\Storage X\About\IT\Python\Git\AUser\main.py",
    "-i=D:\Storage X\About\IT\Python\Git\AUser\image\logo.ico",
    "--distpath=D:\Storage X\About\IT\Python\Git\AUser\exe",
    "--workpath=D:\Storage X\About\IT\Python\Git\AUser\exe\Temp",
    "--specpath=D:\Storage X\About\IT\Python\Git\AUser\exe\Temp",
    "-w",
    "-F",
    "-n=AUser",
    "--uac-admin",
    "--add-data=D:\Storage X\About\IT\Python\Git\AUser\image;image",
    "--version-file=D:\Storage X\About\IT\Python\Git\AUser\exe\\file_version.py"
])
