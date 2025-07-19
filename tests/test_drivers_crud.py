#!/usr/bin/env python
'''Tests for `esm_fullstack_challenge` package.'''
import pytest
from fastapi import status
from fastapi.testclient import TestClient
from typing import Optional

from esm_fullstack_challenge.main import app
from esm_fullstack_challenge.models.driver import DriverBaseDTO, DriverDTO


@pytest.fixture
def test_client():
    with TestClient(app) as client:
        yield client


def test_get_non_existing_driver(test_client):
    # get non-existing driver
    get_response = test_client.get('/drivers/-1')
    assert get_response.status_code == status.HTTP_404_NOT_FOUND


def test_create_driver(test_client, driver_base: Optional[DriverBaseDTO] = None) -> DriverDTO:
    if driver_base is None:
        driver_base = DriverBaseDTO(
            driver_ref='berker',
            number='5',
            code='BRKR',
            forename='Berker',
            surname='Acir',
            dob='1996-09-17',
            nationality='Turkish',
            url='https://www.linkedin.com/in/berkeracir/'
        )

    # create driver
    post_response = test_client.post('/drivers', json=driver_base.model_dump())
    assert post_response.status_code == status.HTTP_200_OK
    driver = DriverDTO(id=post_response.json()['id'], **(driver_base.model_dump()))

    # validate create response body
    post_response_body = post_response.json()
    for key, value in driver.model_dump().items():
        assert post_response_body[key] == value

    # validate get response body
    get_response = test_client.get(f'/drivers/{driver.id}')
    assert get_response.status_code == status.HTTP_200_OK
    get_response_body = get_response.json()
    for key, value in driver_base.model_dump().items():
        assert get_response_body[key] == str(value)

    return driver


def test_update_non_existing_driver(test_client):
    driver_base = DriverBaseDTO(
        driver_ref='berker',
        number='5',
        code='BRKR',
        forename='Berker',
        surname='Acir',
        dob='1996-09-17',
        nationality='Turkish',
        url='https://www.linkedin.com/in/berkeracir/'
    )
    # update non-existing driver
    put_response = test_client.put('/drivers/-1', json=driver_base.model_dump())
    assert put_response.status_code == status.HTTP_404_NOT_FOUND


def test_update_driver(test_client):
    driver = test_create_driver(test_client)
    updated_driver = driver.model_dump()
    for key, value in updated_driver.items():
        # TODO: better value update
        if key == 'id':
            continue
        updated_driver[key] = str(reversed(value))

    # update the driver
    put_response = test_client.put(f'/drivers/{driver.id}', json=updated_driver)
    assert put_response.status_code == status.HTTP_200_OK

    # validate updated response body
    put_response_body = put_response.json()
    for key, value in updated_driver.items():
        assert put_response_body[key] == value

    # validate get response body
    get_response = test_client.get(f'/drivers/{driver.id}')
    assert get_response.status_code == status.HTTP_200_OK
    get_response_body = get_response.json()
    for key, value in updated_driver.items():
        assert get_response_body[key] == value


def test_delete_non_existing_driver(test_client):
    # delete non-existing driver
    get_response = test_client.get('/drivers/-1')
    assert get_response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_driver(test_client):
    driver = test_create_driver(test_client)

    # delete the driver
    delete_response = test_client.delete(f'/drivers/{driver.id}')
    assert delete_response.status_code == status.HTTP_200_OK

    # try fetching the deleted driver
    get_response = test_client.get(f'/drivers/{driver.id}')
    assert get_response.status_code == status.HTTP_404_NOT_FOUND
