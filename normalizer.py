#!/urs/bin/python

import re
import json

def build():
    serialize(parse())

def parse():
    elements = []
    with open('source_map.html') as f:
        for line in f:
            if line.find('coords') is not -1:
                l = line.split('"')
                ps = l[3].strip(',').split(',')
                pc = []
                for i in xrange(0, len(l)-1, 2):
                    pc.extend(normalize(ps[i], ps[i+1]))
                elements.append({
                    'name':l[5],
                    'points':pc
                })
    return elements

def normalize(x, y):
    return [100.0*int(x)/WIDTH, 100.0*int(y)/HEIGHT]

def serialize(o):
    with open('json_map.json', 'w+') as f:
        json.dump(o, f)





WIDTH = 1278
HEIGHT = 1578
if __name__ == '__main__':
    build()
