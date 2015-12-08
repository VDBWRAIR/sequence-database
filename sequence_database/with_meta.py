import pandas as pd 
from toolz.itertoolz import mapcat, last
from toolz import compose
import re, os
import functools
from glob import glob
from Bio import SeqIO
read_by_extension = {'xlsx' : pd.read_excel, 'csv' : pd.read_csv, 
                     'tsv' : P(pd.read_csv, sep='\t')}
mdf = pd.read_excel('fastas/ppH1N1metadata.xlsx')
P = functools.partial
get_ext = lambda x: x.split('.')[-1]

def load_metadata(fn):
    return read_by_extension[get_ext(fn)](fn)

def load_fasta(fn):
    segment = fn2segment(fn)
    id_seq = lambda s: ('>' + s.id, segment, str(s.seq))
    return map(id_seq, SeqIO.parse(fn, format='fasta'))

fastas2df = compose(P(pd.DataFrame.set_index, keys='id'), P(pd.DataFrame, columns=('id', 'segment', 'seq')), list, P(mapcat, load_fasta) )
#fastas2df = compose(P(pd.DataFrame.set_index, keys='id'), P(pd.DataFrame, columns=('id', 'seq')), \
#        P(map, id_seq), P(mapcat, P(SeqIO.parse, format='fasta')))

segment_re = re.compile(r'(?:[^\.].((HA)|(NA)|(NS)|(PB1)|(PB2)|(MP)|(NP)|(PA)).*)') 
fn2segment = compose(lambda m: m.groups()[0], segment_re.match, os.path.basename)

fs = ['fastas/3.HAall.815seqsALGN.fas', 'fastas/3.MPall.815seqsALGN.fas', 'fastas/3.NAall.815seqsALGN.fas', 'fastas/3.NPall.815seqsALGN.fas', 'fastas/3.NSall.815seqsALGN.fas', 'fastas/3.PAall.815seqsALGN.fas', 'fastas/3.PB1all.815seqsALGN.fas', 'fastas/3.PB2all.815seqsALGN.fas']
expected = ['HA', 'MP', 'NA', 'NP', 'NS', 'PA', 'PB1', 'PB2']
assert expected == map(fn2segment, fs)

print '|'.join(map('({0})'.format, SEGMENTS))
sdf.tail()
alns = glob('fastas/*.fas')
sdf = fastas2df(alns)
#map(lambda x: x[-1], filter(lambda x: len(x) > 1, map(str.split, map(str, mdf.columns))))
SEGMENTS = ('HA', 'MP', 'NA', 'NP', 'NS', 'PA', 'PB1', 'PB2')
#sdf.loc['>A/Wisconsin/18/2011']
all_segments = lambda df, s: df.loc[s] 
fetch_segment(sdf, '>A/Wisconsin/18/2011', 'HA')
res = all_segments(sdf ,'>A/Wisconsin/18/2011' )
extract = lambda df: (df.index.values[0], df.seq.values[0])
to_fasta = compose('\n'.join, P(get_fields, fields=('id', 'seq')))
#TODO: figure out how to get index speed for id \
#        without having to describe id as an index \
#        so can access it normally like other fields.
def get_fields(df, fields):
    return [df[f].values[0] for f in fields]

assert len(res) == 8
def fetch_segment(df, id, segment):
    return df[ (df.index == id) & (df.segment == segment)]

#mdf[mdf.SequenceName.str.startswith('>A/Wisconsin')]
# assert there should be an entry for each segment in the sequence dataframe
xs = mapcat(open, glob('fastas/*.fas'))
ids = [s for i, s in enumerate(xs) if (i % 2 == 0)]
sdf[sdf.index.str.startswith('>A/Wisconsin')]
len(sdf[sdf.index.str.startswith('>A/Wisconsin')].segment.values)

