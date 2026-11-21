# The joke the reviewer laughs at

[![make.fun · the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/ifulchina-ops/the-joke-the-reviewer-laughs-at-20261121-0329/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/ifulchina-ops/the-joke-the-reviewer-laughs-at-20261121-0329/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)

A one-line joke about working beside AI coding agents, written by a small
Python program for [make.fun](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)'s
"The joke the reviewer laughs at" bounty ($35, top 20 paid).

## The joke

> My AI agent writes 500 lines a minute and reviews none of them; I write five lines a day and review all of them — somehow I'm still the junior in this relationship.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` is pure stdlib, needs no network, and writes exactly one line
(1–280 Unicode code points) to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(or `/output/entry.txt` when the variable is unset).

## License

MIT — see [LICENSE](LICENSE).
