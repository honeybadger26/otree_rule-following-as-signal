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

- Something has gone wrong with the transition between Part 1 and Part 2. There is no screen advising Deciders that in Part 1 the payoffs for bucket selection will be different. I have created a new file EnvironmentPageX that should have all the necessary info, but please check if it works as expected without bugs. Please make sure ALL players (deciders and selectors) see this page just before they begin Part 2.
- If somebody doesn't answer one of the HEXACO questions, and tries to submit, ALL their answers get reset.
- Same problem in Religion questionnaire. Leaving any question unanswered brings back all the questions unanswered.
- Display participant ID on the final screen, similar to other recent experiments. [Simon: Added final paragraph to `payment_info\templates\payment_info\PaymentInfo.html`]

## Done

- Religion Questionnaire -- 9 point sliders. Force responses -- at the moment, if you click next, it advances you to the next page, and records your responses as 5 for each item. (Check SVO program for how they force responses on slider items?)
	- 9 point sliders. Is it possible to display the number that the participant is selecting as they move the slider? Or just to have some check marks above so they have some sense of where the possible options are?
- HEXACO questionnaire -- same problem as religion questionnaire. Isn't really forcing a response.
- Payment Info program
	- I've reworded the first paragraph to indicate what I want it to report. It needs to tell people their earnings from the experiment PLUS the $10.00 participation fee.
- Instructions page. Payment info box does not update when I change  the value of the currency per point variables: 
  
  > The points you earn in a round will be converted to money at a conversion rate of <strong>100 points = 3 Dollars</strong>..
  
  Can you program this using relevant variables so it updates each session?
- Instructions page. Collapsible headings now work, but they only appear blue while I hover mouse over. Can you make them blue at all times? If not, please remove the word "blue" from the instructions.
- Give participants button to hide their payout when they have finished, similar to other recent experiments.
- Change default value participation fee to 500 points.
- Number of rounds per part -- currently just 1. Please set to 3 for further testing.
- Remove the PayID page from the experiment (sorry -- had second thoughts about how to do this part.)
- Change default currency per point to 0.02.
- Replace SVO program
	- Instead of the SVO program, participants are to be given a couple of questionnaries. See file "new_questions.md". Suggested program titles are in the file.
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
- Earnings are reported in Euros. [TH: This seems to be encoded in a variable that I don't know how to fix.] [Simon: I believe the variables is `REAL_WORLD_CURRENCY_CODE` in `settings.py`. Currently, I have it set to AUD]
- What variable(s) determine the round(s) that are paid? I'd like to be able to explain on the payment info page which round was selected to be paid.
	- These variables are now available using `session.vars.rfas_payed_round1` and `session.vars.rfas_payed_round2`. I've added a paragraph on the payment info page showing how to use them so edit this as you see fit. Adding this means that you now cannot run Payment Info by itself on the server page (since it now relies on the RFAS task being completed)


---

# Todo - Toby

- Consent page/Explanatory statement
	- Consent page needs updated contact information @done
	- Reference to Euros need to be replaced with dollars throughout @done
	- Reference to earning credits needs to be removed. @done
	- Clarify are participants paid for 1 round from EACH part, or 1 round from either part? @done [They are paid for one round from each part. With $0.02 per point, the maximum average earning from the experiment is around $31.70 per participant (including participation fee). Thi minimum average earning possible is around $16.]
- Payment info page
	- Update based on whether using PayID or other method @done
	- Add breakdown of payment info to final screen. Explain which rounds were selected. @done