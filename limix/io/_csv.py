def read_csv(filename, sep=' ', header=True):
    r"""Read a CSV file.

    Parameters
    ----------
    filename : str
        Path to a CSV file.

    Returns
    -------
    data : dask dataframe

    Examples
    --------
    .. doctest::

        >>> from limix.io import read_csv
        >>> from limix.io.examples import csv_file_example
        >>>
        >>> df = read_csv(csv_file_example())
        >>> print(df.compute()) #doctest: +NORMALIZE_WHITESPACE
           pheno   attr1 attr2 attr3
        0    sex  string    10     a
        1   size   float    -3     b
        2  force     int     f     c
    """
    from dask.dataframe import read_csv as _read_csv

    header = 0 if header else None
    return _read_csv(filename, sep=sep, header=header)


def see(filepath):
    """Shows a human-friendly representation of a CSV file.

    Parameters
    ----------
    filepath : str
        CSV file path.

    Returns
    -------
    str
        CSV representation.
    """
    from pandas import read_csv
    print(read_csv(filepath).head())
