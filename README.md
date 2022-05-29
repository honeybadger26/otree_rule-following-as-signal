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

## Done

---

# Todo - Toby

- Instructions - Shaun suggests a at start of Part 1 instructions, reinforce that participants role will be assigned after reading the instructions. @done

- Double check in the data: is group membership constant across blocks?
- "can then choose which deciderS" @done
- delete redundant "earn" @done
- Use strategy method for selector choice? (save for future)
- Andrew would include a practice block? (for future)
- "my place of worship" instead of "Church" @done
- Reverse scored Hexaco questions are still appearing wrong. (answer order is reversed)
- Shaun wants the HEXACO one first -- in case religous one triggers attitudes
- Andrew query about explanatory statement -- double check

- Consent page/Explanatory statement
	- Consent page needs updated contact information @done
	- Reference to Euros need to be replaced with dollars throughout @done
	- Reference to earning credits needs to be removed. @done
	- Clarify are participants paid for 1 round from EACH part, or 1 round from either part? @done [They are paid for one round from each part. With $0.02 per point, the maximum average earning from the experiment is around $31.70 per participant (including participation fee). The minimum average earning possible is around $16.]
- Payment info page
	- Update based on whether using PayID or other method @done
	- Add breakdown of payment info to final screen. Explain which rounds were selected. @done