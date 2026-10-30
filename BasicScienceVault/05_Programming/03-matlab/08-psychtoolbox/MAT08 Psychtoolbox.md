---
aliases: [Psychtoolbox, PTB, Screen Flip, KbCheck, Frame Timing, SkipSyncTests]
tags: [programming, matlab, psychtoolbox, experiment-control, timing, type/overview, neuro]
---
# MAT08 Psychtoolbox

> [[MAT00 MATLAB Overview|↑ MATLAB]] · [[MOC-programming|Programming MOC]] · [[MAT08 Psychtoolbox - Worksheet|✏️ Worksheet]] · [[MAT08 Psychtoolbox - Solutions|✅ Solutions]] · [[Mistakes - MATLAB|⚠️ Mistake log]]

## Why this matters
**Psychtoolbox-3** (PTB) is the classic MATLAB (and GNU Octave) toolbox for vision and psychophysics experiments, used for decades in EEG, MEG and fMRI labs. It gives low-level control over the display, with precise **timestamps of every screen refresh**. The ideas – double buffering, frames, flips, triggers on the flip – are the same as in PsychoPy ([[Py11 PsychoPy Experiment Control]]).

## Checking the installation and setting up the screen
```matlab
PsychtoolboxVersion                      % installed version (also checks that PTB is on the path)
PsychDefaultSetup(2);                    % unified key names, colour range 0–1, assertions
Screen('Preference', 'SkipSyncTests', 0);% 0 = run the synchronisation tests (required for experiments!)
screens = Screen('Screens');
scr = max(screens);                      % external monitor if present
[win, rect] = PsychImaging('OpenWindow', scr, 0.5);   % grey background; rect = [0 0 width height]
ifi = Screen('GetFlipInterval', win);    % inter-frame interval, e.g. 0.0167 s at 60 Hz
[xc, yc] = RectCenter(rect);
Priority(MaxPriority(win));              % real-time priority for better timing
HideCursor;
% ... experiment ...
Priority(0); ShowCursor; sca;            % sca = Screen('CloseAll')
```
- `Screen` is PTB's central function: the first argument names the sub-command (`'OpenWindow'`, `'Flip'`, `'DrawTexture'`, …). `Screen('OpenWindow?')` prints help for one sub-command.
- Wrap the experiment in `try … catch … sca; rethrow(err); end` – otherwise an error leaves a black full-screen window that blocks your desktop.
- `PsychImaging` offers advanced pipelines (high bit depth, gamma correction, stereo); plain `Screen('OpenWindow', …)` also works.

## Stimuli, textures and timing with Screen('Flip')
```matlab
Screen('TextSize', win, 40);
DrawFormattedText(win, '+', 'center', 'center', 1);    % draw into the back buffer
vbl = Screen('Flip', win);                              % show it at the next refresh; returns the timestamp
img = imread('stimuli/face01.png');
tex = Screen('MakeTexture', win, img);                  % upload once, before the trial loop
dst = CenterRectOnPointd([0 0 400 400], xc, yc);
Screen('DrawTexture', win, tex, [], dst);
[vbl, onset] = Screen('Flip', win, vbl + (30 - 0.5) * ifi);   % show 30 frames after the fixation onset
Screen('Flip', win, onset + (6 - 0.5) * ifi);           % remove after 6 frames (100 ms at 60 Hz)
Screen('Close', tex);                                    % free texture memory
```
- **Double buffering:** you draw into the hidden back buffer; `Screen('Flip')` swaps buffers at the **vertical retrace** and returns `[VBLTimestamp, StimulusOnsetTime, FlipTimestamp, Missed]`.
- **Schedule flips** with the `when` argument: `vbl + (n - 0.5) * ifi` asks for the flip `n` frames after the previous one; the `- 0.5` frame margin makes sure you don't miss the target refresh by a tiny amount.
- **Durations are whole frames** (60 Hz → multiples of 16.7 ms). `Missed > 0` means the deadline was missed – log it.
- **Textures:** make them **before** the trial (`MakeTexture` is slow); draw them during the trial (`DrawTexture` is fast). Procedural Gabors: `CreateProceduralGabor`.
- Colours are 0–1 with `PsychDefaultSetup(2)` (0–255 otherwise).

## Keyboard and mouse
```matlab
KbName('UnifyKeyNames');                          % same key names on all OSs (included in PsychDefaultSetup(2))
keys = [KbName('f') KbName('j') KbName('ESCAPE')];
t0 = onset; rt = NaN; resp = "";
while GetSecs - t0 < 2.0
    [down, secs, code] = KbCheck;                  % poll the keyboard
    if down && any(code(keys))
        rt = secs - t0;                            % RT relative to the stimulus onset timestamp
        resp = string(KbName(find(code, 1)));
        break
    end
end
[x, y, buttons] = GetMouse(win);                   % mouse position and buttons
% better timing, no missed presses: KbQueueCreate; KbQueueStart; ...; [pressed, firstPress] = KbQueueCheck;
```
- **`GetSecs`** is PTB's high-precision clock – all timestamps (flips, keys) are on this clock, so RT = key time − stimulus onset.
- `KbCheck` polling can miss very short presses while you're busy drawing; **`KbQueue*`** functions record presses in the background with timestamps.
- `KbStrokeWait` / `KbReleaseWait` for "press any key to continue" screens.
- Response boxes and button boxes give lower latency than USB keyboards.

