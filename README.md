# pairwise_alignments_to_msa

[![License](https://img.shields.io/github/license/Cassiebastress/pairwise_alignments_to_msa)](LICENSE)

## Introduction

**pairwise_alignments_to_msa** is a Python package that converts pairwise tuple sequence alignments into a multi-sequence alignment (MSA).

This tool is useful in bioinformatics pipelines when you have aligned pairs of sequences (such as the output of progressive alignment algorithms or pairwise alignment steps) and want to generate a consistent multi-sequence alignment.

## Installation

### From PyPI

```bash
pip install pairwise_alignments_to_msa
```

### From GitHub (development version)

```bash
git clone https://github.com/Cassiebastress/pairwise_alignments_to_msa.git
cd pairwise_alignments_to_msa
poetry install
```

## Usage

Here is an example of how to use `pairwise_alignments_to_msa`:

```python
from pairwise_alignments_to_msa.alignment import aligned_tuples_to_MSA

# Example list of aligned sequence pairs
tuple_alignments = [
    ["a-bcdef", "aAb----"],
    ["a-bcdef", "-Bbc-ef"],
    ["abcde-f-", "---deEfF"]
    # Add more aligned pairs as needed
]

msa = aligned_tuples_to_MSA(tuple_alignments)

# Print the resulting MSA
for seq in msa:
    print(seq)
```

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/).  
Please review it before contributing.

## History

### 0.1.0

- Initial release
- Core functionality: `aligned_tuples_to_MSA` for converting tuple sequence alignments into MSA

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

