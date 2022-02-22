import pandas as pd
import numpy as np


def minuscule(dataset: pd.DataFrame) -> pd.DataFrame:
    r"""Modifie la casse des éléments du DataFrame en minuscule.

    Several sentences providing an extended description. Refer to
    variables using back-ticks, e.g. `var`.

    Parameters
    ----------
    dataset 
        Le DataFrame à modifier

    Returns
    -------
    dataset 
        Le DataFrame modifié

    Other Parameters
    ----------------
    only_seldom_used_keyword : int, optional
        Infrequently used parameters can be described under this optional
        section to prevent cluttering the Parameters section.
    **kwargs : dict
        Other infrequently used keyword arguments. Note that all keyword
        arguments appearing after the first parameter specified under the
        Other Parameters section, should also be described under this
        section.

    Raises
    ------
    BadException
        Because you shouldn't have done that.

    See Also
    --------
    numpy.array : Relationship (optional).

    Notes
    -----
    Notes about the implementation algorithm (if needed).

    This can have multiple paragraphs.

    You may include some math:

    .. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

    And even use a Greek symbol like :math:`\omega` inline.

    References
    ----------
    Cite the relevant literature, e.g. [1]_.  You may also cite these
    references in the notes section above.

    .. [1] O. McNoleg, "The integration of GIS, remote sensing,
       expert systems and adaptive co-kriging for environmental habitat
       modelling of the Highland Haggis using object-oriented, fuzzy-logic
       and neural-network techniques," Computers & Geosciences, vol. 22,
       pp. 585-588, 1996.

    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.

    >>> a = [1, 2, 3]
    >>> print([x + 3 for x in a])
    [4, 5, 6]
    >>> print("a\nb")
    a
    b
    """

    for column in dataset.columns:
        dataset[column] = dataset[column].astype(str).str.lower()

    return dataset

def conversionCoquille(dataset: pd.DataFrame) -> pd.DataFrame:
    r"""Modifie les valeurs du dataset qui sont proches des réponses.    

    Several sentences providing an extended description. Refer to
    variables using back-ticks, e.g. `var`.

    Parameters
    ----------
    dataset 
        Le DataFrame à modifier

    Returns
    -------
    dataset 
        Le DataFrame modifié

    Other Parameters
    ----------------
    only_seldom_used_keyword : int, optional
        Infrequently used parameters can be described under this optional
        section to prevent cluttering the Parameters section.
    **kwargs : dict
        Other infrequently used keyword arguments. Note that all keyword
        arguments appearing after the first parameter specified under the
        Other Parameters section, should also be described under this
        section.

    Raises
    ------
    BadException
        Because you shouldn't have done that.

    See Also
    --------
    numpy.array : Relationship (optional).

    Notes
    -----
    Notes about the implementation algorithm (if needed).

    This can have multiple paragraphs.

    You may include some math:

    .. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

    And even use a Greek symbol like :math:`\omega` inline.

    References
    ----------
    Cite the relevant literature, e.g. [1]_.  You may also cite these
    references in the notes section above.

    .. [1] O. McNoleg, "The integration of GIS, remote sensing,
       expert systems and adaptive co-kriging for environmental habitat
       modelling of the Highland Haggis using object-oriented, fuzzy-logic
       and neural-network techniques," Computers & Geosciences, vol. 22,
       pp. 585-588, 1996.

    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.

    >>> a = [1, 2, 3]
    >>> print([x + 3 for x in a])
    [4, 5, 6]
    >>> print("a\nb")
    a
    b
    """

    # On définit les valeurs qu'il est possible de remplacer avec des valeurs correctes
    listValA = ["(a)", "1"]
    listValB = ["(b)", "2"]
    listValC = ["(c)", "3"]
    listVal1 = ["(1)", "a", "1.0", "(a)"]
    listVal2 = ["(2)", "b", "2.0", "(b)"]
    listVal3 = ["(3)", "c", "3.0", "(c)"]

    # On différencie les colonnes en fonction des réponses attendues
    for column in dataset.columns:
        if column in ["Q1", "Q2", "Q3", "Q4"]:

            # On remplace les valeurs proches des réponses attendues (a, b ou c)
            dataset[column] = dataset[column].replace(
                to_replace=listValA, value="a")
            dataset[column] = dataset[column].replace(
                to_replace=listValB, value="b")
            dataset[column] = dataset[column].replace(
                to_replace=listValC, value="c")

            # On remplace les valeurs restantes par des NaN
            listValNan = dataset[column].unique()
            listValNan = [
                val for val in listValNan if val not in ("a", "b", "c")]
            dataset[column] = dataset[column].replace(listValNan, np.nan)

        else:

            # On remplace les valeurs proches des réponses attendues (1, 2 ou 3)
            dataset[column] = dataset[column].replace(
                to_replace=listVal1, value="1")
            dataset[column] = dataset[column].replace(
                to_replace=listVal2, value="2")
            dataset[column] = dataset[column].replace(
                to_replace=listVal3, value="3")

            # On remplace les valeurs restantes par des NaN
            listValNan = dataset[column].unique()
            listValNan = [
                val for val in listValNan if val not in ("1", "2", "3")]
            dataset[column] = dataset[column].replace(listValNan, np.nan)

    return dataset

if __name__ == "__main__":
    datasetCSV = pd.read_csv("Run_Questionnaire/DataSetTotal.csv")
    print(datasetCSV)
    datasetPretraite = minuscule(datasetCSV)
    datasetPretraite = conversionCoquille(datasetPretraite)

    # for column in datasetPretraite.columns:
    #     print(datasetPretraite[column].value_counts())
    #     print("---------------")

    print(datasetPretraite)
