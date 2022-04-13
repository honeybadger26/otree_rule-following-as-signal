# Thesis

## Instructions
- Download and install [Docker](https://www.docker.com/products/docker-desktop/)
- `cd` to this folder and run:
```
docker-compose up
```
- In your browser, go to [localhost:8000](http://localhost:8000)

## Notes
- If something goes wrong with the `docker-compose` command try the below command instead:
```
docker-compose down && docker-compose up --build --force-recreate
```

## Tests
To run tests, use the following:
```
docker-compose build && docker-compose run otree test
```
- Note 1: To run a specific test, add the test name to the end of `otree test`
- Note 2: If you have already built the image you can omit the `docker-compose build` command

## Todo
- [ ] Left align all text
- [ ] Enable Dictator block only
