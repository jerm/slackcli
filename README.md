# slack-cli
Slack CLI Application.

### Usage
```
Run the command:
slack-cli -t [TOKEN] -c [CHANNEL] "Hello World"`
slack-cli -t [TOKEN] -c [CHANNEL] -u [USERNAME] -i [ICON_URL] "Hello from Slack!"  # username & icon url are optionals`
 
To make thing simpler, you can also use environment variables to save the token, channel, username, and icon url.
For example:
 
# you can export these in shell or include these inside .bashrc
export SLACK_TOKEN=[TOKEN]
export SLACK_CHANNEL=[CHANNEL]
export SLACK_USERNAME=[USERNAME]
export SLACK_ICON_URL=[ICON_URL]
 
slack-cli "Hello World from Slack CLI!"
slack-cli "Hello again!"
slack-cli "42 is the answer to everything"
```
