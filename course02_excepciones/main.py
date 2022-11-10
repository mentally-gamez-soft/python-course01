import traceback
import sys

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