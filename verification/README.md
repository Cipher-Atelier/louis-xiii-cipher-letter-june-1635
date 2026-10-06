# Verify louis-xiii-june-1635

[Repository overview](../README.md) · [Read the result and check one example by hand](../READING_GUIDE.md)

## What this check does

The supported command first checks the published file fingerprints in `SHA256SUMS.txt`, then repeats this investigation’s saved calculation. A fingerprint (SHA-256) identifies exact file bytes; it is not a scientific correctness score.

The replay checks recorded tokens, frozen input/key hashes and partial substitutions. It does not replay all 969 groups or validate the broader 47-entry/721-position research table.

It uses Python’s standard library, makes no network requests, and needs no downloaded scans or extra packages for this default check. It does not fit a new key or edit the research evidence.

## Download and open the folder

1. On [this repository’s main page](https://github.com/Cipher-Atelier/louis-xiii-cipher-letter-june-1635), choose **Code → Download ZIP**, following [GitHub’s download instructions](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives).
2. Extract the whole ZIP. Keep its folders and files together; do not download only `check_all.py`.
3. Open a terminal in the extracted top-level folder: it contains `README.md`, `SHA256SUMS.txt` and the `verification` folder. For example, after navigating to its parent directory:

```sh
cd louis-xiii-cipher-letter-june-1635-main
```

If you already use Git, cloning the full repository is an alternative:

```sh
git clone https://github.com/Cipher-Atelier/louis-xiii-cipher-letter-june-1635.git
cd louis-xiii-cipher-letter-june-1635
```

## Run the supported check

Use **Python 3.10 or later**. On macOS/Linux, check the installed version and run:

```sh
python3 --version
python3 verification/check_all.py
```

On Windows, if the Python launcher is installed, use:

```powershell
py -3 --version
py -3 verification/check_all.py
```

If your Python command is `python` rather than `python3` or `py -3`, use that command after confirming it is Python 3.10+. If Python is absent, obtain it from [python.org](https://www.python.org/downloads/) or your operating system’s supported installation method.

Run ordinary Python, with no `-O`/`-OO` options and no `PYTHONOPTIMIZE` setting that enables optimization: the checker relies on assertions.

## What a successful run looks like

The command exits successfully and prints a JSON report with top-level `"status": "passed"`. It also reports how many fingerprinted files were checked. That file count can change when documentation is updated.

The following are the expected status/topic/replay fields; the actual report also includes `files_checked` and scope limits:

```json
{
  "status": "passed",
  "topic": "louis-xiii-june-1635",
  "replay": {
    "louis-xiii-june-1635": {
      "status": "passed",
      "partial_coverage": [
        [
          6,
          18
        ],
        [
          10,
          21
        ]
      ],
      "scope": "Frozen coverage, not plaintext accuracy or global blindness"
    }
  }
}
```

In ordinary words: **The two preserved coverage pairs are [6, 18] and [10, 21]. There is no public full-letter plaintext to reproduce.**

## What passing does not establish

Facing clear text and earlier printed text are historical evidence, not an exact answer key for every cipher group. Uncertain boundaries, sign lengths and conflicting assignments prevent a complete reading; related 1635 letters cannot simply share a key without proof.

Passing verifies that these published inputs and saved rules give the recorded result. It does not certify source-image transcription, historical truth, a unique interpretation, author identity, discovery priority or external expert review. To inspect those questions, follow [the manual example and source-checking route](../READING_GUIDE.md#check-one-example-by-hand).

## If it fails

| Symptom | What to do |
| --- | --- |
| Python command not found, or version below 3.10 | Install/use Python 3.10+; confirm its version first |
| Cannot open `verification/check_all.py` | Move into the extracted repository’s top-level folder |
| Missing file | Extract the complete ZIP again; retain the directory structure |
| `Hash mismatch: ...` | Compare with an untouched download of the same version; edits change the fingerprint |
| Optimization warning | Run without `-O`/`-OO` and disable any `PYTHONOPTIMIZE` setting |
| Assertion, replay mismatch or another error on an untouched package | Save the complete error, Python version and repository commit/download reference; report it in a [research issue](https://github.com/Cipher-Atelier/louis-xiii-cipher-letter-june-1635/issues/new?template=research.yml) |

Do not change the evidence, expected results or fingerprints just to make a failing check pass. If reporting reproduction, record the commit SHA shown on GitHub; a later `main` download may contain documentation updates. A [commit-specific archive](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives#source-code-archive-urls) pins the file version.

## Preserved publication scope

Conditional local partial mappings. Public replay checks frozen 6/18 and 10/21 coverage only; no continuous validated decipherment or complete 969-group replay.

969 physical groups and partial mappings; no continuous validated decipherment. Conditional correspondence and exposure prevent counting mappings as solved text. Later 47/721 claims require their own exact artifact check.

From the repository root run `python3 verification/check_all.py` with Python 3.10 or later, without optimization. It verifies the repository checksum inventory and invokes only [experiments/verify.py](experiments/verify.py). The check uses the standard library and makes no network requests. Obtain source images separately under their provider terms for visual review. Source credit is not image redistribution permission.

See the [research record](../louis-xiii-june-1635/README.md) and [machine-readable scope](TOPIC_SCOPE_INDEX.json). Successful arithmetic or exact output replay does not prove historical truth, unique interpretation or priority.
