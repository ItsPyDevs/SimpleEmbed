import requests
import json

class SimpleEmbed:
    def __init__(self, title="", description="") -> None:
        self.embed = {
            "title": title,
            "description": description,
            "color": 5814783,  # Default color (green)
            "fields": []
        }

    def add_field(self, name, value, inline=False) -> None:
        """Add a field to the embed."""
        self.embed['fields'].append({
            "name": name,
            "value": value,
            "inline": inline
        })

    def set_color(self, color):
        """Set the color of the embed."""
        self.embed['color'] = color

    def set_footer(self, text, icon_url=None) -> None:
        """Set the text and icon of the footer."""
        self.embed['footer'] = {
            "text": text
        }
        if icon_url:
            self.embed['footer']['icon_url'] = icon_url

    def set_thumbnail(self, url) -> None:
        """Set the URL of the thumbnail."""
        self.embed['thumbnail'] = {
            "url": url
        }

    def set_author(self, name, url=None, icon_url=None) -> None:
        """Set the author of the embed."""
        self.embed['author'] = {
            "name": name
        }
        if url:
            self.embed['author']['url'] = url
        if icon_url:
            self.embed['author']['icon_url'] = icon_url

    def remove_field(self, index) -> None:
        """Remove a field at a specific index."""
        if 0 <= index < len(self.embed['fields']):
            self.embed['fields'].pop(index)
        else:
            print(f"Index {index} out of bounds.")

    def clear_fields(self) -> None:
        """Clear all fields from the embed."""
        self.embed['fields'] = []

    def set_title(self, title) -> None:
        """Set the title of the embed."""
        self.embed['title'] = title

    def set_description(self, description) -> None:
        """Set the description of the embed."""
        self.embed['description'] = description

    def help(self) -> str:
        """Display help for available options."""
        help_text = """
        Available methods:
        - set_title(title): Sets the title of the embed.
        - set_description(description): Sets the description of the embed.
        - add_field(name, value, inline): Adds a field to the embed.
        - set_color(color): Sets the color of the embed (in hex).
        - set_footer(text, icon_url): Sets the text and icon of the footer.
        - set_thumbnail(url): Sets the URL of the thumbnail.
        - set_author(name, url, icon_url): Sets the author of the embed.
        - remove_field(index): Removes a field at a specific index.
        - clear_fields(): Clears all fields from the embed.
        - send(webhook_url): Sends the embed to a Discord webhook.
        - help(): Displays this help message.
        """
        print(help_text)

    def send(self, webhook_url) -> None:
        """Send the embed to a Discord webhook."""
        response = requests.post(
            webhook_url,
            data=json.dumps({"embeds": [self.embed]}),
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 204:
            print("Embed sent successfully!")
        else:
            print(f"Error sending embed: {response.status_code}")
            print(response.text)
