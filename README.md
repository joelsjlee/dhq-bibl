# dhq-bibl
Testing ground for DHQ Bibliographies.

## Running
Run `python3 bibl.py 000585.xml` and it will parse the `<bibl>` tags from the XML file and query them against Semantic Scholar's API.

## To Do
* Retry with Exponential Backoff for Semantic Scholar
* Understanding matchScore on S2 responses
* Try [batch retrieval](https://api.semanticscholar.org/api-docs/#tag/Paper-Data/operation/post_graph_get_papers) of BibTeX instead of one by one