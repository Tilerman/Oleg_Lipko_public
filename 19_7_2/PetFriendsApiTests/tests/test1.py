from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()

def test_successful_update_self_pet_info(self, name='Мурзик',
                                         animal_type='Котэ', age=5):
   _, auth_key = self.pf.get_api_key(valid_email, valid_password)
   _, my_pets = self.pf.get_list_of_pets(auth_key, "my_pets")

   if len(my_pets['pets']) > 0:
       status, result = self.pf.update_pet_info(auth_key, my_pets['pets'][0]['id'],
                                                name, animal_type, age)
       assert status == 200
       assert result['name'] == name
   else:
       raise Exception("There is no my pets")
