import sys
import os
## This code was written by BrainSnap for #HashCode2017 ##


## This code was written by BrainSnap for #HashCode2017 ##

v_sizes = []
endpoints = []
caches = []
c_size = 0

class Endpoint(object):
    """docstring for Endpoint."""
    def __init__(self, dc, cache):
        super(Endpoint, self).__init__()
        self.dc_latency = dc
        self.cache_latencies = cache
        self.video_requests = {}

    def set_video(self, videos):
        self.video_requests = videos

    def pondera(cache):

        return

class Cache(object):
    """docstring for Cache."""
    def __init__(self, v):
        super(Cache, self).__init__()
        self.videos_size = v

def main():
    pass

if __name__ == "__main__":
    main()

def parser(filename):

    with open (filename, 'r') as file1:

        vid, endp, req, cachenum, cachsize = file1.readline().strip().split(' ')
        vid, endp, req, cachenum, cachsize = [int(vid),int(endp), int(req), int(cachenum), int(cachsize)]
        #Here we fill the array of videos sizes and indexes
        videos = [int(c_temp) for c_temp in file1.readline().strip().split(' ')]

        for x in endp:
            c = [int(i) for i in file1.readline().strip().split(' ')]
            dic = {}
            for y in c[1]:
                ca = [int(i) for i in file1.readline().strip().split(' ')]
                dic[ca[0]] = ca[1]
            e = Endpoint(c[0], dic)
            endpoints.append(e)

        for x in req:
            c = [int(i) for i in file1.readline().strip().split(' ')]
            endpoints[c[1]].video_requests[c[0]] = c[3]
