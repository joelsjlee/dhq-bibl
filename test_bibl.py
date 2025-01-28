import pytest
from lxml import etree
from bibl import extract_bibl

mock_xml = '''<?xml version="1.0" encoding="UTF-8"?><?oxygen RNGSchema="../../common/schema/DHQauthor-TEI.rng" type="xml"?><?oxygen SCHSchema="../../common/schema/dhqTEI-ready.sch"?><TEI xmlns="http://www.tei-c.org/ns/1.0" xmlns:cc="http://web.resource.org/cc/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dhq="http://www.digitalhumanities.org/ns/dhq" xmlns:mml="http://www.w3.org/1998/Math/MathML">
   <text xml:lang="en" type="original">
      <front>
      </front>
      <body>
      </body>
      <back>
         <listBibl>
            <bibl xml:id="crymble2016" label="Crymble 2016"> Crymble, Adam. <title rend="quotes">Identifying and Removing Gender Barriers in Open Learning Communities: <title rend="italic">The Programming Historian,</title></title> <title rend="italic">Blended Learning in Practice</title> (2016): 49-60, <ref target="http://researchprofiles.herts.ac.uk/portal/files/10476604/Blip_2016_Autumn_2016_Final_Autumn_2016.pdf">https://researchprofiles.herts.ac.uk/portal/files/10476604/Blip_2016_Autumn_2016_Final_Autumn_2016.pdf</ref>.</bibl>
               <bibl><title rend="quotes">Multilingual Guide,</title><title rend="italic"> Drupal
                  Documentation</title>. Available from: <ref target="https://www.drupal.org/docs/multilingual-guide">https://www.drupal.org/docs/multilingual-guide</ref>. Date accessed: August 25,
               2021.</bibl>
            <bibl xml:id="gibbs2015" label="Gibbs 2015"> Gibbs, Fred. <title rend="quotes">Editorial
                  Sustainability and Open Peer Review at <title rend="italic">Programming
                     Historian,</title></title> <title rend="italic">DH Commons</title>, 1 (2015).
                  <ref target="https://web.archive.org/web/20180713014622/http://dhcommons.org/journal/issue-1/editorial-sustainability-and-open-peer-review-programming-historian">https://web.archive.org/web/20180713014622/http://dhcommons.org/journal/issue-1/editorial-sustainability-and-open-peer-review-programming-historian.</ref>
               </bibl>
            <bibl xml:id="gil2015" label="Gil 2015"> Gil, Alex. <title rend="quotes">The User, the
                  Learner and the Machines We Make,</title> <title rend="italic">Minimal Computing: A Working Group of GO::DH</title>, May 21, 2015.<ref target="https://go-dh.github.io/mincomp/thoughts/2015/05/21/user-vs-learner/">https://go-dh.github.io/mincomp/thoughts/2015/05/21/user-vs-learner/</ref>.</bibl>
            <bibl xml:id="isasi2021" label="Isasi and Rojas Castro 2021"> Isasi, Jennifer and Antonio Rojas
               Castro. <title rend="quotes">¿Sin equivalencia? Una reflexión sobre la traducción al
                  español de recursos educativos abiertos.</title>
               <title rend="italic">Hispania</title> vol. 104.4 (December 2021). <ref target="https://doi.org/10.1353/hpn.2021.0130.">https://doi.org/10.1353/hpn.2021.0130</ref>.</bibl>
            <bibl xml:id="lecher2019" label="Lecher 2019"> Lecher, Colin. <title rend="quotes">GitHub Will Keep Selling Software to ICE, Leaked Email Says.</title>
               <title rend="italic">The Verge</title>, October 9, 2019.
               <ref target="https://www.theverge.com/2019/10/9/20906213/github-ice-microsoft-software-email-contract-immigration-nonprofit-donation">https://www.theverge.com/2019/10/9/20906213/github-ice-microsoft-software-email-contract-immigration-nonprofit-donation</ref>.</bibl>
            <bibl xml:id="lincoln2017" label="Lincoln 2017"> Lincoln, Matthew. <title rend="quotes">Infrastructure for Collaboration: Catching Dead Links And Errors,</title>
               <title rend="italic">The Programming Historian Blog</title>, July 31, 2017. <ref target="https://programminghistorian.org/posts/infrastructure-at-ph">https://programminghistorian.org/posts/infrastructure-at-ph</ref>.</bibl>
            <bibl xml:id="lincoln2020" label="Lincoln 2020"> Lincoln, Matthew. <title rend="quotes">Multilingual Jekyll: How <title rend="italic">The Programming Historian</title>
                  Does That,</title> (personal blog) March 1, 2020. <ref target="https://matthewlincoln.net/2020/03/01/multilingual-jekyll.html">https://matthewlincoln.net/2020/03/01/multilingual-jekyll.html</ref>.</bibl>
               <bibl><title rend="quotes">Localization in .NET,</title><title rend="italic"> Microsoft
                  Docs</title>. Available from: <ref target="https://docs.microsoft.com/en-us/dotnet/core/extensions/localization">https://docs.microsoft.com/en-us/dotnet/core/extensions/localization</ref>. Date
               accessed: August 25, 2021.</bibl>
            <bibl xml:id="niche2009" label="NiCHE 2009">
               <title rend="quotes">The Programming Historian,</title>
               <title rend="italic">Network in Canadian History &amp; Environment</title>. Accessed April 10, 2022. <ref target="http://web.archive.org/web/20091211210942/http://niche-canada.org/programming-historian">http://web.archive.org/web/20091211210942/http://niche-canada.org/programming-historian</ref>.</bibl>
            <bibl xml:id="ph246" label="PH Issue 246">
               <title rend="quotes">Spanish translation - Issue #246,</title>
               <title rend="italic">Programming Historian GitHub Repository</title>. Accessed April 10, 2022.
                  <ref target="https://github.com/programminghistorian/jekyll/issues/246">https://github.com/programminghistorian/jekyll/issues/246</ref>.</bibl>
            <bibl xml:id="ratto2011" label="Ratto 2011"> Ratto, Matt. <title rend="quotes">Critical
                  Making: Conceptual and Material Studies in Technology and Social Life,</title>
               <title rend="italic">The Information Society: An International Journal</title>, vol. 27.4
               (2011): 252-260. <ref target="https://doi.org/10.1080/01972243.2011.583819">https://doi.org/10.1080/01972243.2011.583819</ref>.</bibl>
            <bibl xml:id="sichani2019" label="Sichani et al. 2019"> Sichani, Anna-Maria, James
               Baker, Maria José Afanador Llach and Brandon Walsh. <title rend="quotes">Diversity
                  and Inclusion in Digital Scholarship and Pedagogy: The Case of The Programming
                  Historian</title>, <title rend="italic">Insights</title> (2019). <ref target="https://doi.org/10.1629/uksg.465">https://doi.org/10.1629/uksg.465</ref>.</bibl>
            <bibl xml:id="smithies2019" label="Smithies et al. 2019"> Smithies, James, Carina
               Westling, Anna-Maria Sichani, Pam Mellen and Arianna Ciula. <title rend="quotes">Managing 100 Digital Humanities Projects: Digital Scholarship &amp; Archiving in
                  King’s Digital Lab,</title> <title rend="italic">Digital Humanities
                  Quarterly</title>, vol. 13.1 (2019). <ref target="http://www.digitalhumanities.org/dhq/vol/13/1/000411/000411.html">https://www.digitalhumanities.org/dhq/vol/13/1/000411/000411.html</ref>.</bibl>
         </listBibl>
      </back>
   </text>
</TEI>
'''

def test_extract_list_bibl(tmp_path):
    ''' Testing the extraction function of the bibl.py file '''
    mock_file = tmp_path / "mock_file.xml"
    mock_file.write_text(mock_xml)
    bibl_data = extract_bibl(mock_file)
    assert len(bibl_data) == 14
    assert bibl_data[0]['ref_id'] == 'mock_file_ref_0'
    assert bibl_data[0]['xml_id'] == 'crymble2016'
    assert bibl_data[0]['xml_label'] == 'Crymble 2016'
    assert bibl_data[0]['xml_titles_quotes'] == [
            "Identifying and Removing Gender Barriers in Open Learning Communities:"
        ]
    assert bibl_data[0]['xml_titles_ital'] == [
            "The Programming Historian,",
            "Blended Learning in Practice"
        ]

