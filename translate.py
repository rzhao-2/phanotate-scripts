from Bio import SeqIO
import sys
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Translates open reading frames in a fasta file.')
    parser.add_argument('-tbl', '--translation-table', action="store", default=11, help='NCBI translation table to be used [default: 11]')
    parser.add_argument('-o', '--output', action='store', default=sys.stdout, help='Output file location in fasta format [default: stdout]')
    required = parser.add_argument_group('required')
    required.add_argument('-i', '--input', action='store', required=True, help='Input file in fasta format')
    
    return parser

def translate(filepath, translation_table):
    records = SeqIO.parse(filepath, "fasta")
    proteins = []
    for record in records:
        record.seq = record.seq.translate(table=translation_table, cds=True)
        proteins.append(record)
    return proteins

def main():
    args = get_args().parse_args()

    infile = args.input
    outfile = args.output
    translation_table = args.translation_table

    proteins = translate(infile, translation_table)
    SeqIO.write(proteins, outfile, "fasta")

if __name__ == '__main__':
    main()