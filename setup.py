from cx_Freeze import setup, Executable

setup(name="Quiz Game",
      version="1.0",
      description="anwer correct",
      executables=[Executable("quizgame.py")])
