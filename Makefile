install:
	poetry install

brain-games:
	poetry run brain-games

lint:
	poetry run flake8 brain_games