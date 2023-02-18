from cx_freeze import setup, Executable

setup(name="Simple Object Detection Software",
      version="0.1",
      description = "This Software detects objects in Realtime",
      executable =[Executable("main.py")]
      )