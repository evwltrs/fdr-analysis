# fdr-analysis by 1nf

## Setup

`sudo apt -y install libgeos-dev`

`pip install -r requirements.txt`

### Windows
> On windows you will be unable to use the GUI or generate maps. For graphs please run `pip install requirements-win.txt` and you are able to use the CLI with the `-t graph` option only.

## GUI

`python3 gui.py`




## CLI

Example:
`python3 cli.py -f fdr.csv -o output.png -t map`

`-f` | File path for the input. Can be `.csv` or `.csv.gz.`

`-o` | File path for the output. Can be `x.png`, `x.jpg`, `x.svg`, `x.pdf` + others

`-t` | Type of output to generate. Can be `graph` or `map`

## Examples
![gui](https://user-images.githubusercontent.com/20270765/193347644-e9353523-3634-4b5a-b93c-4bffe21ae17a.gif)
![graph](https://user-images.githubusercontent.com/20270765/193347725-72698186-e32d-4bd3-927f-adeecedb7a52.png)
![map](https://user-images.githubusercontent.com/20270765/193347739-39781187-79ae-418e-83de-c6faf4089d1e.png)
