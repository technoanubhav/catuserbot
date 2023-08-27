from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 5504325
    API_HASH = "15c6833f2ba2767b908f6f67d5ee3cd7"
    # the name to display in your alive message
    ALIVE_NAME = "Anubhav"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://yjdccuod:q3OdZ7sPtbXTQ2SubfuZz1i15ZRckzPf@rajje.db.elephantsql.com/yjdccuod"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOHMBuwN7v8s4wuyc5Qgi0jnwlAPDYUblYY7mrX1JqXrCdq1qezb2TkYrK42_8LqqgWF8FlIbeP89WPP9yGnh4lmykocf5LSlZO8RwlZ6ov31yu7UQ5C45BFBK8pVbHhmd9MSVoZeOUQ2gVRV17m1V641rJQreeAyibUyDxfNHu6L3R_Ex5iUmmzma4F1OgCDhWj6Vf9JMmQBOxJFngYY7LdIk4uSDtXAmZD07Jgo8l2o9ErJ6Qbf-__ig3nE0ek2VLgiJLSNYJB0xKYxFKYyUPkCESITs7rvhsXVOgNZIqpuQaxmyeh6pdp--SACEuv-GxX49nWUGkXETo8gQOkHMYFPMco="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6614674167:AAEyj9yZGnk3sUrRJwNA0JePo8rwMUL7KQk"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -989884916
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"
