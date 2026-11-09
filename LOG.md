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

## 2026-11-10 no_text_sample (Track A, prepared)

- Student's requested rule: "lets exclude photos which contains letters for this time"
- Student authorized agent review and training: "do the same for other cities' images, then proceed training without them"
- Agent visually reviewed the five existing training sample sheets (32 photos per city, 160 total), checking larger originals where needed.
- Excluded clear writing in any language, including signs, subtitles, watermarks and text on objects. Kept uncertain cases and numbers-only images.
- Excluded 124 sampled training photos: Seoul 21, Busan 26, Tokyo 26, Osaka 25, Taipei 26. This is not a text-free dataset: the other training photos were not reviewed.
- Full numbered review: scripts/text_photo_review.csv. Reapply with scripts/exclude_sample_text.py. No source photos deleted; validation unchanged; starter recipe unchanged.
- Student's earlier observation: "if there is hangul in the image, it is quite easy to mistake it as busan for this model."
- Validation and interpretation: pending the training result and student's interpretation.
- Next: train no_text_sample with seed 0 and compare with the baseline.
