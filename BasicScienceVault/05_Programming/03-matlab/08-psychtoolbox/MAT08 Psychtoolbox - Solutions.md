---
tags: [programming, matlab, psychtoolbox, type/solution]
---
# MAT08 Psychtoolbox – Solutions

> Worksheet: [[MAT08 Psychtoolbox - Worksheet]] · Theory: [[MAT08 Psychtoolbox]] · Wrong? → [[Mistakes - MATLAB]]

## Level 1
1. `PsychtoolboxVersion` prints the installed version (fails if PTB isn't on the path); `PsychDefaultSetup(2)` sets defaults (unified key names, 0–1 colour range, checks); `GetFlipInterval` returns the measured duration of one refresh (ifi); `sca` closes all PTB windows (Screen('CloseAll')).
2. It swaps the back and front buffers at the next vertical retrace, so the drawn content becomes visible; it returns `[VBLTimestamp, StimulusOnsetTime, FlipTimestamp, Missed, Beampos]` on the `GetSecs` clock.
3. Creating a texture copies the image to the graphics card and takes variable, often long time; doing it during a trial delays the flip (missed frames). Drawing an existing texture is fast.
4. `KbCheck` polls the keyboard state at the moment it is called (presses between calls can be missed, timing depends on the loop). `KbQueue*` records key events in the background with accurate timestamps; `KbQueueCheck` reads them out later.

## Level 2
5. 50 ms = 6 frames; 200 ms = 24 frames; 1 s = 120 frames. 30 ms = 3.6 frames → **not** exactly (25 ms = 3 or 33.3 ms = 4 frames).
6. 500 ms at 60 Hz = 30 frames: `when = vbl + (30 - 0.5) * ifi`. The half-frame margin requests "any time after 29.5 frames", so the flip happens at the 30th refresh; asking for exactly 30 × ifi could, due to tiny timing jitter, land just after it and be shown one frame late.
7. A positive value means the flip **missed its deadline** (here by ~8 ms, about half a frame at 60 Hz): the stimulus appeared one frame later than requested. Log and report it; find the cause.
8. The time before `Flip` can be up to one frame (or more, if scheduled) earlier than the actual onset, so RTs are overestimated by a variable amount (0–16.7 ms at 60 Hz). Use the `StimulusOnsetTime`/`vbl` returned by `Flip`.

## Level 3
9. Any three: only one monitor (or proper multi-monitor setup without mirroring); native resolution and refresh rate; OS display scaling at 100 %; up-to-date proper graphics driver (not a generic one); no desktop compositor/full-screen optimisations interfering; correct PTB setup for the OS (e.g. on Linux, a suitable X/Wayland configuration); run `PerceptualVBLSyncTest`/`VBLSyncTest` for diagnosis.
10. Recover: press Ctrl+C (if needed), then type `sca` and Enter blindly (or Alt+Tab to MATLAB). Prevent: `try … catch err, sca; ShowCursor; Priority(0); rethrow(err); end` around the experiment.
11. OS display scaling (e.g. Windows 125 %) or a non-native resolution; or a different monitor size/pixel density than assumed – define stimuli in degrees and compute pixels from the real geometry.

## Level 4
12. Put a photodiode on a screen corner where a white patch appears with each stimulus; record it as an EEG channel together with the triggers. Run the full experiment once, compute the delay between each trigger and the photodiode onset: the mean = constant lag (correct for it), the SD = jitter (should be < 1 ms). Also check that each trigger code matches the intended condition and that the number of triggers equals the number of trials.
13. Size on screen $s = 2d\tan(2.5°) = 2\cdot60\cdot0.0437\approx5.24$ cm. Pixels per cm = 1920/53 ≈ 36.2 → $5.24\cdot36.2\approx190$ px.
14. ```matlab
    PsychDefaultSetup(2); Screen('Preference', 'SkipSyncTests', 0);
    try
        [win, rect] = PsychImaging('OpenWindow', max(Screen('Screens')), 0);
        ifi = Screen('GetFlipInterval', win); sq = CenterRect([0 0 200 200], rect);
        missed = zeros(100, 2); vbl = Screen('Flip', win);
        for k = 1:100
            Screen('FillRect', win, 1, sq);
            [vbl, ~, ~, missed(k, 1)] = Screen('Flip', win, vbl + 0.5 * ifi);
            [vbl, ~, ~, missed(k, 2)] = Screen('Flip', win, vbl + (6 - 0.5) * ifi);
        end
        sca; fprintf('ifi = %.4f s, missed deadlines: %d\n', ifi, sum(missed(:) > 0));
    catch err
        sca; rethrow(err);
    end
    ```
