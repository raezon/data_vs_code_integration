@echo off
echo Installing libraries from instruction.txt...

if not exist instruction.txt (
    echo Error: instruction.txt not found!
    pause
    exit /b
)

for /f "tokens=*" %%i in (instruction.txt) do (
    echo Installing %%i...
    pip install %%i
)

echo Installation complete.
pause
