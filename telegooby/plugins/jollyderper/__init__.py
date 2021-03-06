#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from random import choice, randint

from plugin import Plugin
from utils import is_text_message


class JollyDerper(Plugin):
    async def on_chat_message(self, message):
        if not is_text_message(message):
            return

        try:
            message_text = message['text']
        except KeyError:
            return
        for trigger in self.settings.get('triggers'):
            if trigger in message_text.lower():
                if '?' in message_text:
                    msg = choice(self.settings.get('answers'))
                elif '!' in message_text:
                    msg = choice(self.settings.get('exclamation_responses'))
                else:
                    max_words = 3
                    words_count = randint(1, max_words)
                    words = []
                    for _ in range(words_count):
                        words.append(choice(self.settings.get('herps_derps')))
                    msg = " ".join(words)
                return msg
