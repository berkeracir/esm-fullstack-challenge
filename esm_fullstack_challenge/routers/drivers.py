from typing import List, Dict
import logging

from fastapi import APIRouter, HTTPException, status

from esm_fullstack_challenge.controllers.driver import (
    update_driver as db_update_driver,
    create_driver as db_create_driver,
    delete_driver as db_delete_driver,
)
from esm_fullstack_challenge.models import AutoGenModels
from esm_fullstack_challenge.models.driver import DriverUpdateDTO, DriverCreateDTO
from esm_fullstack_challenge.routers.utils import get_route_list_function, get_route_id_function


logger = logging.getLogger('routers/drivers.py')

drivers_router = APIRouter()

table_model = AutoGenModels['drivers']

# Route to get driver by id
get_driver = get_route_id_function('drivers', table_model)
drivers_router.add_api_route(
    '/{id}', get_driver,
    methods=["GET"], response_model=table_model,
)

# Route to get a list of drivers
get_drivers = get_route_list_function('drivers', table_model)
drivers_router.add_api_route(
    '', get_drivers,
    methods=["GET"], response_model=List[table_model],
)


# Add route to create a new driver
@drivers_router.post('', response_model=table_model)
def create_driver(create_dto: DriverCreateDTO):
    """
    Create a new driver.
    """
    new_id = db_create_driver(create_dto)
    if new_id is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Driver could not be created.'
        )

    return table_model(id=new_id, **(create_dto.model_dump()))


# Add route to update driver
@drivers_router.put('/{id}', response_model=table_model)
def update_driver(id: int, update_dto: DriverUpdateDTO):
    """
    Update driver.
    """
    success = db_update_driver(id, update_dto)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Driver with id={id} does not exist!'
        )

    return table_model(id=id, **(update_dto.model_dump()))


# Add route to delete driver
@drivers_router.delete('/{id}', response_model=Dict[str, int])
def delete_driver(id: int):
    """
    Delete driver.
    """
    # NOTE: Status Code 204 could be used without response body
    success = db_delete_driver(id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Driver with id={id} does not exist!'
        )

    return {'id': id}
