class VesselValues:
    types: str = "Feature"
    geometry_type: str = "Point"
    latitude: float = 51.31948720361112
    longitude: float = 4.273654881388889
    sogKph: float = 13.78
    headingTrueDegrees: float = 7.61
    epochSeconds: float = 1652081541.9124634

    latest_value_tercofin = {"type": types,
                             "geometry": geometry_type,
                             "latitude": latitude,
                             "longitude": longitude,
                             "sogkph": sogKph,
                             "headingTrueDegrees": headingTrueDegrees,
                             "epochSeconds": epochSeconds}
    _instance = None
    number: int

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(VesselValues, cls).__new__(cls)
        return cls._instance
