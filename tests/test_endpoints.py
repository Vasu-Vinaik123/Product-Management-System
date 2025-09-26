
def test_create_seller(client):
  payload = {
      "username": "alice",
      "email": "alice@example.com",
      "password": "secret"
  }
  response = client.post("/seller", json=payload)
  assert response.status_code == 201
  data = response.json()
  assert data["username"] == "alice"
   

def test_get_seller(client):
  response = client.get("/seller")
  data = response.json()
  assert response.status_code == 200
  assert data[0]["username"] == "alice"



def test_create_product(client):
  payload = {
    "name":"Laptop",
    "description":"Asus ROG",
    "price":1800,
    "seller_id":1
  }

  response = client.post("/product", json=payload)
  data = response.json()
  assert response.status_code == 201
  assert data["name"] == "Laptop"
