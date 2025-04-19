#!/usr/bin/env python3

import argparse
import datetime
import time
from typing import Optional


def get_timestamp(date_str: Optional[str] = None) -> int:
    """Convert a human-readable date string to a Unix timestamp."""
    if date_str is None:
        # Use current time if no date is provided
        return int(time.time())
    
    # Check if the input is just a time (HH:MM)
    time_only_formats = [
        "%H:%M",      # 15:30 (24-hour format)
        "%I:%M %p",   # 3:30 PM (12-hour format)
    ]
    
    # Try time-only formats first - if matched, use today's date
    for fmt in time_only_formats:
        try:
            time_obj = datetime.datetime.strptime(date_str, fmt).time()
            # Combine with today's date
            today = datetime.date.today()
            dt = datetime.datetime.combine(today, time_obj)
            return int(dt.timestamp())
        except ValueError:
            continue
    
    # Try to parse the date string in various formats
    formats = [
        "%Y-%m-%d %H:%M:%S",  # 2023-01-30 15:30:45
        "%Y-%m-%d %H:%M",      # 2023-01-30 15:30
        "%Y-%m-%d",            # 2023-01-30
        "%d/%m/%Y %H:%M:%S",   # 30/01/2023 15:30:45
        "%d/%m/%Y %H:%M",      # 30/01/2023 15:30
        "%d/%m/%Y",            # 30/01/2023
        "%m/%d/%Y %H:%M:%S",   # 01/30/2023 15:30:45
        "%m/%d/%Y %H:%M",      # 01/30/2023 15:30
        "%m/%d/%Y",            # 01/30/2023
    ]
    
    for fmt in formats:
        try:
            dt = datetime.datetime.strptime(date_str, fmt)
            return int(dt.timestamp())
        except ValueError:
            continue
    
    raise ValueError(
        "Could not parse date string. Please use a format like 'YYYY-MM-DD HH:MM:SS', 'DD/MM/YYYY HH:MM', or just 'HH:MM' for today's date"
    )


def display_timestamps(timestamp: int) -> None:
    """Display all Discord timestamp formats with their rendered appearance."""
    formats = {
        "Default": "",
        "Short Time": "t",
        "Long Time": "T",
        "Short Date": "d",
        "Long Date": "D",
        "Short Date/Time": "f",
        "Long Date/Time": "F",
        "Relative Time": "R",
    }
    
    print("\nDiscord Timestamps (copy and paste these into Discord):")
    print("-" * 60)
    
    # Calculate local time from the timestamp for display
    local_time = datetime.datetime.fromtimestamp(timestamp)
    formatted_local_time = local_time.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"For time: {formatted_local_time} (local)\n")
    
    # Create renderings for each format
    now = datetime.datetime.now()
    
    for name, code in formats.items():
        if code:
            discord_format = f"<t:{timestamp}:{code}>"
        else:
            discord_format = f"<t:{timestamp}>"
        
        # Generate the rendered appearance based on the format code
        rendered = ""
        dt = datetime.datetime.fromtimestamp(timestamp)
        
        if code == "t":  # Short Time (e.g., 1:23 PM)
            rendered = dt.strftime("%I:%M %p")
        elif code == "T":  # Long Time (e.g., 1:23:45 PM)
            rendered = dt.strftime("%I:%M:%S %p")
        elif code == "d":  # Short Date (e.g., 01/30/2023)
            rendered = dt.strftime("%m/%d/%Y")
        elif code == "D":  # Long Date (e.g., January 30, 2023)
            rendered = dt.strftime("%B %d, %Y")
        elif code == "f":  # Short Date/Time (e.g., January 30, 2023 1:23 PM)
            rendered = dt.strftime("%B %d, %Y %I:%M %p")
        elif code == "F":  # Long Date/Time (e.g., Monday, January 30, 2023 1:23 PM)
            rendered = dt.strftime("%A, %B %d, %Y %I:%M %p")
        elif code == "R":  # Relative Time (e.g., 5 minutes ago, in 2 hours)
            time_diff = dt - now
            days_diff = time_diff.days
            seconds_diff = time_diff.seconds
            
            if days_diff == 0 and abs(seconds_diff) < 60:
                rendered = "just now"
            elif days_diff == 0 and seconds_diff < 0:
                minutes = abs(seconds_diff) // 60
                if minutes == 1:
                    rendered = "1 minute ago"
                else:
                    rendered = f"{minutes} minutes ago"
            elif days_diff == 0 and seconds_diff > 0:
                minutes = seconds_diff // 60
                if minutes == 1:
                    rendered = "in 1 minute"
                else:
                    rendered = f"in {minutes} minutes"
            elif days_diff < 0:
                if days_diff == -1:
                    rendered = "yesterday"
                else:
                    rendered = f"{abs(days_diff)} days ago"
            elif days_diff > 0:
                if days_diff == 1:
                    rendered = "tomorrow"
                else:
                    rendered = f"in {days_diff} days"
        else:  # Default (e.g., January 30, 2023 1:23 PM)
            rendered = dt.strftime("%B %d, %Y %I:%M %p")
        
        print(f"{name:<16} → {discord_format:<16} → {rendered}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate Discord timestamps from human-readable dates"
    )
    parser.add_argument(
        "date", 
        nargs="?", 
        help="Human readable date time: 'YYYY-MM-DD HH:MM', 'MM/DD/YYYY', or just 'HH:MM' for today's date with that time. "
             "If no args, defaults to current time."
    )
    
    args = parser.parse_args()
    
    try:
        timestamp = get_timestamp(args.date)
        display_timestamps(timestamp)
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main()) 