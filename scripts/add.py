import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# User can add name and favourite sport in response.json
# default sport Cricket will be added incase user does not provide fav sport


def load_json():
  
  with open('../response.json') as json_obj:
    response = json.load(json_obj)
  return response

response = loan_json()






def write_sport():
  name = input("Please add your name: ")
  sport = input("Please add your favourite sports name: ")
  if(sport ==""):
    sport = 'Cricket'
  if(name):
    response[name] = sport
    write_json(response)
    
    
if __name__ == "__main__":
  call_sport()

  
call_sport()
