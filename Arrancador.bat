::Este batch levanta el servidor Django automaticamente
@echo off
cls

::Color y tamaño de ventana:
if not "%1" == "max" start /MAX cmd /c %0 max & exit/b
mode con:cols=170
color 08

::IP mediante web service
for /f "delims=[] tokens=2" %%a in ('ping -4 -n 1 %ComputerName% ^| findstr [') do set NetworkIP=%%a
for /f %%a in ('powershell Invoke-RestMethod api.ipify.org') do set PublicIP=%%a
TITLE DjangoSrvr:   ( IP Privada: %NetworkIP% )  -  ( IP Publica: %PublicIP% )

::Lo que respecta al servidor
@cd %CD%
cls
python manage.py runserver 0.0.0.0:8000