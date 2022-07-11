#!/usr/bin/env python3

import unittest
import os.path
import tempfile
from Bio import SeqIO

import extern

path_to_data = os.path.join(os.path.dirname(os.path.realpath(__file__)),'data')
path_to_script = os.path.join(os.path.dirname(os.path.realpath(__file__)),'..','bin', 'phanotate-translate')

class Tests(unittest.TestCase):
    maxDiff = None

    def test_translate(self):
        example = [seq for seq in SeqIO.parse(os.path.join(path_to_data, 'NC_009554.1_protein.fa'), format='fasta')]
        with tempfile.NamedTemporaryFile(mode='w', suffix='.fa') as outfile:
            infile = os.path.join(path_to_data, 'NC_009554.1_transcript.fa')
            cmd = '%s -i %s -o %s' % (path_to_script, infile, outfile.name)
            extern.run(cmd)
            records = [seq for seq in SeqIO.parse(outfile.name, format='fasta')]
            i = 0
            self.assertEqual(len(example), len(records))
            while i < len(records):
                self.assertEquals(example[i].seq, records[i].seq)
                self.assertEquals(example[i].description, records[i].description)
                i += 1

if __name__ == "__main__":
    unittest.main()
