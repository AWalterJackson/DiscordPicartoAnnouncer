This project requires Python 3 and the requests library.

Configuration is taken from a webhooks.json file that is placed in the same directory as the picartoAlertWebhooker.py file.
An example of the webhooks.json required syntax is below:

```JSON
{
    "webhooks": [
        {
            "serverName": "Example",
            "useAtHere": false,
            "url": "https://discordapp.com/api/webhooks/webhookURL",
            "creators": ["Creators", "Names", "Here"]
        }
    ]
}
```

| Field      | Purpose                                                                                                  |
| ---------- | -------------------------------------------------------------------------------------------------------- |
| serverName | Used internally for debugging and separating alerts by server. Not required to match actual server name. |
| useAtHere  | Whether to include an @here tag in the notification posted to the server.                                |
| url        | The webhook URL for this server.                                                                         |
| creators   | An array of the channel names to check                                                                   |