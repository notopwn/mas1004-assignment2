# Log

One entry for each recipe, selection or Track B model you train, newest at
the bottom. The numbers come from `experiments.csv`. "Why" and "what it means"
are in your own words: your agent asks you for them and does not make them up.
End the log with your plan for what to try next.

<!-- The form of an entry:

## <date> <tag> (Track A or B)
- changed: what is different from the run before
- why: your reason
- validation: 0.000 (before: 0.000)
- what it means: what you think the result says
-->

## 2026-11-06 Starter photo review

> some samples contain letters, and outdoor image samples should be easier to determine relying on the weather, skyline, the way of buildings look etc

## 2026-11-09 baseline (Track A, seed 0)

- Used the starter recipe and all 44,257 training photos with seed 0.
- Validation balanced accuracy was 0.4977. Per-city accuracy was Seoul 0.5782, Busan 0.3791, Tokyo 0.6400, Osaka 0.3454, and Taipei 0.5457.
- Training processed 249,984 photos in 3,906 batches of 64 and took 2,306.7 seconds on the Colab T4 GPU.
- The run used commit a269dc1 and recipe hash 17ac485223fa. Full results are in results/baseline_seed0/result.json and experiments.csv.
- Ran curate.py mistakes on all 12,077 validation photos and generated one sheet of 48 confident errors per city in results/curate/.

### Student observations from the baseline mistake sheets

> if there is hangul in the image, it is quite easy to mistake it as busan for this model.

> and it also confuses cities between the same country

- The student cited photos 14 and 26 on mistakes_baseline_seed0_seoul_00 as examples.
- The sheet's CSV records photo 14 (commons_18159670.jpg) as predicted Busan with confidence 0.90, and photo 26 (commons_17824716.jpg) as predicted Busan with confidence 0.86. Both are validation photos labelled Seoul.

## 2026-11-10 no_text_sample (Track A, training completed)

- Student's requested rule: "lets exclude photos which contains letters for this time"
- Student authorized agent review and training: "do the same for other cities' images, then proceed training without them"
- Agent visually reviewed the five existing training sample sheets (32 photos per city, 160 total), checking larger originals where needed.
- Excluded clear writing in any language, including signs, subtitles, watermarks and text on objects. Kept uncertain cases and numbers-only images.
- Excluded 124 sampled training photos: Seoul 21, Busan 26, Tokyo 26, Osaka 25, Taipei 26. This is not a text-free dataset: the other training photos were not reviewed.
- Full numbered review: scripts/text_photo_review.csv. Reapply with scripts/exclude_sample_text.py. No source photos deleted; validation unchanged; starter recipe unchanged.
- Student's earlier observation: "if there is hangul in the image, it is quite easy to mistake it as busan for this model."
- Local CPU quick check passed (20 training steps and 200 validation photos). This is a setup check, not a full experiment result.
- Colab loaded commit 989201e and started seed 0 on the T4 GPU with 44,133 selection rows and the official 249,984-photo budget (3,906 batches of 64).
- Full validation balanced accuracy: 0.4938. Training took 2,130.4 seconds (35.5 minutes). Result imported from Colab and checked against the current recipe and selection hashes.
- Student interpretation: "it was only a slightest change of training dataset, so it didnt really affected much, i think"
- Next: review the new mistake sheets when they finish and let the student choose the next experiment.

## 2026-11-10 Imported baseline seed 1 and compared the selection experiment

| Run | Validation balanced accuracy | Training seconds |
| --- | ---: | ---: |
| baseline, seed 0 | 0.4977 | 2306.7 |
| baseline, seed 1 | 0.4931 | 2669.3 |
| no_text_sample, seed 0 | 0.4938 | 2130.4 |

- The selection experiment is 0.39 percentage points below baseline seed 0. The two baseline seeds differ by 0.46 percentage points. These two baseline runs do not establish a statistical confidence interval.
- This experiment excluded 124 photos from the 160-photo sample review, leaving 44,133 training photos. It did not remove all text-bearing photos from the full dataset.
- The recipe hash is identical across all three runs (17ac485223fa); the experiment's selection hash is 4387ca522155 and its training commit is 989201e.

| True city | Baseline seed 0 | no_text_sample seed 0 |
| --- | ---: | ---: |
| Seoul | 0.5782 | 0.5885 |
| Busan | 0.3791 | 0.3691 |
| Tokyo | 0.6400 | 0.6114 |
| Osaka | 0.3454 | 0.3647 |
| Taipei | 0.5457 | 0.5354 |

- Confusion counts relevant to the student's observation: Seoul predicted Busan, 159 to 158; Busan predicted Seoul, 442 to 478; Tokyo predicted Osaka, 431 to 546; Osaka predicted Tokyo, 831 to 838.
- Source: the three result.json files under results/ and the imported rows in experiments.csv. All five new mistake sheets (48 validation errors per city) finished on Colab, were imported locally, and passed PNG/CSV checks.

## 2026-11-10 balanced (Track A, completed)

- Student request: "lets try giving every city equal training attention. proceed right away"
- Changed sample_weights to give each training photo weight 1 / number of selected photos in its city. This gives each city an expected 20% share of training draws.
- Kept the 44,133-photo selection from no_text_sample, including its 124 exclusions. All other recipe settings are unchanged.
- Direct comparison: no_text_sample seed 0, validation balanced accuracy 0.4938.
- Student's reason: "this is just a basic idea. to give equal attention, more reasonable&rational."
- Validation balanced accuracy: 0.4989 (no_text_sample seed 0: 0.4938), a 0.51 percentage point increase. Training took 2,122.8 seconds (35.4 minutes).
- Student interpretation: "still not an meaningful improvement, should find better way"
- Local CPU quick check passed: 20 steps and validation on 200 photos. This is a setup check, not an official experiment result.
- Colab pulled training commit 481c791 and confirmed seed 0 on CUDA with 44,133 selected photos and 3,906 batches of 64 (249,984 photos).
- Imported the completed result and all five mistake sheets (48 confident validation errors per city). Verified PNGs, CSV row counts, full training budget, accuracy from the confusion matrix, recipe hash 7eb0f0acc97f, and unchanged selection hash 4387ca522155.
- Next: review the mistakes and let the student choose the next change.

