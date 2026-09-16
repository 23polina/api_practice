import json
import pytest


def test_verify_get_events_endpoint(api_client):
    params = {
        "limit": 2
    }
    get_response = api_client.get_endpoint("events", params=params)
    get_response_json = get_response.json()
    assert get_response.status_code == 200
    assert get_response_json["data"][0]["id"] == "evt:aaiahk:2016-02-27:loss-of-control-inflight-accident-invest:ZLINZ242L"
    assert get_response_json["data"][1]["id"] == "evt:aaiahk:2016-10-23:aircraft-accident-report-1-2019-air-acci:ROBINSONR22B"
    assert get_response_json["next_cursor"] == "evt:aaiahk:2016-10-23:aircraft-accident-report-1-2019-air-acci:ROBINSONR22B"
    with pytest.raises(IndexError):
        get_response_json["data"][3]


def test_verify_event_by_id(api_client):
    get_events_response = api_client.get_endpoint("events")
    event_id = get_events_response.json()["data"][0]["id"]
    get_event_id_response = api_client.get_endpoint(f"events/{event_id}")

    assert get_event_id_response.status_code == 200

    with open("test_data/expected_event_by_id_response.json") as file:
        expected_response_event_by_id = json.load(file)

    assert get_event_id_response.json() == expected_response_event_by_id


def test_not_found_event_by_incorrect_id(api_client):
    get_event_response = api_client.get_endpoint("events/ereeeee")
    get_event_response_json = get_event_response.json()["error"]

    assert get_event_response.status_code == 404
    assert get_event_response_json == {"code": "not_found",
                                       "message": "no occurrence with id 'ereeeee'"}


def test_get_all_courses(api_client):
    get_sources_response = api_client.get_endpoint("sources")
    get_sources_response_json = get_sources_response.json()["data"][1]

    assert get_sources_response.status_code == 200
    assert get_sources_response_json == {"code": "mak",
                                         "name": "the Interstate Aviation Committee (MAK)",
                                         "license": "MAK official investigation reports",
                                         "homepage": "https://mak-iac.org/",
                                         "narratives": 450,
                                         "policy": "excerpt"
                                         }


def test_data_aircraft_family_boeing_787(api_client):
    get_aircraft_family_response = api_client.get_endpoint("aircraft/boeing-787/safety")
    get_aircraft_family_response_json = get_aircraft_family_response.json()

    assert get_aircraft_family_response.status_code == 200

    with open("test_data/boeing-787_family.json") as file_boeing:
        expected_boeing_json = json.load(file_boeing)

    assert get_aircraft_family_response_json == expected_boeing_json


def test_not_found_aircraft_family(api_client):
    get_invalid_response = api_client.get_endpoint("aircraft/boeing-787000/safety")
    get_invalid_response_json = get_invalid_response.json()["error"]
    assert get_invalid_response.status_code == 404
    assert get_invalid_response_json == {"code": "not_found",
                                         "message": "no aircraft family with slug 'boeing-787000'"}