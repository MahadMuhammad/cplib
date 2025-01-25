## Overview

This repository contains a custom tools/scripts for competitive programming. It includes various utilities and templates to streamline the process of setting up, running, and testing competitive programming problems.

### Chrome Web Extension

This repository uses the [Competitive Companion](https://github.com/jmerle/competitive-companion) Chrome web extension for fetching problem data. This extension allows you to quickly and easily download problem statements and test cases from various competitive programming websites.

## Usage

To clone this repository and set up your environment, follow these steps:
```sh
git clone https://github.com/MahadMuhammad/cplib.git ~/cplib
cd ~/cplib
```

Add the following to your shell configuration file (e.g., `.bashrc`, `.zshrc`):

```sh
export PATH="$HOME/cplib/utils/gen:$PATH"
alias gen='gen -o'
```

Then, source your shell configuration file to apply the changes:

```sh
source ~/.bashrc  # or source ~/.zshrc
```

```sh
gen [output_file_name] [-p]
```

#### Options

- `-o, --output_file`: Path to the output file (default: `A.cpp`).
- `--author`: Author name to include in the header (default: `mahad`).
- Optional `-p, --python`: Generate a Python file with a Python header comment.

### `utils/dbrun` Script

The dbrun script is used for building and testing competitive programming problems.

#### Usage

```sh
dbrun [file_name]
```


### `utils/download_prob` Script

The download_prob script is used to download and set up problems from Competitive Companion.

#### Usage

```sh
download_prob
```

#### Options

- `--echo`: Just echo received responses and exit.
- `--dryrun`: Don't actually create any problems.
- `-n COUNT, --number COUNT`: Number of problems to download.
- `-b COUNT, --batches COUNT`: Number of batches to download (default: 1 batch).
- `-t TIME, --timeout TIME`: Timeout for listening to problems in seconds.