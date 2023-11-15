import os

from config import TOKEN

from nextcord import Intents
from nextcord.ext.commands import Bot


class Client(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_extensions()

    def load_extensions(self) -> None:
        print("---------[Loading]---------")
        loaded = []
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                self.load_extension(f"cogs.{filename[:-3]}")
                print(f"[System]: {filename[:-3]} cog loaded.")
                loaded.append(filename[:-3])
        print("---------------------------")
        return loaded

    def unload_extensions(self) -> None:
        print("--------[Unloading]--------")
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                self.unload_extension(f"cogs.{filename[:-3]}")
                print(f"[System]: {filename[:-3]} cog unloaded.")
        print("---------------------------")

    async def on_ready(self):
        print(f"Connecté en tant que : {self.user}")


client = Client(
    ".",
    intents=Intents(
        messages=True,
        guilds=True,
        members=True,
        message_content=True,
        invites=True,
    ),
)

if __name__ == "__main__":
    client.run(TOKEN)
