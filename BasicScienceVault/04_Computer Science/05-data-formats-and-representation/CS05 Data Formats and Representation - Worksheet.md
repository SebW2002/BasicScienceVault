---
tags: [computer-science, data-format, type/worksheet]
---
# CS05 Data Formats and Representation – Worksheet

> Theory: [[CS05 Data Formats and Representation]] · Solutions: [[CS05 Data Formats and Representation - Solutions]] · Log mistakes in [[Mistakes - Computer Science]]
> No calculator unless marked 🧮. 1 MB = 10⁶ bytes, 1 GB = 10⁹ bytes.

## Level 1 – Concepts
1. State the three rules of tidy data.
2. Convert the wide table `neuron | rate_light | rate_dark` with rows `1 | 12 | 8` and `2 | 5 | 6` into long (tidy) format.
3. Which format would you choose: a) 3 hours of Neuropixels data with spike-sorting results and behaviour, b) an fMRI study with 30 subjects to share on OpenNeuro, c) a confocal z-stack with known pixel size, d) a figure for a poster?
4. Why is JPEG unsuitable for microscopy data?

## Level 2 – Bits and bytes
5. How many grey levels does a 12-bit camera have? A 16-bit one?
6. How much memory do $10^8$ values need in float32 and in float64?
7. Raw ephys is stored as int16 with a gain of 0.195 µV per bit. Which voltage corresponds to a stored value of 1000? What is the maximum representable voltage?
8. Why might `0.1 + 0.2 == 0.3` return False in most programming languages? How should you compare floats?

## Level 3 – Data volumes
9. A 64-channel EEG at 1000 Hz with float32 samples records for 1 hour. File size?
10. A two-photon microscope records 512 × 512 pixels at 30 Hz with uint16. Data rate per second and per hour?
11. A light-sheet microscope produces 2048 × 2048 pixel images (uint16) at 100 images/s. How long until a 10 TB disk is full?

## Level 4 – Standards & metadata
12. Parse the BIDS filename `sub-07_ses-02_task-nback_run-1_bold.nii.gz`. What information does it contain? Where would the repetition time (TR) be stored?
13. A DICOM file from the clinic is to be shared with collaborators. What must you check first?
14. A colleague sends you a CSV with a column `signal` and no other information. List five metadata items you would need before you can analyse it.
15. 🧮 A Zarr array of shape (time = 100,000, x = 512, y = 512), uint16, is chunked as (100, 512, 512). How many chunks are there, and how large is each chunk? What would happen if you wanted the time series of a single pixel?
