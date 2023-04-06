-include .env
export

db.restore.dump:
	@docker-compose exec -T mongo mongorestore -vvvvv -u ${MONGO_INITDB_ROOT_USERNAME} -p ${MONGO_INITDB_ROOT_PASSWORD} --dir data/dump

db.run:
	@docker-compose up -d mongo

bot.run:
	@python -m bot