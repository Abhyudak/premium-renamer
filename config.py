import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "10006455")

API_HASH = os.environ.get("API_HASH", "5f56e57e1925dd75e577e38aabd10c1a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5566721946:AAHhjnDXw7EwghcfFolwHayXL89KCvbobjs") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","pyro-botz")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Nadas:Nadas@cluster0.uyhil.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/1d37b125283508b294503.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '739635492').split()]
