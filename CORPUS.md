# The corpus: 900 unique strategies from 53 repositories

This is, as far as I can establish, **the largest deduplicated index of public
freqtrade strategies that exists** — and the claim is written so that you can
refute it. The search queries are published below. Run them, find a repository I
missed, and the number changes.

What is indexed here is **measurements**, not code. Each strategy gets a card
with its numbers, or with the named reason it could not be measured. The
strategies themselves stay in their authors' repositories under their authors'
licences.

## Scale

```
repositories indexed                        53
class occurrences (with duplicates)      2,567
UNIQUE STRATEGY CLASSES                    900
share that are copies                      65%

largest single repository   jaredrsommer/freqtradestrategies   558 classes
this corpus is larger by                                       1.6x
```

## Where the originals actually come from

Sorted by **first appearances**, not file count. The distinction is the whole
point: a repository can hold five hundred strategies and contribute none.

```
repository                                    classes   first seen   copies
PeetCrypto/freqtrade-stuff                        346          312     10%
davidzr/freqtrade-strategies                      464          166     64%
TheoBrigitte/freqtrade                            220          117     47%
jaredrsommer/freqtradestrategies                  558           77     86%
mlsys-io/PortfolioBench                            67           66      1%
Foxel05/freqtrade-stuff                            31           31      0%
markdregan/FreqAI-Marcos-Lopez-De-Prado            27           25      7%
MelvynClark/Freqtrade-Strategy                     21           21      0%
werkkrew/freqtrade-strategies                      50            8     84%
freqtrade/freqtrade-strategies                     68            7     90%
...
keithorange/HUGE_FreqTrade_Strategy_Collection    477            0    100%
p-zombie/freqtrade                                 35            0    100%
```

**Seventeen of the 53 repositories contributed no original strategy at all.**
The most striking is a repository whose name announces a *huge collection*: 477
classes, every one of them already present elsewhere.

The small personal repositories are the original ones. `Foxel05` contributed 31
of 31, `MelvynClark` 21 of 21, `mikedigriz` 7 of 7. The large collections are
mostly re-postings of each other.

> **"First seen" means alphabetical scan order, not authorship.** Who copied
> from whom is not visible in the code, and this index does not claim to know.

## The search, so you can extend or refute it

Repositories were found with the GitHub search API using these queries, then
filtered to those containing classes that inherit `IStrategy`:

```
freqtrade+strategies          freqtrade+strategy+in:name
freqtrade+strategy            freqtrade+in:readme+IStrategy
topic:freqtrade               populate_entry_trend
freqtrade-strategies          populate_buy_trend
freqtrade+hyperopt+strategies NostalgiaForInfinity
freqtrade+bot+strategies
```

**This is not proof of exhaustiveness.** GitHub search does not return
everything, private and archived repositories are invisible, and strategies
posted in gists, forums or Discord are not covered. The claim is "the largest I
could find with these queries", and the queries are here precisely so the claim
can be beaten.

## A size filter that was wrong, and how it was found

Four repositories were initially excluded for exceeding 60 MB. Checking them
showed the filter used the wrong signal entirely — they are large because of
stored backtest results, not strategies:

```
Rikj000/MoniGoMani     271 MB    21 .py files, 2 with strategies
imsatoshi/GeneTrader   226 MB    49 .py files
obseries/...-ichiv1    111 MB     2 .py files
```

Repository size says nothing about strategy count. The filter was replaced: the
tree is listed through the API and only `.py` files containing `IStrategy` are
fetched. Size stops mattering, and so does the caveat that used to accompany it.

One repository (`ShahAnuj2610/my-freqtrade`) could not be cloned at all — it
contains filenames with colons, which Windows rejects. Fetching files
individually recovered it. That is now the default method rather than a
workaround.

## Reproduce

```bash
python harvest.py <owner/repo> [<owner/repo> ...]   # fetch strategy files only
python census_repos.py                              # this table
python corpus.py --shard k/5                        # measure
python ledger.py --pop=corpus            # the ladder, one population at a time
python anatman.py                                   # every lived defect, as a test
```
