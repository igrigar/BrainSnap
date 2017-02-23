## This code was written by BrainSnap for #HashCode2017 ##

videos = []
endpoints = []
caches = []
c_size = 0

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
    e = Endpoint(1000, {2:100,0:200}, {1:3000, 0:200})
    c = Cache({3:50})
    print e.dc_latency
    print e.cache_latencies[2]
    print e.video_requests[0]
    print c.videos_size[3]

if __name__ == "__main__":
    main()
