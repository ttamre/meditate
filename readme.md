# Meditate
Python3 script to remind you to meditate


### Usage
1. Create a twilio account and fill in the following within a file `secrets.json`
    ```json
    {
        "account_sid": "",
        "auth_token": "",
        "client_number": ""
    }
    ```

2. Create a file `numbers.txt` with all the numbers you want to be reminded
3. Set up a cron job (example: every day at noon `0 12 * * * python3 ~/meditate.py`)