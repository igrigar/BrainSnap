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
    e = Endpoint(1000, {0:200, 1:300})
    e.video_requests[0] = 1000
    e.video_requests[1] = 2000
    print e.pondera(1)


if __name__ == "__main__":
    main()
