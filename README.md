# 🚗 mbta parking checker

Looks up if a MA license plate has any active parking charges on the MBTA site.

Crude, cheesy, and messy.

```bash
# really meant to execute from docker like this
docker build -t check-parking .

# fire away.
# `check-parking` uses some env vars for target/source email.
# pass a string to check-parking with the plate number
docker run -p 25:25 -p 587:587 -p 143:143 \
    -e TARGET_EMAIL=<target-email> \
    -e SOURCE_EMAIL=<source-email> \
    -e SOURCE_EMAIL_PASSWORD=<source-email-password> \
    -t parking-check bash -c "check-parking '<plate number>'"
```

The following env variables are set in the Travis job config:

- `$TARGET_EMAIL` - destination email address
- `$SOURCE_EMAIL` - source email address
- `$SOURCE_EMAIL_PASSWORD` - source email SMTP password
- `$PLATE_NUMBER` - plate number
