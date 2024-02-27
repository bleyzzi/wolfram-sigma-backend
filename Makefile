up:
	docker compose -f docker-compose-wolfram-backend.yaml up -d

down:
	docker compose -f docker-compose-wolfram-backend.yaml down --remove-orphans
