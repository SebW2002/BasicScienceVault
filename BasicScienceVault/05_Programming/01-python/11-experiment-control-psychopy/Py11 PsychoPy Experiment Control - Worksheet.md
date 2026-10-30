---
tags: [programming, python, psychopy, type/worksheet]
---
# Py11 PsychoPy Experiment Control – Worksheet

> Theory: [[Py11 PsychoPy Experiment Control]] · Solutions: [[Py11 PsychoPy Experiment Control - Solutions]] · Log mistakes in [[Mistakes - Python]]
> Work on paper. Run code only for tasks marked 💻.

## Level 1 – Recall
1. What happens on `stim.draw()`, and what on `win.flip()`?
2. Name two advantages of Builder and two situations that call for Coder.
3. What is a conditions file? What does each row and each column represent?
4. Why should you save the seed of the trial randomisation?

## Level 2 – Timing arithmetic
5. Frame duration at 60, 75, 120 and 144 Hz?
6. At 60 Hz, how many frames are 50 ms, 100 ms, 250 ms? Which of 40 ms and 75 ms can be shown exactly?
7. You request 30 ms at 60 Hz with a clock-based loop (`while clock.getTime() < 0.030`). How long will the stimulus actually be visible? Why?
8. `win.nDroppedFrames` is 12 after a run of 600 trials with a 6-frame stimulus. What does this mean for your data?

## Level 3 – Read and write code
9. Why is `win.callOnFlip(kb.clock.reset)` better than calling `kb.clock.reset()` right before `win.flip()`?
10. Find the timing problem:
    ```python
    for trial in trials:
        img = visual.ImageStim(win, image=trial["image"])   # load inside the trial
        img.draw(); win.flip()
    ```
11. Write the loop that shows `img` for exactly 6 frames and then a blank screen.
12. A conditions file has 4 rows; `TrialHandler(nReps=25, method="random")`. How many trials in total? Is it guaranteed that each condition occurs equally often in every quarter of the experiment?

## Level 4 – Neuro transfer
13. Your ERP's N170 peaks at 190 ms instead of the expected 170 ms; the peak is also broader than in the literature. Name two timing-related causes and how you'd test them.
14. In an fMRI experiment, how do you make sure that stimulus onsets in your log match the scanner's time? What goes into `events.tsv`?
15. 💻 (PsychoPy installed) Open a window, measure `win.getActualFrameRate()`, show a fixation cross and a Gabor for 6 frames each in a loop of 10 trials with a random orientation (seeded), record key presses (`f`/`j`) with RTs and save a CSV.
