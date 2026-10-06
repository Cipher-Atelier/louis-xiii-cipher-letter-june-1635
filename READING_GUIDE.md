# Read this investigation

[Repository overview](README.md) · [Technical verification](verification/README.md)

## Understand the document

A royal letter from Louis XIII to Châtillon and Brézé, dated 30 June 1635. Its cipher mixes graphical signs and numbers; a group can stand for a letter or a longer unit.

Start with the [source catalogue or manuscript](https://gallica.bnf.fr/ark:/12148/btv1b9058223v/f126.item). It identifies the historical object. The source image is the evidence; the tables in this repository are recorded readings of that evidence.

## Read the current result

This is an unfinished key-reconstruction investigation. Some local assignments and words are plausible, but there is no reliable continuous decipherment or full translation. The public checker tests two saved short-passage predictions.

Open [Two saved partial-prediction trials](verification/experiments/louis-xiii-june-1635/partial_predictions.json) and the [research account](louis-xiii-june-1635/README.md). A literal preserves the recorded output before making it smoother to read. An English explanation or translation adds interpretation and should not silently repair it.

Example:

```text
G_delta → s; G_hash → i
```

These are candidate assignments in a saved test table. The labels name cipher shapes; they are not words recovered from the letter.

Facing clear text and earlier printed text are historical evidence, not an exact answer key for every cipher group. Uncertain boundaries, sign lengths and conflicting assignments prevent a complete reading; related 1635 letters cannot simply share a key without proof.

## Check one example by hand

1. Open [partial_predictions.json](verification/experiments/louis-xiii-june-1635/partial_predictions.json). In trial `version: 1`, `tokens` lists 18 recorded cipher groups and `mapping` lists the candidate values available at that time.
2. Count token positions from 1. The first six behave as follows:

| Position | Token | Available candidate value |
| --- | --- | --- |
| 1 | `G_cross_slant` | no entry → `null` |
| 2 | `N83_dd` | no entry → `null` |
| 3 | `G_delta` | `s` |
| 4 | `N74_dd` | no entry → `null` |
| 5 | `G_venus` | no entry → `null` |
| 6 | `G_hash` | `i` |

3. Compare with the first six entries of `expected_predictions`: `[null, null, "s", null, null, "i"]`. `null` means the saved table makes no prediction for that token.
4. Count the complete non-null predictions: six of 18 in trial 1, ten of 21 in trial 2. These count supplied values, not independently verified correct letters. Each trial includes its own source URL for comparing the recorded groups with the manuscript.

The larger research inventory describes 969 physical groups and broader partial tables. Those broader claims are not what this small public replay checks. The manuscript had already been viewed during selection; the saved predictions are not globally blind experiments.

## Choose the check you want

- **Understand the result:** read the literal/test result beside the research account. You can do this in GitHub without installing anything.
- **Check the calculation:** follow the example above, then [run the supported Python check](verification/README.md). This verifies the saved transformation or declared model.
- **Check the source:** compare recorded signs with the original image and retain disagreements. Scans/crops are not included; obtain access under the provider’s terms. Original coordinates, when present, refer to the specified image version.
- **Evaluate the historical reading:** examine alternative signs, key evidence, language, document boundaries and prior readings. A successful calculation does not settle these questions.

To report a problem, use [Work on existing research](https://github.com/Cipher-Atelier/louis-xiii-cipher-letter-june-1635/issues/new?template=research.yml). Give the file, row/position, source reference, your observation, and what changes in the output. Distinguish a different source reading from a changed key or an editorial interpretation.

## What the files mean

| Open this | It contains |
| --- | --- |
| [Research account](louis-xiii-june-1635/README.md) | Historical context, method, interpretation, credits and limits |
| [Two saved partial-prediction trials](verification/experiments/louis-xiii-june-1635/partial_predictions.json) | The saved text or bounded test result |
| [Trial tokens, mappings and expected outputs](verification/experiments/louis-xiii-june-1635/partial_predictions.json) | The recorded input/assignments used in the example |
| [Candidate mappings in each trial](verification/experiments/louis-xiii-june-1635/partial_predictions.json) | The proposed transformation, historical key, or tested assumptions |
| [Technical verification](verification/README.md) | Setup, command, expected output and what the check covers |
| [Source scope](verification/TOPIC_SCOPE_INDEX.json) | Machine-readable release boundaries and omitted material |
| [Publication provenance](SOURCE_PROVENANCE.json) | Where this package came from and what documentation changed |

CSV and TSV are tables: GitHub or a spreadsheet can display them. TSV uses tabs between columns. JSON stores named fields and lists; `null` means no value in that field, and its interpretation depends on the record. You do not need to start by reading every JSON file.

## Terms used in the research

- **Ciphertext:** the recorded encrypted signs or letters.
- **Key/mapping:** the rule assigning output to a cipher sign. It may be a hypothesis, a surviving historical key, or an assumption in a test; those are different kinds of evidence.
- **Literal reading:** the saved output with gaps and awkward wording retained, before editorial translation or repair.
- **Coverage:** how many recorded positions receive a value. It does not measure how many values are historically correct.
- **Frozen:** saved unchanged at a particular stage so a later correction cannot replace an earlier test result.
- **Replay:** applying saved rules to saved inputs again. It checks reproducibility within the declared scope.
- **Training/heldout:** material used to fit a rule, and material excluded from that fitting. Prior viewing or later correction can limit how independent a heldout test is; read the case-specific account.
