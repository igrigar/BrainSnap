#!/usr/bin/env python
# -*- coding: utf8 -*-

videos = [50, 50, 80, 30, 110]
endpoints = []
caches = []
c_size = 100

class Endpoint(object):
    """docstring for Endpoint."""
    def __init__(self, dc, cache, requests):
        super(Endpoint, self).__init__()
        self.dc_latency = dc
        self.cache_latencies = cache
        self.video_requests = requests

class Cache(object):
    """docstring for Cache."""
    def __init__(self, v):
        super(Cache, self).__init__()
        self.videos_size = v

def main():
    endpoints.append(Endpoint(1000, {0:1000, 1:200, 2:300}, {3:1500, 4:500, 1:1000}))
    endpoints.append(Endpoint(500, {}, {0:1000}))

    # Get least latency cache.
    key = 0
    cache = 5001
    for ep in endpoints:
        tmp = ep.cache_latencies
        if not tmp:
            continue
        tmp_k = min(tmp, key=tmp.get)
        if tmp[tmp_k] < cache:
            key = tmp_k
            cache = tmp[tmp_k]
        #print min(ep.cache_latencies, key=ep.cache_latencies.get)

    print key, cache


if __name__ == "__main__":
    main()
