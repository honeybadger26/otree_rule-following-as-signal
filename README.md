# Rule Following As Signal

## Instructions

- Download and install [Docker](https://www.docker.com/products/docker-desktop/)
- `cd` to this folder and run:
```
./run.sh
```
- In your browser, go to [localhost:8000](http://localhost:8000)

## Notes

- If there is a 'permission denied' error when attempting to run `./run.sh` try:
```
chmod +x run.sh && ./run.sh
```
- If something else goes wrong try:
```
docker system prune -a && ./run.sh
```

## Tests

To run tests, use the following:
```
./run.sh -t
```
or
```
./run.sh -t <test_name>
```

---

# Todo - Simon

- Develop a *strategy method* version of the app
	- I.e. all deciders have to indicate how they *would* play in DG, before they know whether they have been chosen.

		See new page created in rfas/templates "DictatorTask-strategy.html"
	- Note: important to keep variable names the same, insofar as possible.
	- Also need to keep both versions of the software alive for future development. Maybe use different branches in the repo? To discuss.
	- Develop a full list of variable names for the new version, with notes for anyone trying to compare data on how they differ from other version.

- For both branches:
	- The $10 participation fee, on the informed consent page, and on the first page of instructions, is not coded using the variable. Update to use the config variable.

## Done

---

# Todo - Toby

- Andrew would include a practice block? (for future)