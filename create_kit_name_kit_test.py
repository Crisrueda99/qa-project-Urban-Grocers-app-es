import pytest
from sender_stand_request import post_new_client_kit, get_new_user_token
from data import kit_body_1, kit_body_2, kit_body_3, kit_body_4, kit_body_5, kit_body_6, kit_body_7, kit_body_8, kit_body_9

def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

def test_1_allowed_characters_1():
    positive_assert(kit_body_1)

def test_2_allowed_characters_511():
    positive_assert(kit_body_2)

def test_3_less_than_allowed_0():
    negative_assert_code_400(kit_body_3)

def test_4_more_than_allowed_512():
    negative_assert_code_400(kit_body_4)

def test_5_special_characters():
    positive_assert(kit_body_5)

def test_6_spaces_allowed():
    positive_assert(kit_body_6)

def test_7_numbers_allowed():
    positive_assert(kit_body_7)

def test_8_parameter_not_passed():
    negative_assert_code_400(kit_body_8)

def test_9_wrong_type_number():
    negative_assert_code_400(kit_body_9)