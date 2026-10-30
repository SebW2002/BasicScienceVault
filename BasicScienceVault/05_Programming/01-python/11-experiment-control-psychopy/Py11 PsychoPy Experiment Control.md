---
aliases: [PsychoPy, Experiment Control, Stimulus Presentation, Builder vs Coder, Frame Timing, TrialHandler]
tags: [programming, python, psychopy, experiment-control, timing, type/overview, neuro]
---
# Py11 PsychoPy Experiment Control

> [[Py00 Python Overview|↑ Python]] · [[MOC-programming|Programming MOC]] · [[Py11 PsychoPy Experiment Control - Worksheet|✏️ Worksheet]] · [[Py11 PsychoPy Experiment Control - Solutions|✅ Solutions]] · [[Mistakes - Python|⚠️ Mistake log]]

## Why this matters
Behavioural, EEG, MEG and fMRI experiments need stimuli shown at **known times**, responses recorded with **millisecond precision**, conditions **randomised** and everything **logged**. PsychoPy does this in Python (the MATLAB counterpart is Psychtoolbox, [[MAT08 Psychtoolbox]]). Timing errors here can't be fixed in the analysis.

## Builder vs. Coder
| | **Builder** (GUI) | **Coder** (Python script) |
|---|---|---|
| how | drag "routines" and "components" onto a timeline, loops over a conditions file | write Python with the `psychopy` library |
| strengths | fast for standard designs, fewer timing mistakes, exports to the web (PsychoJS/Pavlovia) | full flexibility: adaptive staircases, closed-loop, complex logic, hardware |
| weaknesses | complex logic gets messy (code components everywhere) | you're responsible for timing and data saving |
| good for | RT tasks, questionnaires, standard EEG paradigms, online studies | real-time feedback, eye-tracker/EEG integration, unusual designs |
Builder **generates a Python script** – reading it is a great way to learn the Coder API. A common path: build in Builder, add small **code components**, switch to Coder only when necessary.

## The window, stimuli and the flip
```python
from psychopy import visual, core
win = visual.Window(size=(1920, 1080), fullscr=True, color="grey", units="height")
fix = visual.TextStim(win, text="+", height=0.05)
img = visual.ImageStim(win, image="stimuli/face01.png", size=(0.4, 0.4))
grating = visual.GratingStim(win, tex="sin", mask="gauss", sf=10, size=0.3, ori=45)  # Gabor
fix.draw()          # draw into the hidden back buffer
win.flip()          # swap buffers at the next screen refresh → stimulus becomes visible
```
- **Double buffering:** you draw into an invisible buffer; `win.flip()` shows it at the next **vertical refresh** and returns (approximately) the time it happened. Everything visible is tied to refresh cycles.
- **Units:** `"height"` (fraction of screen height, simplest), `"pix"`, `"deg"` (visual angle; needs monitor distance and width in the Monitor Center – required in vision science).
- `sf` = spatial frequency in cycles per unit; `ori` in degrees; `contrast`, `opacity`, `pos`.

## Timing and frame rate
- A 60 Hz display refreshes every $1000/60\approx16.7$ ms; 120 Hz → 8.3 ms; 144 Hz → 6.9 ms. **A stimulus duration is a whole number of frames.** 100 ms at 60 Hz = 6 frames; 50 ms = 3 frames; 75 ms is impossible (4.5 frames).
- **Count frames** for brief stimuli instead of using clocks:
```python
n_frames = round(0.100 * 60)       # 6
for _ in range(n_frames):
    img.draw()
    win.flip()
win.flip()                          # blank screen
```
- Check the real rate: `win.getActualFrameRate()`; log dropped frames with `win.recordFrameIntervals = True` (`win.nDroppedFrames`).
- Avoid heavy work (loading images, saving files) between flips; preload stimuli before the trial.
- **Verify physically:** a photodiode on the screen corner recorded with your EEG is the only proof of when stimuli really appeared (monitor input lag, LCD response time).

