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

#crear el login. ej
python3 manage.py startapp persons


#probar usando oauth como autenticación.
#https://django-oauth-toolkit.readthedocs.io/

---

generar las tablas para el modelo de una app.

(.venv) pablo@xiaomi:/src/github/facu-infor/ttps/ttps_test$ python3 manage.py makemigrations persons
Migrations for 'persons':
  persons/migrations/0001_initial.py
    - Create model IdentificationType
    - Create model Person
    - Create model Identification
(.venv) pablo@xiaomi:/src/github/facu-infor/ttps/ttps_test$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, persons, sessions
Running migrations:
  Applying persons.0001_initial... OK
(.venv) pablo@xiaomi:/src/github/facu-infor/ttps/ttps_test$ 


muy buena referencia a como manejar las relaciones en las consultas.
https://stackoverflow.com/questions/7495126/django-model-foreignkeys-question

dado:
class Employees(models.Model):
    ...

class Expenses(models.Model):
    ...
    employee = models.ForeignKey(Employees)


1 -
employee = Employee.objects.get(name='John Doe')
employee_expenses = employee.expenses.all()

2- 
employee_expenses = Employee.objects.get(name='John Doe').expenses.all()

3-
employee_expenses = Expense.objects.filter(employee__name="John Doe")

el __ desreferencia el objeto employee