## Synchronisation and frame timing (EEG/MEG triggering)
- **Trigger on the flip:** send the EEG/MEG trigger code **immediately after** the `Screen('Flip')` that shows the stimulus returns (or use hardware that is triggered by the video signal) – the flip timestamp tells you when the image appeared.
```matlab
[vbl, onset] = Screen('Flip', win, when);
io64(ioObj, address, code);  WaitSecs(0.005);  io64(ioObj, address, 0);   % parallel port (Windows)
% serial/USB trigger boxes: IOPort('Write', port, uint8(code));
```
- **Measure, don't assume:** a **photodiode** on a corner patch that changes with the stimulus, recorded as an EEG channel, shows the true onset and any constant lag (monitor input lag, LCD response) or jitter.
- **fMRI:** wait for the scanner's trigger (often sent as a key, e.g. `'5'`) with `KbWait`/`KbQueue`, then time everything relative to it.
- Keep everything **frame-locked**: compute all timings in frames, preload stimuli, avoid disk access and `disp` output during trials, close other programs.

## Typical sources of error
| Problem | Symptom | Fix |
|---|---|---|
| sync tests fail | "SYNCHRONIZATION FAILURE" warning; unreliable timestamps | fix the display setup (single monitor, native resolution, no mirroring, proper graphics driver, disable compositor/scaling); never run real experiments with `SkipSyncTests = 1` |
| `SkipSyncTests = 1` left in the code | experiment runs, but timing is unknown | only for debugging on a laptop; set to 0 for data collection |
| wrong resolution / OS display scaling (Retina, Windows 125 %) | stimuli wrong size, sync failure | use the monitor's native resolution, 100 % scaling; check `rect` and `Screen('Resolution', scr)` |
| refresh rate not what you think | durations off (e.g. 100 ms ≠ 6 frames at 75 Hz) | read `ifi`; compute frames from it; check with a photodiode |
| missed flips | `Missed > 0`, durations too long | preload textures, simplify drawing, high priority, fewer background processes |
| stimulus size in pixels, not degrees | not comparable between setups | convert with viewing distance and screen width ([[D4 Unit Circle Trigonometry]]) |
| black screen after an error | can't see MATLAB | `try/catch` with `sca`; or press Ctrl+C then type `sca` blindly |

## Same idea in Python
PsychoPy: `win.flip()`, `win.callOnFlip()`, `psychopy.hardware.keyboard` (which uses PTB's keyboard engine), frame-counted durations ([[Py11 PsychoPy Experiment Control]]).

## In neuroscience #neuro
- **ERP latencies and amplitudes** depend on trigger–stimulus synchrony: constant offsets shift latencies, jitter smears ERPs.
- **Visual psychophysics:** contrast thresholds with QUEST (`QuestCreate`, `QuestUpdate`), gamma-corrected displays, stimuli in degrees of visual angle.
- **MEG/EEG triggers** via parallel port, LabJack, or vendor boxes; photodiode channels as ground truth.
- **fMRI:** scanner-synchronised starts, onset logs for the GLM ([[CS12 Neuroimaging Data Analysis]]).

## Math links #math-link
- Frames ↔ durations ($1/f_\text{refresh}$) → [[A5 Fractions]]
- Visual angle $\theta = 2\arctan\frac{s}{2d}$ → [[D4 Unit Circle Trigonometry]]
- Gabor patches = sinusoid × Gaussian → [[B4 Trigonometric Functions]], [[B2 Exponential Functions]]

## Connections
- PsychoPy equivalent → [[Py11 PsychoPy Experiment Control]]
- Saving results → [[MAT04 MATLAB Data Import and Files]]
- Recording side → [[Meth03 Electrophysiology]], [[MAT09 EEGLAB]]

## Key takeaways
- Check `PsychtoolboxVersion`; `PsychDefaultSetup(2)`; keep sync tests on (`SkipSyncTests = 0`).
- Draw into the back buffer, `Screen('Flip')` at the retrace; schedule flips with `vbl + (n − 0.5) * ifi`; durations are whole frames.
- Preload textures; record keys with `KbCheck`/`KbQueue` on the `GetSecs` clock.
- Send triggers right after the flip, verify with a photodiode; wrap everything in `try/catch` with `sca`.
