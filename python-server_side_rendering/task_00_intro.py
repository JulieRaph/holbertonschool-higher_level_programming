import os

def generate_invitations(template, attendees):
    # check input type
    if not isinstance(template, str):
        print(f"Error: template must be a string")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print(f"Error: attendees must be a list of dictionnaries")
        return

    # check template and list of non-empty participants
    if not template:
        print(f"Template is empty, no output files generated.")
        return
    if not attendees:
        print(f"No data provided, no output files generated.")
        return

    # process each participant
    for index, attendee in enumerate(attendees, start=1):
        # create a copy for each attendee
        invitation = template
        # Replace placeholders with corresponding values, if empty N/A
        invitation = invitation.replace("{name}", attendee.get("name", "N/A"))
        invitation = invitation.replace("{event_title}", attendee.get("event_title", "N/A"))
        invitation = invitation.replace("{event_date}", attendee.get("event_date", "N/A"))
        invitation = invitation.replace("{event_location}", attendee.get("event_location", "N/A"))

    # Name of the output file
    output_file = f"output_{index}.txt"

    # check if the output file already exist
    if os.path.exists(output_file):
        print(f"Error : the file '{output_file}' already exists.")

    # write an invitation in the file
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(invitation)
            print(f"The invitation is generated {output_file}")
    except Exception as e:
        print(f"Error when writing file '{output_file}' : {e}")
