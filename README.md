# Louis XIII’s cipher letter to Châtillon and Brézé (30 June 1635)

A royal letter from Louis XIII to Châtillon and Brézé, dated 30 June 1635. Its cipher mixes graphical signs and numbers; a group can stand for a letter or a longer unit.

## What has been found?

This is an unfinished key-reconstruction investigation. Some local assignments and words are plausible, but there is no reliable continuous decipherment or full translation. The public checker tests two saved short-passage predictions.

A small example from the recorded result:

```text
G_delta → s; G_hash → i
```

These are candidate assignments in a saved test table. The labels name cipher shapes; they are not words recovered from the letter.

## Start reading

1. [Read the plain-language guide](READING_GUIDE.md): the document, result, file meanings and one worked check. No programming is required.
2. Open [Two saved partial-prediction trials](verification/experiments/louis-xiii-june-1635/partial_predictions.json) to inspect the saved text or test result itself.
3. Read the [research account](louis-xiii-june-1635/README.md) for historical context, methods, earlier work and unresolved questions.

## How can I check it?

Follow the worked example in [the reading guide](READING_GUIDE.md#check-one-example-by-hand). It connects a source record, a key or model assumption, and the saved output. For an independent source check, use the [original-source entry](https://gallica.bnf.fr/ark:/12148/btv1b9058223v/f126.item); images are linked, not redistributed here.

If you use Python, follow the [complete verification instructions](verification/README.md), including download/setup, expected results and troubleshooting. The command from this repository’s top-level folder is:

```sh
python3 verification/check_all.py
```

A successful run means the published files and declared calculation reproduce. It does not establish that every source sign or historical interpretation is correct.

## Precise research scope

Conditional local partial mappings. Public replay checks frozen 6/18 and 10/21 coverage only; no continuous validated decipherment or complete 969-group replay.

This is part of [Cipher-Atelier](https://github.com/Cipher-Atelier), founded by [Maxim Egorov](https://github.com/cayde-6). Explore the [research index](https://github.com/Cipher-Atelier/research-index), [contribution guide](https://github.com/Cipher-Atelier/.github/blob/main/CONTRIBUTING.md), and [step-by-step research workflow](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md).

Source credit and item-specific restrictions remain in the research records. Scans, crops, restricted materials and private correspondence are excluded. No new blanket licence is asserted. AI-assisted work requires evidence checking and does not constitute external human expert review.

[Publication provenance](SOURCE_PROVENANCE.json) records the source commit, retained file hashes and deliberate code/navigation adaptations. The original repository history remains intact.

## Contribute to this investigation

Read the current result and source limitations, then coordinate a bounded task in an existing issue or use [Work on existing research](https://github.com/Cipher-Atelier/louis-xiii-cipher-letter-june-1635/issues/new?template=research.yml). Fork the repository and submit a focused pull request with your evidence and checks. Independent replication and constructive alternative readings are welcome. See [Start here](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md) for the shared workflow.
