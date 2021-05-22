tests:
	docker exec -ti PatruAPI bash -c "cd test ; py.test -v --cov=src --cov-report term-missing"

html-coverage:
	cd test
	coverage html

docker-comp:
	sudo docker build -f PatruAPI/Dockerfile -t PatruAPI ./PatruAPI
	sudo docker-compose --compatibility up