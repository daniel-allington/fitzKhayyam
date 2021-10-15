import sys
import os
import os.path
import re
import numpy as np

rx_alpha = re.compile('[A-Za-z]')
rx_nonroman = re.compile('[^IVXLC]')
rx_digits = re.compile('\\d')

dest_folder = os.path.join('..', '_stanzas')

front_matter_template = '''---
layout: stanza
edition: {ed}
stanza: {st}
---
'''

if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

def process_file(fp, edition):
    l = open(fp, 'r').readlines()
    l = [s.strip() for s in l]
    l = [s for s in l if len(rx_alpha.findall(s)) > 0]
    stanza_number_lines = np.where([len(rx_nonroman.findall(s.strip('.')))==0 for s in l])[0]
    stanzas = [l[i+1:i+5] for i in stanza_number_lines]
    for n, stanza in enumerate(stanzas):
        with open(
                os.path.join(
                    dest_folder, 'ed-{ed}-stanza-{st}.md'.format(
                        ed = edition, st = n + 1)), 'w') as f:
            front_matter = front_matter_template.format(
                ed = edition, st = n + 1)
            body = rx_digits.sub('', '\n\n'.join(stanza))
            f.write('\n'.join([front_matter, body]))

if __name__ == '__main__':
    process_file(fp = sys.argv[1], edition = sys.argv[2])