- Verified each city has equal total sampling weight. Seed 0 planned draws (of 249,984): seoul 50153, busan 49745, tokyo 50023, osaka 49939, taipei 50124.

### Balanced sampling comparison (seed 0, same 44,133 training photos)

| True city | Previous sampling | Equal city sampling | Change, percentage points |
| --- | ---: | ---: | ---: |
| Seoul | 0.5885 | 0.4875 | -10.10 |
| Busan | 0.3691 | 0.4453 | +7.62 |
| Tokyo | 0.6114 | 0.5071 | -10.43 |
| Osaka | 0.3647 | 0.4539 | +8.92 |
| Taipei | 0.5354 | 0.6005 | +6.51 |

- Overall scores: baseline seed 0, 0.4977; baseline seed 1, 0.4931; no_text_sample seed 0, 0.4938; balanced seed 0, 0.4989.
- Balanced is 0.12 percentage points above baseline seed 0, which uses all training photos. The direct comparison isolating sampling is against no_text_sample, which uses the same selection.
- This is one balanced run. The two baseline seeds differed by 0.46 percentage points, so the measured improvement is small and does not establish reliable superiority across seeds.
- Source: results/balanced_seed0/result.json, results/no_text_sample_seed0/result.json and experiments.csv. Training commit: 481c791.

## 2026-11-10 wider_crop (Track A, completed)

- Student approved the proposed crop-area change from 35–100% to 70–100%: "try it."
- Changed only RandomResizedCrop's scale from (0.35, 1.0) to (0.70, 1.0).
- Kept equal city sampling, the 44,133-photo selection, flips, colour augmentation, optimiser, schedule, batch size and official training budget.
- Direct comparison: balanced seed 0, validation balanced accuracy 0.4989.
- Student's reason: "it will help model to think in humane way, i guess. as human thinks more of a scenery instead of small details, perchance"
- Validation balanced accuracy: 0.4840, compared with balanced seed 0 at 0.4989, a decrease of 1.49 percentage points. Training took 2,246.1 seconds (37.4 minutes).
- Student interpretation: "still not helpful, need to find something more fundamental"
- Local CPU quick check passed (20 steps, 200 validation photos). This is a setup check, not an official experiment result.
- Colab pulled training commit 4e6c630 and confirmed seed 0 on CUDA with 44,133 selected photos and 3,906 batches of 64 (249,984 photos).
- Imported the completed result and all five mistake sheets (48 confident validation errors per city). Verified PNGs, CSV row counts, official training budget, accuracy from the confusion matrix, recipe hash ac3b9e487a3f and unchanged selection hash 4387ca522155.
- Next: consider a more fundamental change and let the student choose the next experiment or submission recipe.

### Wider crop comparison (seed 0, same selection and equal city sampling)

| True city | Balanced | Wider crop | Change, percentage points |
| --- | ---: | ---: | ---: |
| Seoul | 0.4875 | 0.4940 | +0.65 |
| Busan | 0.4453 | 0.4137 | -3.16 |
| Tokyo | 0.5071 | 0.5184 | +1.13 |
| Osaka | 0.4539 | 0.4135 | -4.04 |
| Taipei | 0.6005 | 0.5805 | -2.00 |

- Of the completed local validation results, balanced seed 0 remains highest at 0.4989. The current working recipe is still wider_crop; no unrequested recipe rollback was made.
- One run per changed recipe does not prove a general conclusion about scenery. This result measures the effect of this particular crop-range change with the other current settings.
- Source: results/wider_crop_seed0/result.json, results/balanced_seed0/result.json and experiments.csv. Training commit: 4e6c630.

## 2026-11-10 b_mobilenet320 (Track B, prepared)

- Student request: "yes let's start Track B", approving MobileNetV3-Large at 320 x 320 with pretrained weights.
- Student's stated motivation: "still not helpful, need to find something more fundamental".
- First Track B configuration: torchvision MobileNetV3-Large IMAGENET1K_V2, 320 x 320, 6 epochs, batch size 64, equal city sampling, AdamW learning rate 0.0003, and the starter Track B augmentation (crop area 35–100%, horizontal flips, colour jitter).
- Added an optional --selection argument to train_b.py to carry over the student's 44,133 selected training photos and preserve the 124 exclusions. No validation photos used for training. Track A recipe unchanged.
- This starts a different track with a different model, resolution and training schedule; it is not an isolated test of architecture against Track A.
- Queue: train and copy model plus metadata into submission/, check format and limits without repeating validation, then generate mistake sheets at 320 pixels.
- Validation and student interpretation: pending the run.
- Setup checks passed: selected 44,133 photos, preserved every exclusion, rejected unavailable paths, ran forward/backward, exported ONNX, and measured 4,196,243 parameters / 0.4365664 billion multiply-adds.
- Colab refused a GPU because its usage limit was reached. The Mac MPS fallback passed eight batch-64 training steps at 320 pixels; steps after initial compilation took about 0.86 seconds each on synthetic inputs. This is a short benchmark, not a full-run timing guarantee.
- Starting the same six-epoch model locally on MPS with four data-loader workers; progress printed every 100 batches. Runtime logs go in results/local_logs/.
- Next: complete local training, validate submission format and limits, then generate mistake sheets.
