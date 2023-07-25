import allure
import pytest

from source.api.payments.payments import delete_service, create_service
from source.base.validator import (assert_status_code, assert_json_equal_json, assert_json_by_model)
from source.schemas.payments.external_payments_services_schema import External_Payments
from source.enums.expected import ExpectedJSON


@allure.epic('Payments')
@allure.feature('External Payments')
@allure.story('Services')
@allure.suite('Test delete services')
@pytest.mark.smoke
class TestPaymentsGetList:

    @allure.title('Test of deleting non-existent service by id')
    @allure.description('Проверка ответа [404] при удалении по id несуществующего сервиса оплаты')
    def test_external_payments_services_id_negative_remove_non_existent_service_delete(self):
        payload = {
            "name": "UNIQ"
        }

        response_1 = create_service(json=payload)
        id_test = response_1.json().get("id")
        assert_json_by_model(response=response_1, model=External_Payments)

        response_2 = delete_service(id_data=id_test)
        assert_status_code(response=response_2, expected=204)

        response_3 = delete_service(id_data=id_test)
        expected_2 = ExpectedJSON.PAYMENT_SERVICE_NOT_FOUND.value
        assert_json_equal_json(response=response_3, json=expected_2)
        assert_status_code(response=response_3, expected=404)

    @allure.title('Test of successful deleting existent service by id')
    @allure.description('Проверка успешного ответа [204] при удалении по id существующего сервиса оплаты')
    def test_external_payments_services_id_positive_delete(self):
        payload = {
            "name": "UNIQ"
        }

        response_1 = create_service(json=payload)
        id_test = response_1.json().get("id")
        assert_json_by_model(response=response_1, model=External_Payments)

        response_2 = delete_service(id_data=id_test)
        assert_status_code(response=response_2, expected=204)
