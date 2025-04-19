# Discord Timestamps CLI

A simple command-line tool for generating Discord timestamps from human-readable date/time formats.

## About

Discord timestamps allow you to show a date or time that automatically displays in the reader's local timezone. This CLI tool converts human-readable dates into various Discord timestamp formats.

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/discord-timestamps-cli.git
cd discord-timestamps-cli

# Make the script executable
chmod +x discord_timestamps.py
```

## Usage

```bash
# Generate timestamps for the current time
./discord_timestamps.py

# Generate timestamps for a specific date/time
./discord_timestamps.py "2023-01-30 15:30"
./discord_timestamps.py "30/01/2023 15:30"
./discord_timestamps.py "01/30/2023 15:30"
```

The tool supports multiple date formats including:
- YYYY-MM-DD HH:MM:SS
- YYYY-MM-DD HH:MM
- YYYY-MM-DD
- DD/MM/YYYY HH:MM:SS
- DD/MM/YYYY HH:MM
- DD/MM/YYYY
- MM/DD/YYYY HH:MM:SS
- MM/DD/YYYY HH:MM
- MM/DD/YYYY

## Discord Timestamp Formats

| Style           | Format           | Example Output (varies by user's timezone) |
| --------------- | ---------------- | ----------------------------------------- |
| Default         | `<t:timestamp>`   | November 28, 2023 9:01 AM                 |
| Short Time      | `<t:timestamp:t>` | 9:01 AM                                   |
| Long Time       | `<t:timestamp:T>` | 9:01:00 AM                                |
| Short Date      | `<t:timestamp:d>` | 11/28/2023                                |
| Long Date       | `<t:timestamp:D>` | November 28, 2023                         |
| Short Date/Time | `<t:timestamp:f>` | November 28, 2023 9:01 AM                 |
| Long Date/Time  | `<t:timestamp:F>` | Wednesday, November 28, 2023 9:01 AM      |
| Relative Time   | `<t:timestamp:R>` | 3 years ago                               |

## License

MIT
