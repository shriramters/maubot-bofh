import random
import os
import importlib.resources

from maubot import Plugin, MessageEvent
from maubot.handlers import command

class BofhBot(Plugin):
    def get_excuse(self) -> str:
        """
        Reads the excuses file from the local source tree using the proper package resource method.
        """
        try:
            # Use importlib.resources to read the file from within the package/zip.
            excuses_text = importlib.resources.files('bofh').joinpath('excuses.txt').read_text(encoding='utf-8')
            excuses = [line.strip() for line in excuses_text.strip().split('\n') if line.strip()]

            if not excuses:
                return "The excuse file is empty. The problem exists between the keyboard and chair."

            return random.choice(excuses)
        except FileNotFoundError:
            self.log.error("excuses.txt not found inside the plugin package!")
            return "Error: excuses.txt not found inside the plugin package. The build is broken."
        except Exception as e:
            self.log.error(f"An unexpected error occurred reading package resources: {e}")
            return "A critical error occurred reading the excuses file."


    @command.new(name="excuse", help="Get a random BOFH excuse.")
    async def excuse_handler(self, evt: MessageEvent) -> None:
        """
        Handles the !excuse command.
        """
        await self.client.set_typing(evt.room_id, True)

        excuse = self.get_excuse()

        # This sends a new message to the room instead of a reply.
        await self.client.send_text(evt.room_id, excuse)

        await self.client.set_typing(evt.room_id, False)
