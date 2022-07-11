# phanotate-scripts
Various scripts for calling phage genes with circular genomes through [PHANOTATE](https://github.com/deprekate/PHANOTATE).

## Requirements
To install:
```
git clone https://github.com/rzhao-2/phanotate-scripts.git
cd phanotate-scripts
conda env create -f environment.yml -n phanotate-scripts
conda activate phanotate-scripts
```

## Usage

### phanotate_circular
```
cd phanotate-scripts
conda activate phanotate-scripts
bin/phanotate_circular -i genome.fa -o transcripts.fa
```
### phanotate_translate
```
cd phanotate-scripts
conda activate phanotate-scripts
bin/phanotate_translate -i sequences.fa -o proteins.fa
```
