# phanotate-scripts
Various scripts for calling phage genes with circular genomes through [PHANOTATE](https://github.com/deprekate/PHANOTATE).

## Requirements
To install:
```
git clone https://github.com/rzhao-2/phanotate-scripts.git
conda install -c bioconda phanotate
conda install -c bioconda trnascan-se
conda install -c bioconda biopython
conda install -c bioconda extern
```

## Usage

### phanotate-circular
```
python phanotate_circular.py -i genome.fa -o transcripts.fa
```
### translate
```
python translate.py -i sequences.fa -o proteins.fa
```
