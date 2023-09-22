import os
import time
from dotenv import load_dotenv
from get_post_id import InstaScraping

class Main:
    def run_app(self):

        username_var = os.getenv("IG_USERNAME")
        password_var = os.getenv("IG_PASSWORD")
        access_token_var = os.getenv("ACCESS_TOKEN")

        try:
            load_dotenv()
            get_post_id = InstaScraping(username=username_var, password=password_var)
            get_post_id.run()
            time.sleep(2)

            

            