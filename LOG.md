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

## 2026-11-10 b_mobilenet320 (Track B, completed)

- Student request: "yes let's start Track B", approving MobileNetV3-Large at 320 x 320 with pretrained weights.
- Student's stated motivation: "still not helpful, need to find something more fundamental".
- First Track B configuration: torchvision MobileNetV3-Large IMAGENET1K_V2, 320 x 320, 6 epochs, batch size 64, equal city sampling, AdamW learning rate 0.0003, and the starter Track B augmentation (crop area 35–100%, horizontal flips, colour jitter).
- Added an optional --selection argument to train_b.py to carry over the student's 44,133 selected training photos and preserve the 124 exclusions. No validation photos used for training. Track A recipe unchanged.
- This starts a different track with a different model, resolution and training schedule; it is not an isolated test of architecture against Track A.
- Queue: train and copy model plus metadata into submission/, check format and limits without repeating validation, then generate mistake sheets at 320 pixels.
- Validation balanced accuracy: 0.5556.
- Student interpretation: "reasonably better result,,, changing most of the model & environment could be helpful than fine-tuning bad model"
- Setup checks passed: selected 44,133 photos, preserved every exclusion, rejected unavailable paths, ran forward/backward, exported ONNX, and measured 4,196,243 parameters / 0.4365664 billion multiply-adds.
- Colab refused a GPU because its usage limit was reached. The Mac MPS fallback passed eight batch-64 training steps at 320 pixels; steps after initial compilation took about 0.86 seconds each on synthetic inputs. This is a short benchmark, not a full-run timing guarantee.
- Starting the same six-epoch model locally on MPS with four data-loader workers; progress printed every 100 batches. Runtime logs go in results/local_logs/.
- Follow-up completed: validated the exported model and generated all five mistake sheets.

- Confirmed the actual local run on MPS loaded selection hash 4387ca522155 and reached epoch 1/6, batch 100/689, loss 1.597 after 106 seconds. Training was launched from commit 44d0449. Planned total: 4,134 batches, 264,576 training presentations.

### Completed Track B result

- Finished all six epochs locally on MPS: 4,134 batches and 264,576 training presentations, in 3,334.6 seconds (55.6 minutes).
- Validation balanced accuracy: 0.5556, compared with best measured Track A (balanced seed 0) at 0.4989: +5.67 percentage points. Compared with the latest wider_crop result, +7.16 percentage points.
- These runs change architecture, starting weights, resolution, augmentation and training schedule together. The result does not isolate which change produced the gain; a single run also does not measure run-to-run uncertainty.
- The Track B starter does not set a random seed; the experiment row correctly leaves seed blank.

| True city | Best Track A (balanced) | Track B MobileNet320 | Change, percentage points |
| --- | ---: | ---: | ---: |
| Seoul | 0.4875 | 0.5762 | +8.87 |
| Busan | 0.4453 | 0.4784 | +3.31 |
| Tokyo | 0.5071 | 0.6117 | +10.46 |
| Osaka | 0.4539 | 0.4784 | +2.45 |
| Taipei | 0.6005 | 0.6331 | +3.26 |

- Saved matching model and metadata to results/b_mobilenet320/ and submission/. Metadata records IMAGENET1K_V2, image size 320 and selection hash 4387ca522155.
- The final exported model passed the unchanged check_submission.py --no-val: "format and limits: OK"; 16.8 MB, 4.20 million parameters and 0.44 billion multiply-adds (limits: 12 million and 2.0 billion).
- Training, validation, export and the experiments.csv write completed, but Python then hung during interpreter shutdown waiting for its multiprocessing bookkeeping helper (confirmed by a process sample). Stopped only that finished process and helper; exit 143 reflects this cleanup, not interrupted training. Ran the final format check independently and started mistake sheets separately from the saved model.
- Sources: experiments.csv and results/local_logs/b_mobilenet320_run1.txt. Code launched from 44d0449; result row records 8620002, the later log-only commit present at completion.

- Mistake-sheet generation completed successfully on all 12,077 validation photos. Verified five PNGs and their 48-row CSVs. Exported-model accuracy reconstructed from each city's printed error counts matches experiments.csv (0.5556 overall, all five per-city values). Source: results/local_logs/b_mobilenet320_mistakes.txt.
- Next: review the Track B mistakes and let the student choose whether to submit this model or run another experiment.

## 2026-11-10 b_mixup320 (Track B, running locally)

- Student request: "try mixup - try colab first & dont run locally before my confirmation".
- Student's reason: "Test whether reducing reliance on individual cues improves generalisation. It is an established training method, but improvement here is uncertain."
- Add optional Mixup with alpha 0.2: draw a batch-level mixing coefficient from Beta(0.2, 0.2), blend a randomly paired batch, and weight the two label-smoothed cross-entropy losses by the same coefficient. Validation photos are not mixed.
- Keep the MobileNetV3-Large IMAGENET1K_V2 starting weights, image size 320, six epochs, batch size 64, equal city sampling, selection hash 4387ca522155, optimiser, schedule and other augmentations unchanged. Train from the pretrained starting weights, not the prior trained model.
- Direct comparison: b_mobilenet320, validation balanced accuracy 0.5556. Neither run fixes a seed; Colab CUDA versus the previous MPS run also introduces a device difference, so any score difference cannot be attributed exclusively to Mixup.
- Static syntax check passed without importing the training module or starting a local model. No local training is authorised without further student confirmation.
- Next: try the Colab GPU. If unavailable, stop and report; no automatic local fallback. Score and interpretation pending.

- Tried reconnecting to the Colab T4 GPU after pushing 8fdbec9. Colab displayed "GPU 백엔드에 연결할 수 없음" and explicitly cited current usage limits. No GPU session or Mixup training was started. Did not select "Connect without GPU". The experiment remains queued; awaiting the student's decision before any local training.

- Student approved normal local training after the Colab refusal: "then, lets just run it locally, normally." Starting the prepared six-epoch experiment on MPS with batch size 64 and four loader workers, matching the prior local run. No reduction in resolution or training budget. Confirmed the previous 55.56% model remains preserved in results/b_mobilenet320/.
- Local launch wrapper exits only after train_b.py returns successfully and flushes output, avoiding the previously confirmed interpreter-finalisation hang after all artifacts and the experiment row are saved. It does not change the training procedure.

- Confirmed actual training progress: epoch 1/6, batch 100/689, loss 1.603 after 94 seconds on MPS, Mixup alpha 0.2, selection hash 4387ca522155. Training source launched from b1140bb. Live output: results/local_logs/b_mixup320_run1.txt.
