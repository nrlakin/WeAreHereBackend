

class KNNClassifier():

    # Default beacon in case of error.
    ERROR_ID = 99

    def __init__(self, k = 1):
        self.k = k
        self.room_id_map =  {"30201:10": 17,
                             "30205:1" : 2,
                             "30299:2" : 14,
                             "30204:1" : 12,
                             "30207:1" : 9,
                             "30206:1" : 10,
                             "30203:2" : 13,
                             "30200:4" : 14,
                             "65535:1" : 2}

    def get_room(self, ranges):
        """
        Return room, given list of beacon ranges in format
            {"beacon_id": id_string, "rssi": number}
        Currently more elaborate than it needs to be; there will never be more
        than one beacon in a room by current setup. Made to adjust later in case
        we have more than one beacon per region; then, we will split on major
        id # (left of colon).  Will never have more than one vote per room
        with current setup.
        Needs some tweaking to fully implement k > 1.
        """
        print "DEBUG"
        print ranges
        print type(ranges[0]['beacon_id'])
        print type(ranges[0]['rssi'])
        by_strength = sorted(ranges, key = (lambda beacon: beacon['rssi']))
        k_nearest = [beacon['beacon_id'] for beacon in by_strength][-self.k:]
        uniques = set(k_nearest)
        votes = {beacon:0 for beacon in uniques}
        for beacon in k_nearest:
            votes[beacon] += 1
        winner = max(votes.iterkeys(), key = (lambda beacon: votes[beacon]))
        try:
            print 'locaton: ' + str(self.room_id_map[winner])
            return self.room_id_map[winner]
        except KeyError:
            print 'error, got ' + winner
            # winning beacon not in map...
            return self.ERROR_ID

if __name__ == '__main__':
    sample_ranges = [
        {"beacon_id":"30200:4", "rssi":-1000},
        {"beacon_id":"30203:2", "rssi":-1000},
        {"beacon_id":"30204:1", "rssi":-68},
        {"beacon_id":"30205:1", "rssi":-77},
        {"beacon_id":"30206:1", "rssi":-91},
        {"beacon_id":"30207:1", "rssi":-93}
    ]
    knn = KNNClassifier(k = 1)
    print 'Room = ' + str(knn.get_room(sample_ranges))
