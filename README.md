# plumcot-prodigy

Prodigy recipes for PLUMCOT dataset

## Installation


```bash
# clone this repository
$ git clone https://github.com/hbredin/plumcot-prodigy.git
$ cd plumcot-prodigy

# create and activate conda environment
$ conda env create -f environment.yml
$ conda activate plumcot-prodigy

# install prodigy 
$ (plumcot-prodigy) pip install prodigy.*.whl

# download spaCy english model
$ (plumcot-prodigy) python -m spacy download en_core_web_sm

# this assumes that data/ directory contains the following files:
# * TheBigBangTheory.Season01.Episode01.aligned
# * TheBigBangTheory.Season01.Episode01.mkv
$ (plumcot-prodigy) prodigy check_forced_alignment my_dataset -F plumcot_prodigy/recipes.py

Added dataset my_dataset to database SQLite.

✨  Starting the web server at http://localhost:8080 ...
Open the app in your browser and start annotating!

```

![check_forced_alignment recipe](screenshots/check_forced_alignment.jpg)
