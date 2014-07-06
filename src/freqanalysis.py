#!/usr/bin/python

from collections import Counter
from itertools import izip_longest

FREQLETS = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']
FREQNUMS = ['12.702%', '9.056%', '8.167%', '7.507%', '6.966%', '6.749%', '6.327%', '6.094%', '5.987%', '4.253%', '4.025%', '2.782%', '2.758%', '2.406%', '2.360%', '2.228%', '2.015%', '1.974%', '1.929%', '1.492%', '0.978%', '0.772%', '0.153%', '0.150%', '0.095%', '0.074%']

inputstring = raw_input("Input some text: ")

counter = Counter(inputstring)

letters = counter.most_common()

uniques, counts = map(list, zip(*letters))
percents = [str(round((counts[x]/float(len(inputstring)) * 100), 3)) + "%" for x in range(len(counts))]

print '\nTotal characters:', len(inputstring), '\n'
print 'Character   Count   Percentage        Letter   Relative Frequency'
print '==============================        ==========================='

for a, b, c, d, e in izip_longest(uniques, counts, percents, FREQLETS, FREQNUMS, fillvalue=""):
    print "{0:>5}{1:>10}{2:>13}{3:>14}{4:>18}".format(a, b, c, d, e)