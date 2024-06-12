py -m venv venv
call venv\Scripts\activate
rem set path to proxy
rem set path to proxy
python -m pip install --upgrade pip
pip install -r requirements.txt
pip freeze > freeze.txt
pause
