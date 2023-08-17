import pytest

import data
import functions


def test_create_booking_success_firstname():
    body = functions.change_booking_body()
    req = functions.create_booking(body).status_code
    exp = 200

    assert req == exp


@pytest.mark.parametrize("totalprice",
                         [
                             pytest.param(9999999999, id="1_BigNumbers"
                                          ),
                             pytest.param(1, id="2_SmallNumbers"
                                          ),
                             pytest.param(0, id="3_ZeroNumbers"
                                          ),
                             pytest.param(34.565, id="4_FloatNumbers"
                                          )
                         ])
def test_create_booking_success_totalprice(totalprice):
    body = functions.change_booking_body("totalprice", totalprice)
    req = functions.create_booking(body).status_code
    exp = 200

    assert req == exp


def test_delete_booking_success():
    id = functions.create_booking(data.booking_body).json()["bookingid"]
    req = functions.delete_booking(id).status_code
    exp = 201
    assert req == exp
