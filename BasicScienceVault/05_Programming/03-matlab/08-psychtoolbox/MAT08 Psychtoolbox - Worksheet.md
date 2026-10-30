---
tags: [programming, matlab, psychtoolbox, type/worksheet]
---
# MAT08 Psychtoolbox – Worksheet

> Theory: [[MAT08 Psychtoolbox]] · Solutions: [[MAT08 Psychtoolbox - Solutions]] · Log mistakes in [[Mistakes - MATLAB]]
> Work on paper; no calculator unless marked. Run code only for tasks marked 💻.

## Level 1 – Recall
1. What do `PsychtoolboxVersion`, `PsychDefaultSetup(2)`, `Screen('GetFlipInterval', win)` and `sca` do?
2. What does `Screen('Flip', win)` return, and what happens at the moment of the flip?
3. Why should `MakeTexture` be called before the trial loop?
4. What is the difference between `KbCheck` and `KbQueueCheck`?

## Level 2 – Timing
5. ifi = 1/120 s. How many frames for 50 ms, 200 ms, 1 s? Can you show 30 ms exactly?
6. Fixation shown at `vbl`. You want the stimulus 500 ms later at 60 Hz. Write the `when` argument. Why `- 0.5`?
7. `[vbl, onset, ft, missed] = Screen('Flip', win, when)` returns `missed = 0.008`. What does it mean?
8. Your script measures RT as `GetSecs` at key press minus `GetSecs` called **before** `Screen('Flip')`. What error does this introduce?

## Level 3 – Debugging
9. The experiment works on your laptop with `Screen('Preference', 'SkipSyncTests', 1)` but prints a sync failure on the lab PC with 0. Name three things to check.
10. After an error in the trial loop, the screen stays black. How do you recover now, and how do you prevent it in future?
11. Stimuli are 25 % larger than intended on the lab PC. Likely cause?

## Level 4 – Neuro transfer
12. Describe how you would verify that your EEG triggers mark stimulus onsets correctly before collecting data.
13. Compute the size in pixels of a stimulus that should subtend 5° of visual angle at 60 cm viewing distance on a screen 53 cm wide with 1920 px. (Use $\tan 2.5°\approx0.0437$.)
14. 💻 (PTB installed) Open a window, measure `ifi`, then present a white square for exactly 6 frames 100 times and record `missed` for each flip. How many deadlines were missed?
