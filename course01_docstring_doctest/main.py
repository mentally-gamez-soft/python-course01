"""" Voici le DocString du module main """

def checkAlien(colorSangre:str, sangreVenenosa:bool):
    """" To know if a life being is an alien through its blood type
    Args:
        colorSangre: string
        sangreVenenosa: bool
    Returns:
        bool
    """
    colorSangre = colorSangre.lower()
    if colorSangre != 'rojo' and sangreVenenosa == True:
        return True

    return False

def checkAlien2(colorSangre:str, sangreVenenosa:bool):
    """_summary_

    Args:
        colorSangre (str): _description_
        sangreVenenosa (bool): _description_
    """

    pass

# Test with doctest
# Execute in shell python -m doctest .\01_docstring_doctest\main.py -v
def checkAlien3(colorSangre:str, sangreVenenosa:bool):
    """_summary_

    Args:
        colorSangre (str): string for the color of the blood
        sangreVenenosa (bool): True if venom, False else

    Examples:

    >>> checkAlien3("verde", True)
    True

    >>> checkAlien3("rojo", True)
    False
    """
    colorSangre = colorSangre.lower()
    if colorSangre != 'rojo' and sangreVenenosa == True:
        return True

    return False

def sayHello(name:str) -> str:
    """ Bot qui dit bonjour

    Args:
        name (str): Nom de l utilisateur

    Returns:
        str: phrase de bienvenue

    Examples:
    
    >>> sayHello('krys')
    'Bonjour krys. Je suis autobot ton nouvel ami.'
    """
    return f'Bonjour {name}. Je suis autobot ton nouvel ami.'

if __name__ == '__main__':
    print("point de depart")
    result =  checkAlien(colorSangre="VERDE", sangreVenenosa=True)
    print(result)
    print(checkAlien.__doc__)
    print(checkAlien.__name__)
    print(checkAlien)
    print(sayHello('krys'))