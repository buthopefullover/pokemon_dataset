from tkinter.ttk import Style
import requests 
import os
from bs4 import BeautifulSoup

# Function to retrieve elements with class 'image' from a list of URLs
def get_summary_from_hrefs(base_url, href):
    summaries = []

    url = f"{base_url}{href}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # image_elements = soup.find("div", class_="mw-parser-output").find_all("table", style="width: 100%; border: 1px solid #C0C0C0; background-color:#FFFFCC; border-radius: 70px; -moz-border-radius: 70px; -webkit-border-radius: 70px; -khtml-border-radius: 70px; -icab-border-radius: 70px; -o-border-radius: 70px;").find("tr").get_text()
        # Find all div elements with class "mw-parser-output"
        parser_output_divs = soup.find_all('div', class_='mw-parser-output')

        # Loop through the selected divs and find all tables except the ones with class "copytag copytag-yellow"
        for div in parser_output_divs:
            tables = div.find_all('table')
            text = href + ': '
            print(href)
            # Now, you can work with the tables you've selected, excluding the ones with class "copytag copytag-yellow"
            for table in tables:
                if 'copytag' not in table.get('class', []):
                    # Process or extract information from the table as needed
                    text += table.get_text().replace('\n', '') + '; '

            summaries.append(text)
    else:
        print(f"Failed to fetch {url}")

    return summaries


# Specify the directory path where you want to list the files
directory_path = r'C:\Users\Vic\Documents\Codes\pokemon_dataset\first_generation\0001_bulbasaur\page1'

# Create a text file to write the file names
output_file = '0001_Catalogue.txt'

# List all file names in the specified directory
file_names = os.listdir(directory_path)

# Open a file for writing with UTF-8 encoding
with open(output_file, "w", encoding="utf-8") as file:
    for file_name in file_names:
        # Split the filename into name and extension
        # name, extension = os.path.splitext(file_name)

        summaries = get_summary_from_hrefs("https://archives.bulbagarden.net/wiki/File:", file_name)
        for summary in summaries:
            file.write(summary + '\n')

print(f'File names written to {output_file}')