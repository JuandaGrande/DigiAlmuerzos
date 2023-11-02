@echo off
echo.
echo.
echo Instalando dependencias necesarias!!
echo.
echo.
timeout 2 >nul
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install -r rqs.txt
pause
echo.
echo.
echo Gracias por instalar DigiAlmuerzos!! Ya puedes usar el archivo autorun.bat
echo.
echo.
timeout 10