## Responses: keyboard and mouse
```python
from psychopy.hardware import keyboard
from psychopy import event
kb = keyboard.Keyboard()
img.draw()
win.callOnFlip(kb.clock.reset)       # RT clock starts exactly at stimulus onset
win.callOnFlip(kb.clearEvents)
win.flip()
keys = kb.waitKeys(maxWait=2.0, keyList=["f", "j", "escape"])
if keys is None:
    resp, rt = None, None             # miss
else:
    resp, rt = keys[0].name, keys[0].rt
mouse = event.Mouse(win=win)
pos = mouse.getPos(); buttons = mouse.getPressed()
```
- `psychopy.hardware.keyboard` (based on Psychtoolbox's engine) gives better timing than `event.getKeys`.
- Standard keyboards add latency and jitter (several ms); response boxes are better for precise RTs.
- Always provide an **escape key** that saves data and closes the window.

## Randomisation and conditions tables
A **conditions file** (CSV/XLSX) has one row per trial type and one column per parameter:
```text
condition,image,correct_key
face,stimuli/face01.png,f
house,stimuli/house01.png,j
```
```python
from psychopy import data
conds = data.importConditions("conditions.csv")
trials = data.TrialHandler(trialList=conds, nReps=20, method="random", seed=1234)
exp = data.ExperimentHandler(name="faces", dataFileName="data/sub-01_faces")
exp.addLoop(trials)
for trial in trials:
    img.image = trial["image"]
    # … present, collect resp/rt …
    exp.addData("resp", resp); exp.addData("rt", rt)
    exp.addData("correct", resp == trial["correct_key"])
    exp.nextEntry()
exp.saveAsWideText("data/sub-01_faces.csv")
```
- `method="random"` shuffles within each repetition block; `"fullRandom"` shuffles across all; `"sequential"` keeps the order.
- **Counterbalancing** (response mapping, block order) is done across participants – e.g. by participant number.
- **Constraints** (no more than 3 same conditions in a row) need your own shuffling code with checks.
- Set and save the **seed** so the trial order can be reconstructed.

## Logging
```python
from psychopy import logging
logging.LogFile("data/sub-01_faces.log", level=logging.EXP, filemode="w")
logging.exp("block 1 start")
```
Save **every trial immediately** (ExperimentHandler does this on crash/escape too), plus participant info (via `gui.DlgFromDict`), PsychoPy version, frame rate and the conditions file.

## Triggers for EEG/MEG/fMRI
- Send a trigger code **at the flip** that shows the stimulus: `win.callOnFlip(port.setData, code)`, reset to 0 a few ms later (parallel port, serial/USB trigger box, LabJack). For fMRI, **wait for the scanner's trigger pulse** (often a key press like `"5"`) before starting.
- Different codes for different events; write them into the log; check them in the EEG file before the first real participant.

## Same idea in MATLAB
Psychtoolbox: `Screen('OpenWindow')`, `Screen('Flip')` returns the flip timestamp, `KbCheck`, `GetSecs` → [[MAT08 Psychtoolbox]]. The concepts (buffers, refresh, frames, triggers on flip) are identical.

## In neuroscience #neuro
- **ERP latencies** are only as good as trigger timing: a constant delay shifts all latencies; a **jittering** delay smears and reduces the ERP.
- **fMRI:** trials aligned to TR or jittered ITIs for efficient designs; log onsets relative to the first scanner pulse for the GLM's `events.tsv` ([[CS12 Neuroimaging Data Analysis]]).
- **Masked priming / subliminal stimuli** need frame-exact durations of 1–3 frames – check dropped frames.
- **Psychophysics:** staircases (`data.StairHandler`, `QuestHandler`) adapt stimulus intensity to find thresholds; stimuli in degrees of visual angle.

## Math links #math-link
- Frame duration $1/f_\text{refresh}$, durations as integer multiples → [[A5 Fractions]]
- Visual angle $\theta = 2\arctan\frac{s}{2d}$ → [[D4 Unit Circle Trigonometry]]
- Randomisation, permutations, counting orders → [[A7 Sums Products and Factorials]]
- Gabor = sinusoid × Gaussian → [[B4 Trigonometric Functions]], [[B2 Exponential Functions]]

## Connections
- Files and logging → [[Py04 Python Files and Data Formats]], [[Py13 Python Reproducible Projects and Testing]]
- Classes for experiment objects → [[Py12 Python Object-Oriented Programming]]
- Events into analysis → [[Py10 Python Neuroscience Packages]] (MNE), [[Meth03 Electrophysiology]]
- Same in MATLAB → [[MAT08 Psychtoolbox]]

## Key takeaways
- Builder for standard designs (it writes the script), Coder for complex logic.
- `draw()` into the back buffer, `win.flip()` shows it at the next refresh; durations are whole frames.
- Start RT clocks and send triggers **on the flip** (`callOnFlip`); verify with a photodiode.
- Conditions file + TrialHandler with a saved seed; save data every trial; log everything.
