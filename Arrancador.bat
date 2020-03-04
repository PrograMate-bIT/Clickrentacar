::Este batch levanta el servidor Django automaticamente
echo off
cls

::Color y tamaño de ventana:
color 08
mode con:cols=110 lines=30

::IP mediante web service
for /f "delims=[] tokens=2" %%a in ('ping -4 -n 1 %ComputerName% ^| findstr [') do set NetworkIP=%%a
for /f %%a in ('powershell Invoke-RestMethod api.ipify.org') do set PublicIP=%%a
TITLE DjangoSrvr:   ( IP Privada: %NetworkIP% )  -  ( IP Publica: %PublicIP% )

::Lo que respecta al servidor
cd %CD%
cls
python manage.py runserver 127.0.0.1:8000