import pandas
import numpy as np
import math

# our kitchen on Lake and Racine Ave (41.8851024,-87.6618988)
class KioskMap(object):
    def __init__(self, csv=None):
        if csv != None:
            self.addr, self.depot, self.depot_coords = self._read_csv(csv)
        else:
            self.depot_coords, self.depot ,self.addr = None

    def _read_csv(self, csv):
        df = pandas.read_csv(csv)
        df = df.drop_duplicates()

        df.loc[-1] = ["Farmers Fridge","Lake and Racine Ave","41.8851024","-87.6618988"]
        df.index = df.index + 1

        df = df.sort_index()
        home_loc = df.loc[0]
        home_coords = (home_loc['latitude (N)'], home_loc['longitude (N)'])
        import ipdb; ipdb.set_trace()
        return df, home_loc, home_coords

    def some_compute(self):
        coordinate_to = (self.addr['latitude (N)'], self.addr['longitude (N)'])
        import ipdb; ipdb.set_trace()

        self.addr['distance'] = self.coordiate_dist(self.depot_coords, coordinate_to)
        import ipdb; ipdb.set_trace()

    def coordiate_dist(self, coord1, coord2):
        lat1, long1 = coord1
        lat2, long2 = coord2

        earth_radius_km = 6371
        import ipdb; ipdb.set_trace()
        r_lat1 = np.radians(lat1)
        r_lat2 = np.radians(lat2)
        r_long1 = np.radians(long1)
        r_long2 = np.radians(long2)

        return arc * 6371
