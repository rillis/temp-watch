@echo off

:inicial
if exist venv (goto initvenv) else (goto install)

:install
echo Instalando...
py -m venv venv
call venv\Scripts\activate
pip install pythonnet
goto init

:initvenv
call venv\Scripts\activate
goto init

:init
py main.py
