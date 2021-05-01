tests:
	docker exec -ti features bash -c "cd test ; py.test -v --cov=src --cov-report term-missing"

html-coverage:
	cd test
	coverage html

docker-comp:
	sudo docker build -f features/Dockerfile -t features ./features
	sudo docker-compose --compatibility up


