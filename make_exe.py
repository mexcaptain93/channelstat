from cx_Freeze import setup, Executable

executables = [Executable('main.py')]

excludes = []

options = {
    'build_exe': {
        "packages": ["os"],
        "excludes": ["tkinter"],
        "include_files": ["input.txt", "result.txt"]
    }
}

setup(name='ChannelStat',
      version='0.1',
      description='ChannelStat App',
      executables=executables,
      options=options)