import pandas as pd
from OSMPythonTools.nominatim import Nominatim

def get_geolocation_mapping(query=None):
    """
    Returns a list of dicts with 'lat' and 'lon' as keys

    Parameters
    ----------
    query : str
        The name of entity to be mapped (default is None)

    Raises
    ------
    ValueError
    If no queries or an empty query has been passed in as a parameter
    """

    if query is None or not query:
        raise ValueError("Query must not be empty!")

    unneeded_classes = ['highway', 'place', 'tourism', 'boundary', 'railway', 'aeroway']
    unneeded_types = ['parking', 'yes', 'brownfield']

    nominatim = Nominatim()
    result = nominatim.query(query).toJSON()
    df = pd.DataFrame.from_records(result)

    df = df[df['class'].isin(unneeded_classes) == False]
    df = df[df['type'].isin(unneeded_types) == False]
    df = df.filter(items=['lat', 'lon'])

    return df.to_dict('records')