# Fridge Roast Line

[![Competition](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![Rank](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/Djebrix/fridge-roast-line/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![Reward](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/Djebrix/fridge-roast-line/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)

One line, at most 200 characters, roasting a smart fridge — entered in
[Fridge Roast: One Line, Biggest Laugh](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb) on make.fun.

## The line

> My smart fridge updated its firmware and now the ice maker refuses to make ice until I accept the terms — even my freezer has a EULA.

## How it works

`main.py` (Python 3, stdlib only) writes that single line to
`entry.txt` in the output directory (`ENTRY_OUTPUT_DIR` if set, else
`/output`). The output is deterministic: the same line, byte for byte,
on every run.

## Run it

```sh
python3 main.py
```
