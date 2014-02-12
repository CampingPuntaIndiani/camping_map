#!/usr/bin/python

import json
import itertools

def generate(data, w, h):
    """ generate html map
        @param data: loaded json
        @param dim: image map dimension
    """
    def normalize(l):
        return list(itertools.chain.from_iterable([[int(l[i]*w/100), int(l[i+1]*h/100)] for i in xrange(0, len(l)-1, 2)]))

    return '\n'.join(['<area shape="poly" coords="{}" alt="{}" data-place_name="{}" />'.format(
        ",".join(map(lambda x: str(x), normalize(shape['points']))),
        shape['name'],
        shape['name']) for shape in data])



if __name__ == '__main__':
    width = 1278
    height = 1578

    data = None
    with open('json_map.json', 'r') as j:
        data = json.load(j)
    html = '<img src="source_map.jpg" width={}, height={} usemap="#map">'.format(width, height)
    html += '<map id="map" name="map">{}</map>'.format(generate(data, width, height))
    with open('gen_map_{}x{}.html'.format(width, height), 'w+') as h:
        h.write(html)


