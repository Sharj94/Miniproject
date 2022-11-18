from unittest import mock

import pytest

from product import enumerate_product, add_product, update_product, delete_product


@pytest.fixture
def product_list_with_no_products():
    return []


@pytest.fixture
def product_list_with_item():
    return [{"Pear", 300.00}]


def test_prod_enumerate(product_list_with_item):

    expected_outcome = "Number: 0, {'Product': 'Pear', 'Price': '300.0'}"

    mock_product_list = [{"Product": "Pear", "Price": "300.0"}]

    with mock.patch("builtins.print") as mock_print:
        enumerate_product(mock_product_list)
    mock_print.assert_called_with("Number: 0, {'Product': 'Pear', 'Price': '300.0'}")


def test_product_addition(product_list_with_no_products):
    mock_product = "Apple"
    mock_price = "5000"

    expected_outcome = [{"Product": "Apple", "Price": 5000.0}]

    mock_args = [mock_product, mock_price]
    with mock.patch("builtins.input") as mock_input:
        mock_input.side_effect = mock_args
        assert product_list_with_no_products == []
        add_product(product_list_with_no_products)
        assert product_list_with_no_products == expected_outcome


def test_prod_delete(product_list_with_item):
    mock_input = 0
    expected_outcome = []

    mock_args = [mock_input]
    with mock.patch("builtins.input") as mock_input:
        mock_input.side_effect = mock_args
        assert product_list_with_item == [{300.0, "Pear"}]
        delete_product(product_list_with_item)
        assert product_list_with_item == expected_outcome


def test_prod_change(product_list_with_item):
    mock_index = 0
    mock_new_product = "Potato"
    mock_new_price = "1.15"

    expected_outcome = [{"Product": "Potato", "Price": 1.15}]

    mock_product_list = [{"Product": "Pear", "Price": 3.15}]

    mock_args = [mock_index, mock_new_product, mock_new_price]
    with mock.patch("builtins.input") as mock_input:
        mock_input.side_effect = mock_args
        update_product(mock_product_list)
        assert mock_product_list == expected_outcome
