#controller
# maintain two pieces of state
# items in buffer and number of items in the ready pool
# call work function at each timestep
class Buffer:
    def __init__(self, max_wip, max_flow):
        self.queued = 0
        self.wip = 0 #ready pool

        self.max_wip = max_wip
        self.max_flow = max_flow # average outflow

    def work(self, u) :
        #add to ready pool
        u = max(0, int(round(u)))
        u = min(u, self.max_wip)

        # transfer from ready to queue
        r = int(round(random.uniform(0, self.wip)))
        self.wip -= r
        self.queued += r

        # release from Queue
        r = int((round(random.uniform(0, self.maxflow))))
        r = min((r, self.queued))
        self.queued -= r

        return self.queued

