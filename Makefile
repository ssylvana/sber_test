up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose build

run:
	uvicorn service:app  

test:
	pytest --cov=.

.PHONY: all test clean