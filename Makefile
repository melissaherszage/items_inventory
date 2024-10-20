# Makefile para levantar el servicio de airflow con Docker

# Comando para levantar el proyecto con Docker Compose
run-project:
	docker-compose up -d

# Comando para frenar el proyecto y eliminar los contenedores
stop:
	docker-compose down

# Comando para recrear el proyecto y empezar denuevo
rebuild:
	docker-compose up -d --build

# Comando para ver los logs
logs:
	docker-compose logs -f

# Comando para listar los dags que cree en airflow
list-dags:
	docker-compose exec webserver airflow dags list
