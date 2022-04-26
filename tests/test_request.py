def test_hit_increase(client):
    response = client.get("/")
    assert b"Counter hit 1 times" in response.data
    response = client.get("/")
    assert b"Counter hit 2 times" in response.data


def test_hit_reset(client):
    response = client.get("/")
    response = client.get("/")
    response = client.get("/reset")
    assert b"Counter reset" in response.data
    response = client.get("/")
    assert b"Counter hit 1 times" in response.data
