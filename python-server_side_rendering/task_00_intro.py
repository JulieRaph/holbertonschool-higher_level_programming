#!/usr/bin/python3

import os


def generate_invitations(template, attendees):
    """check input type"""
    try:
        if not isinstance(template, str):
            raise TypeError("Error: template must be a string")

        if not isinstance(attendees, list) or not all(
                isinstance(attendee, dict) for attendee in attendees):
            raise TypeError("Error: attendees must be a list of dictionnaries")
    except TypeError as e:
        print("TypeError: {}".format(e))
        return

    """check template and list of non-empty participants"""
    try:
        if not template:
            raise ValueError("Template is empty, no output files generated.")

        if not attendees:
            raise ValueError("No data provided, no output files generated.")
    except ValueError as e:
        print("ValueError: {}".format(e))
        return

    """process each participant"""
    for index, attendee in enumerate(attendees, start=1):
        """create a copy for each attendee"""
        invitation = template
        """Replace placeholders with corresponding values, if empty N/A"""
        invitation = invitation.replace(
            "{name}", attendee.get("name", "N/A"))
        invitation = invitation.replace(
            "{event_title}", attendee.get("event_title", "N/A"))
        invitation = invitation.replace(
            "{event_date}", attendee.get("event_date", "N/A"))
        invitation = invitation.replace(
            "{event_location}", attendee.get("event_location", "N/A"))

        """Name of the output file"""
        output_file = f"output_{index}.txt"

        """check if the output file already exist"""
        if os.path.exists(output_file):
            print(f"Error : the file '{output_file}' already exists.")
            continue

        """write an invitation in the file"""
        try:
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(invitation)
                print(f"The invitation is generated {output_file}")
        except Exception as e:
            print(f"Error when writing file '{output_file}' : {e}")
