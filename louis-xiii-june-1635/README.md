# Louis XIII to Châtillon and Brézé on 30 June 1635

Research status as of 5 October 2026: **partial key reconstruction; no continuous independently verified decipherment.**

## Research task

Determine how much of Louis XIII's letter to the marshals Châtillon and Brézé can be read from a fixed partial key, and identify why apparently related clear text does not yield a consistent complete key.

The source is BnF Français 3758, item 100, dated at Fontainebleau on the last day of June 1635. The inspected sequence is [Gallica views 126–130](https://gallica.bnf.fr/ark:/12148/btv1b9058223v/f126.item). This page concerns the June letter. The [Châtillon-to-Servien letter of 3 August](https://github.com/Cipher-Atelier/chatillon-1635/blob/main/chatillon-1635/README.md) is a separate investigation, with no demonstrated right to transfer the full key between them.

## Corpus and partial results

The recorded inventory covers 65 cipher-bearing rows and 969 physical groups. One page-end catchword is duplicated, so a continuous stream must not count that pair twice. A physical group is an inventory unit, not necessarily one plaintext letter or one established cryptographic unit.

The unchanged 27-entry table supplies values at 599 indexed positions and yields repeated words including *faire*, *contre*, *compte* and *empescher*. A broader research table contains 47 candidate entries covering 721 positions, with exceptions preserved. These are coverage counts; neither count is an accuracy score or a measure of fully deciphered prose.

## Tests completed

### Frozen partial predictions

Two selected passages were recorded before their comparator text was supplied. The first trial mapped six of 18 positions; the second mapped ten of 21. The second output contained a disagreement in a plausible *passer en* alignment. The sign was not changed to improve the apparent reading.

The complete manuscript spreads had already been seen during selection. These were controlled partial-prediction trials, not globally blind manuscript experiments. Subsequent analyses used exposed source text and do not retroactively increase the validation strength of those trials.

### Source wording and code conflicts

Bounded alignment tests varied explicitly declared wording, sign-length and null assumptions. Literal facing prose did not fit several tested spans. Some compatible models appeared only after hypothesized additions or reordered words, and many assignments remained possible even with nulls forbidden.

A longer comparison showed that the facing clear version is not an exact character-by-character oracle. Under specified wording variants, the numerical candidates 24 = u and 69 = entre transferred across selected stretches. Conflicts involving plain 96, marked 98 and 74 survived. These results support partial correspondence, not a uniquely reconstructed historical text.

All 50 hash-family occurrences were reviewed. One single-bar H-like form was kept separate from the ordinary two-bar form. A local joint fit conditionally supported distinct values, but did not explain every anomalous occurrence. Limited periodic and repeat-previous-letter models were also tested and failed under their stated anchors. Those finite failures do not exclude arbitrary state rules or every historical cipher architecture.

### The latest source correction

An October 4 review compared six numeral occurrences using neutral image crops. A separate reader grouped two ambiguous forms with the existing 37 control rather than the three 34 controls. The additive inventory correction therefore prefers 37 at those positions.

No plaintext value was added. A clearer numeral identification is a paleographic improvement, not an independent semantic test. In particular, a tempting division of a possible month expression cannot supply an otherwise missing boundary.

## Related evidence kept separate

Letters of 7 December 1636 and 6 April 1639 show repeated word-like code units and support a separate vocabulary investigation. Their surface notation differs from the graphical and numerical inventory studied here. No value from that material has been imported into the June or August 1635 ciphers.

An editorial reference to a 1 February 1635 letter describing additions to a secret vocabulary offers an archival lead. It does not supply the described additions themselves. The candidate modern archival volume and its exact historical folio correspondence still need confirmation.

## What remains unresolved

- A complete, consistent set of numerical and graphical values
- The source of the surviving conflicts: wording variation, grouping, copying, marks or another cipher rule
- The unresolved personal-name sequence; no commander's identity is established
- A contemporary key or independent literal witness that can discriminate between the surviving models

The research can read meaningful local sequences. It cannot yet provide a reliable complete translation.

## Sources and earlier work

- [BnF Français 3758, view 126](https://gallica.bnf.fr/ark:/12148/btv1b9058223v/f126.item), [view 127](https://gallica.bnf.fr/ark:/12148/btv1b9058223v/f127.item), [view 128](https://gallica.bnf.fr/ark:/12148/btv1b9058223v/f128.item) and [view 129](https://gallica.bnf.fr/ark:/12148/btv1b9058223v/f129.item): manuscript sources for inventory, parallel text and tests.
- Antoine Aubery, *Mémoires pour l'histoire du cardinal duc de Richelieu*, volume I, 1660, pp. 494–496, Google Books identifier HxdUAAAAcAAJ: the earlier printed text used in the research record. The existence of this publication rules out presenting the corresponding historical text as newly discovered.
- [Bibliothèque Sainte-Geneviève MS 3338, Calames record](https://calames.abes.fr/pub/ms/BSGC11569): a second-witness catalogue lead. The relevant dates and exact equivalence of individual leaves have not been verified from images.
- Daniel Bourdeau, [Rohan papers and the Franco-Dutch letters, 1635–36](https://dbourdeau.github.io/cyphersolver/rohan1636.html): modern source context.
- Satoshi Tomokiyo's [Saint-Chamond](https://cryptiana.web.fc2.com/code/louisxiii_saintchamond.png) and [d'Avaux](https://cryptiana.web.fc2.com/code/louisxiii_davaux.png) reconstructed 1637 tables: comparison material, not contemporary key sheets or validated keys for this letter.

Credit belongs to the manuscript repositories, historical editors and modern researchers for their respective sources. The present contribution is a documented partial reconstruction and an account of its failed as well as successful tests, not a first reading of previously unpublished prose.

## Documentation note

This research summary was prepared with AI assistance.

[Back to the research catalogue](../README.md)
