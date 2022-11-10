import traceback
import sys

"""
try:
    n1 = float(input('Introduis un nombre: '))
    n2 = float(input('Introduis un nombre: '))
    print(n1/n2)
except Exception as e: 
    print(f'il y a une erreur - {e}')
    print(type(e))
    print(type(e).__name__)
    print(traceback.format_exc())

    exception_type, exception_object, exception_traceback = sys.exc_info()
    filename = exception_traceback.tb_frame.f_code.co_filename
    line = exception_traceback.tb_lineno

    print('fichier =>',filename )
    print('lingne de code =>', line)

print('on est apres la division')
"""


try:
    n1 = float(input('Introduis un nombre: '))
    n2 = float(input('Introduis un nombre: '))
    print(n1/n2)
except ValueError as e:
    print('Erreur de type =>', type(e).__name__,' | Introduisez un nombre')
except ZeroDivisionError as e:
    print('Erreur de type =>', type(e).__name__,' | Division par zero interdite, choisir une autre valeur')
except Exception as e:
    print('Erreur de type =>', type(e).__name__, ' Une erreur inattendue s est produite')
finally:
    print('Je suis le finally, je m execute si o si')

print('---  fin du traitement ----')