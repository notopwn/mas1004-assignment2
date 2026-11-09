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
