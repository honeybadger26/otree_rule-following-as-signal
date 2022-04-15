# Rule Following As Signal

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

---

# Todo - Simon

- Reference to amounts that can be earned -- are these based on variables or hard coded? [Simon: These are hard coded, see rfas/models.py - ENDOWMENT_SELECTION, ENDOWMENT_STAGE_THREE, etc. I can make all the below variable (editable through session config), but KEEP_ and GIVE_ AMOUNTS are a bit trickier]
	- Make ENDOWMENT_SELECTION variable
    - Make ENDOWMENT_STAGE_THREE variable
    - Make SELECTION_FEE variable
- Instructions page
	- Baseline of 650 points for earnings may need to be changed, TBD
	- Roles subsection
		- include a picture in this subseection, after first para -- "players.png" (temporarily stored in root level of this repository)
	- Part 1
		- Stage 1
			- Add image "decider-choice.png" immediately after first paragraph
		- Stage 2
			- Add image "selector-choose-partners.png" after the second paragraph
		- Stage 3
			- Add image "decider-allocates.png" after the second para
		- Checkbox for all of Part 1 should appear after the Feedback sub-box
- Decider, Stage 1
	- add pictures of buckets over the buttons
- Decider, Stage 3
	- Decider should have the option to give up to 500 points to selector, and keep none for self -- as well as intermediate options (current list of options is constrained so can not give more than half away.)
- Demographic survey
	- Gender question -- code it the same way as in groupreputation3 project	
- Various applications have names like "thesis", "thesis-instructions", etc. This is redundant and distracting. Can we do a global change to wherever "thesis" occurs in a program name, change it to "rfas" (rule following as signal)? [TH: You appear to have done this for main app, but not for thesis_debriefing; thesis_demographics; etc. Please change these also]

## Done

- Instructions page
	- 100 points = 1 Euro --> "1 Dollar"
	- Roles subsection
		- put "selector" and "decider" in boldface when they first appear
- Part 2 intro page
	- Add new para at end: "The rule is to place the balls in the blue bucket."
- Demographic survey
	- Add field of study options
		- Engineering
		- Medicine/Health sciences
		- Natural sciences
		- Business/Marketing
		- Social Sciences
		- Not a student
	- Remove "why did you participate in this study" question
	- Replace "How many experiments question" with "How many experiments in MonLEE question", same as groupreputation3 project
	- Remove "Did you receive all information about this experiment during the experiment?" question
	- Remove "Do you believe you interacted with real humans?" question
- Debriefing
	- Toby has uploaded some edits to Debriefing.html
	- Debriefing2.html is redundant and can be deleted?
- Thank you
	- change reference from Euros to dollars

---

# Todo - Toby

- Consent page/Explanatory statement
	- Consent page needs updated contact information
	- Reference to Euros need to be replaced with dollars throughout
	- Reference to earning credits needs to be removed.
- Payments: why is the baseline payment 6.50, when the MAXIMUM the selector can earn appears to be 5? That seems to ruin any incentive to pick a good partner... Or do they add earnings across parts  1 and 2?
- Instructions page
	- Part 1
		- Stage 2
			- Is it clear that groups remain the same for all 15 rounds? Should it be made more explicit?
- Payment info page
	- Update based on whether using PayID or other