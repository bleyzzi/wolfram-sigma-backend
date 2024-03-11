up:
	docker compose -f docker-compose-wolfram-backend.yaml up -d

down:
	docker compose -f docker-compose-wolfram-backend.yaml down --remove-orphans && docker rm --force $(docker ps -q)

run:
	uvicorn main:app --reload

migrate:
	alembic revision --autogenerate