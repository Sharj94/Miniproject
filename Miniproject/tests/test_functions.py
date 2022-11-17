from unittest import mock

import pytest

from product import add_product


@pytest.fixture
def product_list_with_no_products():
    return []


def test_product_addition(product_list_with_no_products):
    # set up
    mock_product = "Apple"
    mock_price = "5000"

    expected_outcome = [{"Product": "Apple", "Price": 5000.0}]

    # act
    mock_args = [mock_product, mock_price]
    with mock.patch("builtins.input") as mock_input:
        mock_input.side_effect = mock_args
        assert product_list_with_no_products == []
        add_product(product_list_with_no_products)
        assert product_list_with_no_products == expected_outcome