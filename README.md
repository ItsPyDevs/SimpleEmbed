# SimpleWebhookEmbed

**A utility for creating and sending Discord embeds through discord Webhook**

## Overview

`SimpleWebhookEmbed` is a versatile Python package designed for creating and sending rich embeds to Discord. Whether you're building a bot or a custom integration, this package simplifies the process of crafting beautiful and informative messages that can be sent via Discord webhooks. 

Discord embeds are a powerful way to present content in a visually appealing format, allowing for enhanced interaction and presentation in your Discord channels. With `SimpleWebhookEmbed`, you can easily generate and customize embeds with various features and attributes to fit your needs.

## Features

- **__Create Embeds__**: Start by creating a new embed with a title and description. Customize it further with additional fields and attributes to meet your specific needs.
- **__Add Fields__**: Include one or more fields in your embed to present detailed information. Each field can be configured with a title, value, and optional inline setting.
- **__Customize Appearance__**: Adjust the embed’s appearance by setting colors, adding thumbnails, and specifying footer and author details. Enhance the visual impact of your embed to better capture attention.
- **__Send to Webhook__**: Seamlessly send the finalized embed to a Discord webhook URL. This allows you to deliver rich, formatted messages directly to your Discord channels.
- **__Help Command__**: Use the built-in help command to get detailed information about the available methods and their usage. This ensures you can quickly understand and utilize the package’s capabilities.

## Installation

To install `SimpleWebhookEmbed`, use `pip`, which is the Python package installer. Open your terminal or command prompt and run the following command:

```bash
git clone https://github.com/ItsPyDevs/SimpleWebhookEmbed/
cd SimpleWebhookEmbed
pip install .
```
This will download and install the package and its dependencies.

## Usage
Once installed, you can start using SimpleEmbed to create and send Discord embeds. Below is a basic example to get you started:

## Import the Package:

```python
from SimpleWebhookEmbed import SimpleEmbed
```

## Create an embed:
```python
embed = SimpleEmbed(title="Example Title", description="Example Description")
```


## Add a Field:
```python
embed.add_field(name="Field Name", value="Field Value", inline=True)
```
## Customize the Embed:
```py
embed.set_color(0xFF5733)  # Set the color of the embed
embed.set_footer(text="Footer Text", icon_url="https://example.com/icon.png")  # Add a footer
embed.set_thumbnail(url="https://example.com/thumbnail.png")  # Add a thumbnail
embed.set_author(name="Author Name", url="https://example.com", icon_url="https://example.com/author-icon.png")  # Set the author
```

## Send the Embed:
```python
webhook_url = ""
embed.send(webhook_url)
```

In this example, replace YOUR_WEBHOOK_ID and YOUR_WEBHOOK_TOKEN with your actual Discord webhook credentials.

## Available Methods

`set_title(title)`: Sets the title of the embed.

`set_description(description)`: Sets the description of the embed.

`add_field(name, value, inline=False)`: Adds a field to the embed. The inline parameter specifies if the field should be displayed inline with others.

`set_color(color)`: Sets the color of the embed using a hexadecimal color code.

`set_footer(text, icon_url=None)`: Sets the text and optional icon URL for the footer of the embed.

`set_thumbnail(url)`: Sets the URL of the thumbnail image for the embed.

`set_author(name, url=None, icon_url=None)`: Sets the author name, optional URL, and icon URL.

`remove_field(index)`: Removes a field at a specific index from the embed.

`clear_fields()`: Clears all fields from the embed.

`send(webhook_url)`: Sends the embed to the specified Discord webhook URL.

`help()`: Displays a help message with information about available methods and their usage.
