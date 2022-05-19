import heroku3
api_key = "12345-ABCDE-67890-FABCD"
client = heroku3.from_key(api_key)

client.create_app("app-created-with-airplane")
