import requests 
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = "1a8aabf5c07538dba884d25ca0aa6f33"


def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id': 2550})
    assert response.status_code == 200
    
    def test_part_of_body():
        response = requests.put(f'{host}/trainers', headers={"trainer_token":token}, json =
                             {
    "name": "Loners"
})
        assert response.json()["message"] == "Информация о тренере обновлена"
        
        def test_check_response():
            response = requests.get(host)
            response = response.json()
            assert response["trainer_name"] == "Loners"
        
@pytest.mark.parametrize('key,value', [("trainer_name", "Loners"),
                                       ("id", "2550")])

def test_response_json(key,value):
    response = requests.get(f'{host}/trainers', params={'trainer_id':2550})
    assert response.json()[key] == value