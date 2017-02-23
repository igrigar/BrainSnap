#!/usr/bin/env python
# -*- coding: utf8 -*-

videos = [50, 50, 80, 30, 110]
endpoints = []
caches = []
c_size = 100

class Endpoint(object):
    """docstring for Endpoint."""
    def __init__(self, dc, cache):
        super(Endpoint, self).__init__()
        self.dc_latency = dc
        self.cache_latencies = cache
        self.video_requests = {}

    def set_video(self, videos):
        self.video_requests = videos

    def pondera(self, cache):
        # Pondera cada video usando las latencias de cada cache y las requests de los videos para el endpoint #
        dictionary = {}
        for video in self.video_requests:
            dictionary[video] = float(self.video_requests[video])/float(self.cache_latencies[cache])
        return dictionary

class Cache(object):
    """docstring for Cache."""
    def __init__(self, v):
        super(Cache, self).__init__()
        self.videos_size = v

def main():
    endpoints.append(Endpoint(1000, {0:1000, 1:200, 2:300}))
    endpoints[0].set_video({3:1500, 4:500, 1:1000})
    endpoints.append(Endpoint(500, {1:100}))
    endpoints[1].set_video({0:1000, 4:500})

    # Get least latency cache.
    key = 0
    cache = 999999999
    for ep in endpoints:
        tmp = ep.cache_latencies
        if not tmp:
            continue
        tmp_k = min(tmp, key=tmp.get)
        if tmp[tmp_k] < cache:
            key = tmp_k
            cache = tmp[tmp_k]
        #print min(ep.cache_latencies, key=ep.cache_latencies.get)
    rl_pond = {}

    for ep in endpoints:
        if key in ep.cache_latencies:
            tmp = ep.pondera(key)
            for k in tmp:
                if k in rl_pond:
                    rl_pond[k] += tmp[k]
                else:
                    rl_pond[k] = tmp[k]

    print rl_pond

if __name__ == "__main__":
    main()
