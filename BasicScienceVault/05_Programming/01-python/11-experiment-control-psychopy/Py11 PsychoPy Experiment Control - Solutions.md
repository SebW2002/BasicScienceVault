---
tags: [programming, python, psychopy, type/solution]
---
# Py11 PsychoPy Experiment Control – Solutions

> Worksheet: [[Py11 PsychoPy Experiment Control - Worksheet]] · Theory: [[Py11 PsychoPy Experiment Control]] · Wrong? → [[Mistakes - Python]]

## Level 1
1. `draw()` renders the stimulus into the hidden **back buffer** (nothing visible yet). `flip()` swaps buffers at the next vertical refresh, so everything drawn becomes visible at once.
2. Builder: fast, fewer timing mistakes, generates readable code, online export (Pavlovia). Coder: adaptive procedures/closed-loop, complex trial logic, custom hardware (eye tracker, EEG amplifier API), unusual stimulus generation.
3. A table of trial types: each **row** is one condition (trial type), each **column** a parameter (image file, correct key, contrast …) that the experiment reads per trial.
4. To reconstruct the exact trial order later (debugging, checking, re-analysis) and to make the experiment reproducible.

## Level 2
5. 16.7 ms, 13.3 ms, 8.3 ms, 6.9 ms.
6. 3, 6, 15 frames. 40 ms = 2.4 frames ✗; 75 ms = 4.5 frames ✗ – neither exactly (at 75 Hz, 40 ms = 3 frames ✓).
7. Visibility changes only at refreshes, so the duration is rounded to whole frames: the loop ends somewhere between frames 1 and 2 (16.7 or 33.3 ms), varying from trial to trial. Use frame counting (2 frames = 33.3 ms) instead.
8. In 12 trials at least one frame took two refresh cycles: the stimulus lasted longer (or appeared later) than intended. Identify those trials from the frame log, report them, possibly exclude them; find the cause (background processes, loading during trials).

## Level 3
9. The reset is executed exactly when the flip happens (stimulus onset). Resetting before `flip()` starts the clock up to one frame (16.7 ms) too early, adding a variable error to every RT.
10. Loading the image from disk inside the trial takes variable time, delaying the flip unpredictably (dropped frames). Create all `ImageStim` objects (or load the images) **before** the trial loop and only change/draw them during it.
11. ```python
    for _ in range(6):
        img.draw()
        win.flip()
    win.flip()      # nothing drawn → blank screen
    ```
12. 4 × 25 = **100** trials. `method="random"` shuffles **within each repetition** of the 4 conditions, so every block of 4 consecutive trials contains each condition once – hence yes, each quarter (25 trials = 6.25 repetitions) is nearly balanced (±1). With `"fullRandom"` there would be no such guarantee.

## Level 4
13. (1) A constant delay between trigger and actual stimulus onset (monitor input lag, trigger sent before the flip) shifts all latencies → measure with a photodiode and compare with the trigger. (2) Variable delay (jitter: dropped frames, triggers not locked to the flip, USB latency) smears the average → broader, smaller peak; check the photodiode-trigger difference across trials. (Also check filter phase shifts: causal filters delay peaks, [[Py08 SciPy Scientific Computing]].)
14. Start the experiment on the scanner's first trigger pulse (wait for the key the scanner sends), reset the experiment clock at that moment, and log each onset relative to it. `events.tsv`: `onset` (s from the first volume), `duration` (s), `trial_type` (condition), optionally `response_time` and other columns.
15. ```python
    from psychopy import visual, core, data
    from psychopy.hardware import keyboard
    import numpy as np
    win = visual.Window(fullscr=False, size=(800, 600), color="grey", units="height")
    print(win.getActualFrameRate())
    fix = visual.TextStim(win, text="+", height=0.05)
    gab = visual.GratingStim(win, tex="sin", mask="gauss", sf=10, size=0.3)
    kb = keyboard.Keyboard()
    rng = np.random.default_rng(42)
    exp = data.ExperimentHandler(dataFileName="test_gabor")
    for i in range(10):
        gab.ori = rng.choice([45, 135])
        for _ in range(6): fix.draw(); win.flip()
        win.callOnFlip(kb.clock.reset); win.callOnFlip(kb.clearEvents)
        for _ in range(6): gab.draw(); win.flip()
        win.flip()
        keys = kb.waitKeys(maxWait=2, keyList=["f", "j"], clear=False)  # keep presses made during the stimulus
        exp.addData("ori", gab.ori)
        exp.addData("key", keys[0].name if keys else None)
        exp.addData("rt", keys[0].rt if keys else None)
        exp.nextEntry()
    exp.saveAsWideText("test_gabor.csv"); win.close(); core.quit()
    ```
