up:
	docker compose --file shared/docker/docker-compose.yml up --build

flag:
	curl -X POST -d "flag=$(flag)" http://localhost:1337/submit
