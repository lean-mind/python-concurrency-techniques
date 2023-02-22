import time
import logging
from concurrent.futures import Future

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def callback(future):
    logging.info('Hola, soy un callback que se ejecuta hasta que el Futuro posea un valor!')
    logging.info(f'El valor del futuro es: {future.result()}')


if __name__ == '__main__':
    future = Future()

    logging.info('>> Futuro creado. No posee valor alguno.')

    future.add_done_callback(callback)

    logging.info('>>> Establecemos una acción a ejecutar una vez el Futuro posee valor alguno.')

    time.sleep(2)

    future.set_result('CódigoFacilito')

    logging.info('>>> Después de 2 segundos se asigna un valor al Futuro.')
