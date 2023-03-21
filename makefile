run:
	docker-compose up --build

clean:
	docker-compose down --rmi all --volumes --remove-orphans

shell:
	docker-compose exec app sh
