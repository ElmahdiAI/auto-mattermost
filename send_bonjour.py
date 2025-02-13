import os
import mattermostdriver
from mattermostdriver.exceptions import NoAccessTokenProvided

# Get configuration from environment variables
MATTERMOST_URL = os.getenv('MATTERMOST_URL')
TEAM_NAME = os.getenv('TEAM_NAME')
CHANNEL_NAME = os.getenv('CHANNEL_NAME')
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

def send_bonjour():
    try:
        # Initialize the Mattermost driver
        driver = mattermostdriver.Driver({
            'url': MATTERMOST_URL,
            'login_id': LOGIN,
            'password': PASSWORD,
            'scheme': 'https',
            'port': 443,
            'verify': True,
        })

        # Login to Mattermost
        driver.login()

        # Get team ID by team name
        team = driver.teams.get_team_by_name(TEAM_NAME)
        team_id = team['id']

        # Get channel ID by channel name
        channel = driver.channels.get_channel_by_name(team_id, CHANNEL_NAME)
        channel_id = channel['id']

        # Send "Bonjour" message
        driver.posts.create_post({
            'channel_id': channel_id,
            'message': 'Bonjour'
        })

        print("Message envoyé avec succès !")

    except NoAccessTokenProvided as e:
        print(f"Erreur : {e}. Vérifiez vos identifiants.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


if __name__ == "__main__":
    send_bonjour()
