import unittest
from sequence_database import sequence_database

class Test(unittest.TestCase):
    def test_fn2segment(self): 
        fs = ['fastas/3.HAall.815seqsALGN.fas', 'fastas/3.MPall.815seqsALGN.fas', 'fastas/3.NAall.815seqsALGN.fas', 'fastas/3.NPall.815seqsALGN.fas', 'fastas/3.NSall.815seqsALGN.fas', 'fastas/3.PAall.815seqsALGN.fas', 'fastas/3.PB1all.815seqsALGN.fas', 'fastas/3.PB2all.815seqsALGN.fas']
        expected = ['HA', 'MP', 'NA', 'NP', 'NS', 'PA', 'PB1', 'PB2']
        self.assertEquals(expected, map(sequence_database.fn2segment, fs))


    def test_sampling(self):
        alns = glob('fastas/*.fas')
        sdf = fastas2df(alns)


'''
some only have year without month/day

Sampling Year,SamplingDate
int,MM/DD/YY|YYYY/MM/DD[_x] -> ignore _x
  
SamplingDate is  Collection Date in fludb.

some malformed entries in the excel spreadsheet
'''
# try running plot_muts on new data
# swap distance function in k-means implementation and use on 
# Melanie's Variant Pop./haplotype data


