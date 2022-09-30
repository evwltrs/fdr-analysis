# fdr-analysis by 1nf

## Setup

`sudo apt -y install libgeos-dev`

`pip install -r requirements.txt`

## GUI

`python3 gui.py`

## CLI

Example:
`python3 cli.py -f fdr.csv -o output.png -t map`

`-f` | File path for the input. Can be `.csv` or `.csv.gz.`

`-o` | File path for the output. Can be `x.png`, `x.jpg`, `x.svg`, `x.pdf` + others

`-t` | Type of output to generate. Can be `graph` or `map`
