# Louis XIII’s cipher letter to Châtillon and Brézé (30 June 1635)

A royal letter from Louis XIII to Châtillon and Brézé, dated 30 June 1635. Its cipher mixes graphical signs and numbers; a group can stand for a letter or a longer unit.

[Cipher Atelier](https://github.com/Cipher-Atelier) · [Research index](https://github.com/Cipher-Atelier/research-index) · [Reading guide](READING_GUIDE.md) · [Verification](verification/README.md)

## Current status — 11 October 2026

The public package contains two small candidate-mapping trials, with 6/18 and 10/21 supplied values. It does not provide a continuous decoded letter. In trial 1 the first six predictions are `[null, null, "s", null, null, "i"]`: `null` means no prediction from the saved table, not an empty plaintext letter.

| Evidence layer | Open this |
| --- | --- |
| Original | [Letter beginning](https://gallica.bnf.fr/ark:/12148/btv1b9058223v/f126.item) · [trial 1 page](https://gallica.bnf.fr/ark:/12148/btv1b9058223v/f127.item) · [trial 2 page](https://gallica.bnf.fr/ark:/12148/btv1b9058223v/f128.item) |
| Recorded tokens / candidate mapping / literal predictions | [Separate tokens, mapping and expected_predictions fields](verification/experiments/louis-xiii-june-1635/partial_predictions.json) |
| Interpretation of the trials | [Trial explanation](verification/experiments/louis-xiii-june-1635/README.md) |
| Broader research narrative | [Investigation](louis-xiii-june-1635/README.md) · [public exclusions](verification/experiments/EXCLUSIONS.json) |

`G_delta → s` and `G_hash → i` reproduce entries in the candidate table. [Check one trial by hand](READING_GUIDE.md#check-one-example-by-hand). Published file fingerprints and retained assignments are checked; original frozen-record hash fields remain metadata and are not recomputed from the original records.

**Unresolved / missing:** no complete source transcription, contemporary key or full translation is included. The broader 969-group inventory and narrative 27/599 or 47/721 claims are outside this checker’s scope, as are the unsuccessful models in the narrative. Prior manuscript viewing limits blindness. June and August investigations remain separate; page URLs do not supply local row or box locators.

## Start here

1. [Read the plain-language guide](READING_GUIDE.md): the document, result, file meanings and one worked check. No programming is required.
2. Open [Two saved partial-prediction trials](verification/experiments/louis-xiii-june-1635/partial_predictions.json) to inspect the saved text or test result itself.
3. Read the [research account](louis-xiii-june-1635/README.md) for historical context, methods, earlier work and unresolved questions.

## Reproduce the checks

Follow the worked example in [the reading guide](READING_GUIDE.md#check-one-example-by-hand). It connects a source record, a key or model assumption, and the saved output. For an independent source check, use the [original-source entry](https://gallica.bnf.fr/ark:/12148/btv1b9058223v/f126.item); images are linked, not redistributed here.

If you use Python, follow the [complete verification instructions](verification/README.md), including download/setup, expected results and troubleshooting. The command from this repository’s top-level folder is:

```sh
python3 verification/check_all.py
```

A successful run means the published files and declared calculation reproduce. It does not establish that every source sign or historical interpretation is correct.

The [Evidence checks workflow](.github/workflows/verify.yml) runs this offline baseline on Python 3.10 and 3.13, without installing dependencies, and checks changed-file whitespace.

## Research scope and limitations

Conditional local partial mappings. Public replay checks frozen 6/18 and 10/21 coverage only; no continuous validated decipherment or complete 969-group replay.

## Contribute

This is part of [Cipher Atelier](https://github.com/Cipher-Atelier), founded by [Maxim Egorov](https://github.com/cayde-6). Explore the [research index](https://github.com/Cipher-Atelier/research-index), [contribution guide](https://github.com/Cipher-Atelier/.github/blob/main/CONTRIBUTING.md), and [step-by-step research workflow](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md).

Read the current result and source limitations, then coordinate a bounded task in an existing issue or use [Work on existing research](https://github.com/Cipher-Atelier/louis-xiii-cipher-letter-june-1635/issues/new?template=research.yml). Fork the repository and submit a focused pull request with your evidence and checks. Independent replication and constructive alternative readings are welcome. See [Start here](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md) for the shared workflow.

## Sources and rights

Source credit and item-specific restrictions remain in the research records. Scans, crops, restricted materials and private correspondence are excluded. No new blanket licence is asserted. AI-assisted work requires evidence checking and does not constitute external human expert review.

[Publication provenance](SOURCE_PROVENANCE.json) records the source commit, retained file hashes and deliberate code/navigation adaptations. The original repository history remains intact.
