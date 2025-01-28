# dhq-bibl
Testing ground for DHQ Bibliographies.

## Running
Run `python3 bibl.py 000585.xml` and it will parse the `<bibl>` tags from the XML file and query them against Semantic Scholar's API.

## To Do
* Retry with Exponential Backoff for Semantic Scholar
* Understanding matchScore on S2 responses. When you query S2 with the title and there is a match, you also get a matchScore in the response. I have seen scores of 
as high as 311, and as low as 48, but there doesn't seem to be any documentation on the bounds of the score. We would want to reject any matches below a certain threshold.
* Try [batch retrieval](https://api.semanticscholar.org/api-docs/#tag/Paper-Data/operation/post_graph_get_papers) of BibTeX instead of one by one