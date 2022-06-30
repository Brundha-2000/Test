from django.test import TestCase, Client
from django.urls import is_valid_path, reverse

application_type= 'application/json'

class studentTest(TestCase):

  def test_student_index(self):
    assert is_valid_path("")

  def test_student_show(self):
    self.client=Client()
    # data = {"name":'bhavya'}
    url = reverse('show/',args=['system_type'])
    response= self.client.get(url, content_type=application_type)
    result=response.json()
    assert (result == {})
    assert (response.status_code == 200)


  def test_your_view_name(self):
    self.client = Client()
    url = reverse('', args=[''])
    data = {
    'name':'kavya',
    'age':28,
    'email':'kavya@gmail.com',
    'phone':811014083
    }
    response = self.client.post(url, data=data, content_type=application_type)
    result = response.json()
    assert (response.status_code == 200)
    # assert result["data"] = < your expected result > # optional


# from django.test import Client
# c = Client()
# response = c.post('/login/', {'username': 'john', 'password': 'smith'})
# response = c.get('/student/details/')
