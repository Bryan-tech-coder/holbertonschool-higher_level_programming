#!/usr/bin/env python3

import os

def generate_invitations(template, attendees):
    # Validate template type
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    # Validate attendees type
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Check if template is empty
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        # Replace missing or None values with "N/A"
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        # Replace placeholders
        output = template
        output = output.replace("{name}", str(name))
        output = output.replace("{event_title}", str(event_title))
        output = output.replace("{event_date}", str(event_date))
        output = output.replace("{event_location}", str(event_location))

        filename = f"output_{i}.txt"

        try:
            # Optional: check if file exists
            if os.path.exists(filename):
                print(f"Warning: {filename} already exists. Overwriting.")

            with open(filename, "w") as f:
                f.write(output)

        except Exception as e:
            print(f"Error writing file {filename}: {e}")
