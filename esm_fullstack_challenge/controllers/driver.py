import logging
from textwrap import dedent
from typing import Optional

from esm_fullstack_challenge.dependencies import get_db, get_next_id
from esm_fullstack_challenge.models import AutoGenModels
from esm_fullstack_challenge.models.driver import DriverDTO, DriverUpdateDTO, DriverCreateDTO
from esm_fullstack_challenge.routers.utils import get_route_id_function


logger = logging.getLogger("controllers/driver.py")


DRIVER_TABLE = "drivers"
TABLE_MODEL = AutoGenModels[DRIVER_TABLE]

_get_driver_from_db = get_route_id_function('drivers', TABLE_MODEL)


def get_driver(id: int) -> DriverDTO:
    """
    Gets the driver with given id.
    """
    driver = _get_driver_from_db(id)
    return DriverDTO(**driver)


def create_driver(create_dto: DriverCreateDTO) -> Optional[int]:
    """
    Creates a new driver.
    """
    next_driver_id = get_next_id(DRIVER_TABLE)

    model_dump = create_dto.model_dump()

    keys = [field for field in model_dump.keys()]
    values = [model_dump[key] for key in keys]

    keys = ["id"] + keys
    values = [next_driver_id] + values
    fields = ','.join(f'`{key}`' for key in keys)
    values_placeholder = ','.join(['?'] * len(keys))

    query = dedent(
        f'''
            INSERT INTO `{DRIVER_TABLE}`({fields})
                VALUES({values_placeholder})
        '''
    ).strip()

    db = next(get_db())
    with db.get_connection() as conn:
        cur = conn.cursor()
        cur.execute(query, values)
        conn.commit()

    return values[0]


def update_driver(id: int, update_dto: DriverUpdateDTO) -> bool:
    """
    Updates the driver with given id.
    """
    # TODO: think about atomicity
    model_dump = update_dto.model_dump()
    fields = ', '.join([f'`{field}` = :{field}' for field in model_dump.keys()])

    query = dedent(
        f'''
            UPDATE `{DRIVER_TABLE}`
            SET {fields}
            WHERE `id` = :id
        '''
    ).strip()
    parameters = {'id': id, **model_dump}

    db = next(get_db())
    with db.get_connection() as conn:
        cur = conn.cursor()
        cur.execute(query, parameters)
        conn.commit()
        row_count = cur.rowcount

    return row_count == 1


def delete_driver(id: int) -> bool:
    """
    Deletes the driver with given id.
    """
    query = dedent(
        f'''
            DELETE FROM `{DRIVER_TABLE}`
            WHERE `id` = :id
        '''
    ).strip()
    parameters = {'id': id}

    db = next(get_db())
    with db.get_connection() as conn:
        cur = conn.cursor()
        cur.execute(query, parameters)
        conn.commit()
        row_count = cur.rowcount

    return row_count == 1
