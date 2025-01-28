''' File to explore bibl extraction from DHQ articles and Semantic Scholar API reconciliation'''
from lxml import etree
from pathlib import Path
import re
import requests
import argparse
import time
import logging

def extract_bibl(file):
    ''' Function to extract the listBibl tag and the bibl tags within it from DHQ XML files '''
    # Parse file using etree
    tree = etree.parse(file)
    # Define namespaces for files
    namespaces = {
        'tei': 'http://www.tei-c.org/ns/1.0',  
        'cc': 'http://web.resource.org/cc/',   
        'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
        'dhq': 'http://www.digitalhumanities.org/ns/dhq',
        'mml': 'http://www.w3.org/1998/Math/MathML'
    }

    # Find all <listBibl> tags
    listbibl_tags = tree.xpath('.//tei:listBibl', namespaces=namespaces)
    print(listbibl_tags)
    print(type(listbibl_tags))
    # Create bibl_data list
    bibl_data = []
    counter = 0
    # Find the content of each <listBibl> tag
    for listbibl in listbibl_tags:
        # Find all <bibl> tags within the current <listbibl> element
        bibl_tags = listbibl.xpath('.//tei:bibl', namespaces=namespaces)
        for bibl in bibl_tags:
            # grab the xml_id, label, and titles
            bibl_id = Path(file).stem + '_ref_' + str(counter)
            counter += 1
            xml_id = bibl.get('xml:id')
            label = bibl.get('label') 
            titles_quotes = bibl.xpath('.//tei:title[@rend="quotes"]', namespaces=namespaces)
            titles_ital = bibl.xpath('.//tei:title[@rend="italic"]', namespaces=namespaces)
            # create dictionary object for the fields
            bibl_entry = {
                'ref_id': bibl_id,
                'xml_id': xml_id,
                'label': label,
                'titles_quotes': [re.sub(r'\s+', ' ', title.text).strip() for title in titles_quotes],
                'titles_ital': [re.sub(r'\s+', ' ', title.text).strip() for title in titles_ital],
            }
            # append dictionary to list
            bibl_data.append(bibl_entry)

    return bibl_data

def s2_request(bibl_data):
    ''' Requesting Semantic Scholar with the title of citation '''
    for bibl in bibl_data:
        query_params = {
            "query": bibl['titles_quotes'] if bibl['titles_quotes'] else None,
            "fields": "title,authors,publicationDate",
            # "year": "-2022" <- This could be useful if we can get the year 
            # standardized for each citation?
        }
        logging.info("Requested Title: %s", bibl['titles_quotes'][0] if bibl['titles_quotes'] else None)
        # GET request trying to match the title. I was seeing in many (but not all) 
        # cases the title was in the <title rend:quotes> tag
        response = requests.get("https://api.semanticscholar.org/graph/v1/paper/search/match",
                                params=query_params, timeout=10)
        # Check response status
        if response.status_code == 200:
            response_data = response.json()
            # If we get a match via the title, we have to make another call with the paperID
            # to retrieve the BibTeX
            paper_id = response_data['data'][0]['paperId']
            print(paper_id)
            query_params = {
                "fields": "citationStyles"
            }
            detail_response = requests.get(f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}", params=query_params, timeout=10)
            detail_data = detail_response.json()
            # Logging data here but maybe we do some process
            logging.info("Response Received: %s", response_data)
            logging.info("Detail Response: %s", detail_data)
        else:
            logging.info("Response Failed: %s: %s", response.status_code, response.text)
        # Was getting 429 error of too many requests.
        # Temporary stop gap but would probably need exponential backoff and retry
        time.sleep(5)

def main():
    ''' Main function '''
    logging.basicConfig(level=logging.INFO, filename="output_log.txt", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")
    parser = argparse.ArgumentParser(description="Pull editions")
    # Argument for DHQ XML file to be parsed.
    parser.add_argument(
        'file',
        help='The DHQ XML file')
    args = parser.parse_args()
    bibl_data = extract_bibl(args.file)
    s2_request(bibl_data)

if __name__ == "__main__":
    main()
