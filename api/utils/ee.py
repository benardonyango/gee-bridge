from ee import (
    ImageCollection,
    FeatureCollection,
    Image,
    Filter,
    Geometry,
    DateRange,
    EEException
)
from ee.data import getInfo, ASSET_TYPE_FOLDER, ASSET_TYPE_IMAGE_COLL
from rest_framework.serializers import ValidationError


class EEUtil:
    """Exploit earth engine utilities

    Parameters
    ----------
        collection: string
            Collection asset id
    """

    def __init__(self, collection):
        self.collection = collection
        self.__reduced = None

    @property
    def instance(self):
        """Create EE instance from a defined asset id"""
        try:
            if isinstance(self.collection, str):
                ee_asset = ImageCollection(self.collection)
                return ee_asset
        except EEException as e:
            raise ValidationError("Input dataset is not valid")

    @property
    def type(self):
        """Identify the type of the instance"""

        asset_types = {
            ASSET_TYPE_IMAGE_COLL: ImageCollection,
            'FeatureCollection': FeatureCollection,
            'Image': Image,
            ASSET_TYPE_FOLDER: None
        }

        try:
            for getInfo(self.collection)["type"] in asset_types.keys():
                return asset_types.get(getInfo(self.collection)["type"])
        except KeyError as e:
            raise

    @property
    def reduced(self):
        """EE reduced instance from asset id and filters"""
        return self.__reduced

    # setters
    @reduced.setter
    def reduced(self, value):
        """Sets new value for attribute reduced

        Parameters
        ----------
        value : string
            Assign new reduced to instance

        """
        self.__name = value

    def filterDateRange(self, filter=None):
        """Filter by period of time

        Parameters
        ----------
        filter : ee.Filter, optional
            Filter instance of DateRange object
            (the default is None, which doesn't filter)

        Example
        -------
        >>c = EEUtil('projects/fao-wapor/L1/L1_AETI_D')
        >>range = DateRange("2017-01-01", "2018-01-01")
        >>f = ee.Filter(range)
        >>c.filterDateRange(filter=f)

        """

        try:
            if filter and isinstance(filter, Filter):
                try:
                    if not self.reduced:
                        redux = self.instance.filterDate(filter).sort(
                            'system:time_start', True
                        )
                    else:
                        redux = self.reduced.filterDate(filter).sort(
                            'system:time_start', True
                        )
                    self.__reduced = redux
                except EEException as e:
                    raise ValidationError("Input dataset or toi is not valid")
        except ValueError as e:
            raise

    def filterGeometry(self, filter=None):
        """Filter by geometry

        Parameters
        ----------
        filter : ee.Geometry, optional
            Geometry object to filter collection's footprint
            (the default is None, which doesn't filter)

        Example
        -------
        >>c = EEUtil('projects/fao-wapor/L1/L1_AETI_D')
        >>geojson = {
            "type": "Polygon",
            "coordinates": [
                [
                    [100, 0], [101, 0],
                    [101, 1], [100, 1],
                    [100, 0]
                ]
            ]
        }
        >>geom = Geometry()
        >>c.filterGeometry(filter=geom)

        """

        try:
            if filter and isinstance(filter, Geometry):
                try:
                    if not self.reduced:
                        redux = self.instance.filterBounds(filter).sort(
                            'system:time_start', True)
                    else:
                        redux = self.reduced.filterBounds(filter).sort(
                            'system:time_start', True)
                    self.__reduced = redux
                except EEException as e:
                    raise ValidationError("Input dataset or aoi is not valid")
        except ValueError as e:
            raise

    def is_reduced_empty(self):
        """Return if the reduced instance collection is empty

        Returns
        -------
        bool
            True/False if the filtered collection is empty
        """

        if self.reduced:
            try:
                if self.info(reduced=True)["features"]:
                    return False
                else:
                    return True
            except EEException as e:
                raise
        else:
            raise ValueError(
                "Calling function while the reduced doesn't exist"
            )

    def info(self, reduced=False):
        """Wrap earth engine getInfo operation

        Parameters
        ----------
        reduced : bool, optional
            Evaluate original or reduced instance
            (the default is False, which gives information of original asset)

        Returns
        -------
        dict
            All information of the asset collection

        """

        try:
            if reduced:
                try:
                    return self.reduced.getInfo()
                except AttributeError as e:
                    raise ValueError("Reduced instance collection doesn't exist yet")
            return self.instance.getInfo()
        except EEException as e:
            raise
