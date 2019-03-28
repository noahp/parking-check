#!/usr/bin/env python
"""
Just send an email, no goofy postfix messing around.
"""
import click
import smtplib


@click.command()
@click.option("--subject", "-s", help="Subject", type=click.STRING, required=True)
@click.option("--body", "-b", help="Body", type=click.STRING, required=True)
@click.option(
    "--dest-address",
    "-d",
    help="Destination email address",
    type=click.STRING,
    required=True,
)
@click.option(
    "--source-address",
    "-a",
    help="Source email address",
    type=click.STRING,
    required=True,
)
@click.option(
    "--source-password",
    "-p",
    help="Source email SMTP password",
    type=click.STRING,
    required=True,
)
def main(subject, body, dest_address, source_address, source_password):
    """Just send an email."""

    # creates SMTP session
    session = smtplib.SMTP("smtp.gmail.com", 587)

    # start TLS for security
    session.starttls()

    # Authentication
    session.login(source_address, source_password)

    # message to be sent
    message = """From: {source_address}
Subject: {subject}

{body}""".format(
        source_address=source_address, subject=subject, body=body
    )

    # sending the mail
    session.sendmail(source_address, dest_address, message)

    # terminating the session
    session.quit()


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
