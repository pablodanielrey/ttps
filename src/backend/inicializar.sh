#!/bin/bash
docker-compose exec backend python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'nimda')"
curl -u admin:nimda http://localhost:8000/admin_api/inicializar
curl -u admin:nimda http://localhost:8000/admin_api/usuarios
