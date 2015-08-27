# slack-cli
Slack CLI Application.

### Usage
```
Run the command:
slackcli -t [TOKEN] -c [CHANNEL] "Hello World"`
slackcli -t [TOKEN] -c [CHANNEL] -u [USERNAME] -i [ICON_URL] "Hello from Slack!"  # username & icon url are optionals`
 
To make thing simpler, you can also use environment variables to save the token, channel, username, and icon url.
For example:
 
# you can export these in shell or include these inside .bashrc
export SLACK_TOKEN=[TOKEN]
export SLACK_CHANNEL=[CHANNEL]
export SLACK_USERNAME=[USERNAME]
export SLACK_ICON_URL=[ICON_URL]
 
slackcli "Hello World from Slack CLI!"
slackcli "Hello again!"
slackcli "42 is the answer to everything"
```
