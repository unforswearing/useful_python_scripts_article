import heroku3
api_key = "12345-ABCDE-67890-FGHIJ"
client = heroku3.from_key(api_key)

client.apps()

# the above command prints an array of available applications
# [<app 'airplanedev-heroku-example - ed544e41-601d-4d1b-a327-9a1945b743cb'>, <app 'notes-app - 5b3d6aab-cde2-4527-9ecc-62bdee08ed4a'>, …] 

# use the following command to connect to a specific application
app = client.apps()["airplanedev-heroku-example"]

# add a config variable for your application
config = app.config()
config["test_var"] = "value"

# enable or disable maintenance mode
# enable
app.enable_maintenance_mode()

# disable
app.disable_maintenance_mode()

# restarting your application is simple
app.restart()
