tests:
	docker exec -ti patruapi bash -c "cd test ; py.test -v --cov=src --cov-report term-missing"

html-coverage:
	cd test
	coverage html

docker-comp:
	sudo docker build -f patrulha/Dockerfile -t patruapi ./patrulha
	sudo docker-compose --compatibility up

docker-win:
	docker build -f patrulha/Dockerfile -t patruapi ./patrulha
	docker-compose --compatibility up