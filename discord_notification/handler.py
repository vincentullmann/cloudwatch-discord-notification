"""Small Function to send lambda error messges to Discord.

Ref: https://aws.amazon.com/blogs/mt/get-notified-specific-lambda-function-error-patterns-using-cloudwatch/

"""
# IMPORT STANDARD LIBRARIES
import base64
import gzip
import json
import typing

# IMPORT LOCAL LIBRARIES
import discord_sender


def parse_event(event: typing.Any):
    """Parse the Log Payload from an Cloudwatch Event."""
    compressed_payload = base64.b64decode(event['awslogs']['data'])
    uncompressed_payload = gzip.decompress(compressed_payload)
    log_payload = json.loads(uncompressed_payload)
    return log_payload


def handler(event, *_, **__) -> None:
    """Handle Lambda Events."""
    payload = parse_event(event)
    discord_sender.send_message(payload)
