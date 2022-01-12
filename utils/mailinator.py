import json
import requests


class MailinatorAPI:
    def __init__(self):
        self.base_url = "https://mailinator.com/api/v2/domains/private/inboxes/"
        self.api_token = '4255eafc09fe41758026c9d5f1cb8710'

    def get_invited_link(self, email):
        messages_uri = self.base_url + email
        headers = {'Authorization': self.api_token, 'Content-Type': 'application/json'}
        response = requests.get(messages_uri, headers=headers)
        arr = response.content
        data = json.loads(arr)
        msgs_data = data["msgs"]
        print(msgs_data)
        print(type(msgs_data))
        email_data = list(msgs_data).__getitem__(0)
        id = email_data["id"]
        links_uri = messages_uri + f"/messages/{id}/links"
        response = requests.get(links_uri, headers=headers)
        links_data = json.loads(response.content)
        links = links_data["links"]
        invited_url = ""
        for l in links:
            if "invitation" in str(l):
                invited_url = l
        return invited_url

# print(APIClient().get_invited_link("zenq1631540691396"))