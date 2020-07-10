# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# class LatLon:
#     def __init__(self, lat=None, lon=None):
#         self.lat = lat or 42.331429
#         self.lon = lon or -83.045753

class LatLon:
    def __init__(self, lat=42.331429, lon=-83.045753):
        self.lat = lat or 42.331429
        self.lon = lon or -83.045753
    def __str__(self):
        return 'latitude ' + str(self.lat) + ', longitude ' + str(self.lon)

spokes = LatLon()
print(spokes)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class WayPoint(LatLon):
    def __init__(self, lat=42.331429, lon=-83.045753, name='Detroit'):
        super().__init__(lat, lon)
        self.name = name
    def __str__(self):
        return self.name + ' is located at ' + super().__str__()

spoke = WayPoint()
print(spoke)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(WayPoint):
    def __init__(
        self, lat=42.331429, lon=-83.045753, name='Detroit',
        difficulty='Day One issh', size='We out here'
    ):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size
    def __str__(self):
        return super().__str__() + '. Its geocache is ' + self.size + ' big, and ' + self.difficulty + ' to find.' 

dve = Geocache()
print(dve)



# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

asabovesobelow = WayPoint(41.70505, -121.51521, "Catacombs")
print(asabovesobelow)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
waypoint = WayPoint()
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache(44.052137, -121.41556, "Newberry Views", '1.5 liters of sweat hard', '2 millimeters')

# Print it--also make this print more nicely
print(geocache)