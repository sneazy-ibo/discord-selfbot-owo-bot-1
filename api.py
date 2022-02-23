import requests
username = input("Enter Your Username: ")
token = input("Enter Authorize Token: ")
try:
 r = requests.get('https://testapi.io/api/ahihiyou20/authorize',timeout=5)
except requests.exceptions.Timeout:
 print("Something Went Wrong! Please Try Again!")
 exit()
if r.status_code == 200:
 try:
  if token == r.json()[username]:
   print("Successfuly Logged In !")
  else:
   print("Invalid Token")
   exit()
 except KeyError:
  print("Invalid Username")
  exit()
else:
 print("Something Went Wrong! Please Try Again Later!")
 exit()