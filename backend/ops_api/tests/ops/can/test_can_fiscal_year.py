import pytest
from models.cans import CANFiscalYear


@pytest.mark.usefixtures("app_ctx")
def test_can_fiscal_year_lookup(loaded_db):
    cfy = (
        loaded_db.session.query(CANFiscalYear)
        .filter(CANFiscalYear.can_id == 1, CANFiscalYear.fiscal_year == 2022)
        .one()
    )
    assert cfy is not None
    assert cfy.fiscal_year == 2022
    assert cfy.total_fiscal_year_funding == 1233123
    assert cfy.potential_additional_funding == 89000
    assert cfy.can_lead == "Tim"
    assert cfy.notes == "No notes here."


def test_can_fiscal_year_create():
    cfy = CANFiscalYear(
        can_id=1,
        fiscal_year=2023,
        total_fiscal_year_funding=55000,
        potential_additional_funding=100,
        can_lead="Ralph",
        notes="all-the-notes!",
    )
    assert cfy.to_dict()["fiscal_year"] == 2023


@pytest.mark.usefixtures("app_ctx")
@pytest.mark.usefixtures("loaded_db")
def test_can_get_can_fiscal_year_list(client):
    response = client.get("/api/v1/can-fiscal-year/")
    assert response.status_code == 200
    assert len(response.json) == 5
    assert response.json[0]["can_id"] == 1
    assert response.json[1]["can_id"] == 1
    assert response.json[2]["can_id"] == 2
    assert response.json[3]["can_id"] == 2
    assert response.json[4]["can_id"] == 3


@pytest.mark.usefixtures("app_ctx")
@pytest.mark.usefixtures("loaded_db")
def test_can_get_can_fiscal_year_by_id(client):
    response = client.get("/api/v1/can-fiscal-year/1")
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]["can_id"] == 1
    assert response.json[1]["can_id"] == 1


@pytest.mark.usefixtures("app_ctx")
@pytest.mark.usefixtures("loaded_db")
def test_can_get_can_fiscal_year_by_year(client):
    response = client.get("/api/v1/can-fiscal-year/?year=2022")
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]["can_id"] == 1
    assert response.json[1]["can_id"] == 2


@pytest.mark.usefixtures("app_ctx")
@pytest.mark.usefixtures("loaded_db")
def test_can_get_can_fiscal_year_by_can(client):
    response = client.get("/api/v1/can-fiscal-year/?can_id=1")
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]["can_id"] == 1
    assert response.json[1]["can_id"] == 1


@pytest.mark.usefixtures("app_ctx")
@pytest.mark.usefixtures("loaded_db")
def test_can_get_can_fiscal_year_by_can_and_year(client):
    response = client.get("/api/v1/can-fiscal-year/?can_id=1&year=2022")
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["can_id"] == 1
