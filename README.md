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

- Payment Info program
	- Earnings are reported in Euros. [TH: This seems to be encoded in a variable that I don't know how to fix.] [Simon: I believe the variables is `REAL_WORLD_CURRENCY_CODE` in `settings.py`. Currently, I have it set to AUD]
	- What variable(s) determine the round(s) that are paid? I'd like to be able to explain on the payment info page which round was selected to be paid.
		- These variables are now available using `session.vars.rfas_payed_round1` and `session.vars.rfas_payed_round2`. I've added a paragraph on the payment info page showing how to use them so edit this as you see fit. Adding this means that you now cannot run Payment Info by itself on the server page (since it now relies on the RFAS task being completed)
- Replace SVO program
	- Instead of the SVO program, participants are to be given a couple of questionnaries. See file "new_questions.md". Suggested program titles are in the file.

## Done

- Experiment Instructions
	- Request payID, in the same way you coded it for groupreputation3. This program to come as last page in the Instructions program.
	- Delete Information Brochure page
- Rule Following Instructions
	- 100 points = 1 Euro --> "1 Dollar"
	- Roles subsection
		- put "selector" and "decider" in boldface when they first appear
	- Baseline of 650 points for earnings needs to be changed
		- Earning as follows:
			- everyone gets $10 show up fee
			- Then points from the experiment are added to $10.
			- Each point is worth $0.03 (but this should be a variable I can adjust at )
	- Increase size of graphic in "Roles" box by about 50% (I can generate a higher res image if required) 
	- Centre images
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
	- "Click the blue headings to collapse the subsections."
- Decider, Stage 3
	- Decider should have the option to give up to 500 points to selector, and keep none for self -- as well as intermediate options (current list of options is constrained so can not give more than half away.)
- Decider, Stage 1
	- add pictures of buckets over the buttons
- Reference to amounts that can be earned -- are these based on variables or hard coded? [Simon: These are hard coded, see rfas/models.py - ENDOWMENT_SELECTION, ENDOWMENT_STAGE_THREE, etc. I can make all the below variable (editable through session config), but KEEP_ and GIVE_ AMOUNTS are a bit trickier]
	- Make ENDOWMENT_SELECTION variable
    - Make ENDOWMENT_STAGE_THREE variable
    - Make SELECTION_FEE variable
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
	- Gender question -- code it the same way as in groupreputation3 project
- Debriefing
	- Toby has uploaded some edits to Debriefing.html
	- Debriefing2.html is redundant and can be deleted?
- Thank you
	- change reference from Euros to dollars
- Various applications have names like "thesis", "thesis-instructions", etc. This is redundant and distracting. Can we do a global change to wherever "thesis" occurs in a program name, change it to "rfas" (rule following as signal)? [TH: Why do we still have folders for "thesis_debriefing" etc?] [Simon: Not sure what's going on here. These folders must be generated somehow as they aren't checked into the git repo...] [Toby: Ah, ok, I'll ignore/delete.]
- Where are we at with Part 2? I can't see code for it...? [Simon: As discussed this is done, but hard to clearly see. Under `rfas/models.py` there are PTx_NUM_ROUNDS variables which you can use to change the number of rounds of each part]

---

# Todo - Toby

- Consent page/Explanatory statement
	- Consent page needs updated contact information @done
	- Reference to Euros need to be replaced with dollars throughout @done
	- Reference to earning credits needs to be removed. @done
	- Clarify are participants paid for 1 round from EACH part, or 1 round from either part?
- Payment info page
	- Update based on whether using PayID or other method
	- Add breakdown of payment info to final screen. Explain which rounds were selected.