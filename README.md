# 🚗 mbta parking checker

Looks up if a MA license plate has any active parking charges on the MBTA site.

Crude, cheesy, and messy.

```bash
# fire away.
# `check-parking` uses some env vars for target/source email.
# pass a string to check-parking with the plate number
TARGET_EMAIL=<target-email> \
    SOURCE_EMAIL=<source-email> \
    SOURCE_EMAIL_PASSWORD=<source-email-password> \
    check-parking <plate number>
```

The following env variables are used by the script:

- `$TARGET_EMAIL` - destination email address
- `$SOURCE_EMAIL` - source email address
- `$SOURCE_EMAIL_PASSWORD` - source email SMTP password
- `$PLATE_NUMBER` - plate number
