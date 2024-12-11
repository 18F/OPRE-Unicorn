from typing import List

from blinker import signal
from flask import current_app
from loguru import logger

from models import OpsEvent, OpsEventType


class MessageBus:
    """
    A simple message bus implementation that allows for publishing and subscribing to events.

    This message bus implementation uses the Blinker library to handle event signals.

    This message bus assumes it exists in a single thread and is meant to be used within the context of a single request.

    Published events are stored in a list and are handled when the handle method is called (usually at the end of a request).
    """

    published_events: List[OpsEvent] = []

    def handle(self):
        """
        Handle all published events by calling the appropriate handlers for each event type.
        """
        for event in self.published_events:
            ops_signal = signal(event.event_type.name)
            ops_signal.send(event, session=current_app.db_session)
            logger.info(f"Handling event {event}")

    def subscribe(self, event_type: OpsEventType, callback: callable):
        """
        Subscribe to an event type with a callback function.

        :param event_type: The event type to subscribe to.
        :param callback: The callback function to call when the event is published.
        """
        logger.debug(f"Subscribing to {event_type} with callback {callback}")
        ops_signal = signal(event_type.name)
        ops_signal.connect(callback)

    def publish(self, event_type: OpsEventType, event: OpsEvent):
        """
        Publish an event with the given event type and details.

        N.B. This method does not handle the event immediately. The event will be handled when the handle method is called.

        :param event_type: The event type to publish.
        :param event: The event details to publish.
        """
        logger.debug(f"Publishing event {event_type} with details {event}")
        self.published_events.append(event)
