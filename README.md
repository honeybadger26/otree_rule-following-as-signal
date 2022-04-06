# Thesis

## Instructions
- Download and install [Docker](https://www.docker.com/products/docker-desktop/)
- `cd` to this folder and run:
```
docker-compose up --build
```
- In your browser, go to [localhost:8000](http://localhost:8000)

## Notes
- If something goes wrong with the `docker-compose` command try the below command instead:
```
docker-compose down && docker-compose up --build --force-recreate
```