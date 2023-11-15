from nextcord.ext.commands import Bot, Cog
from nextcord import (
    slash_command,
    Colour,
    Embed,
    Interaction,
)


class Ping(Cog):
    def __init__(self, client: Bot) -> None:
        self.client = client

    @slash_command(name="ping", description="Voir la latence du bot")
    async def ping(self, interaction: Interaction):
        latency = round(self.client.latency*1000)
        await interaction.response.send_message(embed=Embed(
            title=f"Le latence du bot est de : {int(latency)}ms",
            colour=Colour.blue()
        ))

def setup(client: Bot):
    client.add_cog(Ping(client))
