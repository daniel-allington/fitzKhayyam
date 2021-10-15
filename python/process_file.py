import sys
import re
import numpy as np

alpha = re.compile('[A-Za-z]')
nonroman = re.compile('[^IVXLC]')

def process_file(fp, version):
    l = open(fp, 'r').readlines()
    l = [s.strip() for s in l]
    l = [s for s in l if len(alpha.findall(s)) > 0]
    stanza_numbers = np.where([len(nonroman.findall(s.strip('.')))==0 for s in l])
    print(stanza_numbers[0])

if __name__ == '__main__':
    process_file(fp = sys.argv[1], version = sys.argv[2])
