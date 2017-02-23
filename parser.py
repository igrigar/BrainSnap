import sys
import os

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


def parser(filename):

    with open (filename, 'r') as file1:

        global c_size
        global v_size
        global endpoints

        vid, endp, req, cachenum, c_size = file1.readline().strip().split(' ')
        vid, endp, req, cachenum, c_size = [int(vid),int(endp), int(req), int(cachenum), int(c_size)]
        #Here we fill the array of videos sizes and indexes
        v_sizes = [int(c_temp) for c_temp in file1.readline().strip().split(' ')]

        for i in range(0, endp):
            c = [int(i) for i in file1.readline().strip().split(' ')]
            dic = {}
            for y in range(0, c[1]):
                ca = [int(i) for i in file1.readline().strip().split(' ')]
                dic[ca[0]] = ca[1]
            e = Endpoint(c[0], dic)
            endpoints.append(e)


        for i in range(0, req):

            c = [int(i) for i in file1.readline().strip().split(' ')]
            endpoints[c[1]].video_requests[c[0]] = c[2]
def main():

    parser("./prueba.in")
    for i in range(0, len(endpoints)):
        print endpoints[i].dc_latency
        print endpoints[i].video_requests
    print v_sizes
    print c_size


if __name__ == "__main__":
    main()
