# ttps
práctica de ttps

#genero un environment para instalar todas las dependencias
python3 -m venv .venv

#instalo django
source .venv/bin/activate
pip install django

#corro el ejemplo
cd ttps_test
ttps_test$ python3 manage.py runserver

