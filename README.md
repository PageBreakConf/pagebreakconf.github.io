# Deploying the PageBreak Website

## Working with AirTable Data

The data for the speakers and sessions is exported from AirTable. Here's how to update the site with new data:

1. Export the relevant AirTable view as a CSV
1. Run the python cleanup script to strip out any sensitive data and reformat some data fields. The script takes 3 arguments: input file, outfile, and the type of data ("sessions" or "people"). The script runs like this:

        ```python
        python3 /Documents/git/pagebreak/scrub_and_format_json.py /Downloads/Humans-Speakers\ from\ Approved\ Sessions.csv /Documents/git/pagebreak/_data/2022people.json people
        ```

        or if you're processing the sessions data:

        ```python
        python3 /Documents/git/pagebreak/scrub_and_format_json.py /Downloads/Sessions-Yes\ Sessions\ Schedule.csv /Documents/git/pagebreak/_data/2022sessions.json sessions
        ```

1. Once the data has been cleaned, add the final output json to your git commit. DO NOT ADD THE AIRTABLE CSV TO YOUR COMMIT. Your git command should look something like this: `git add _data/2022people.json _data/2022sessions.json`.
1. Commit the changes: `git commit -m'updating data'`.
1. Push: `git push`.

## Speaker Images

Because AirTable image links expire, we need to add each speaker image to this repo, in the `assets/` subfolder (and further nested in a yearly subfolder as appropriate). Speaker images should be cropped to square dimensions, and the image path should be added to AirTable.