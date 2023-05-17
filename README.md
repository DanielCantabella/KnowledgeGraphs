![schema.png](schema.png)

# Q1. Find all Authors
```
PREFIX ex: <http://www.semanticweb.org/danicantabella/ontologies/2023/4/SDM_Lab3/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?author_id ?name
WHERE {
   { 
     ?author_id rdf:type ex:author .
     ?author_id ex:name_human ?name .
   }
}
```
# Q2. Find all properties whose domain is Author
```
PREFIX ex: <http://www.semanticweb.org/danicantabella/ontologies/2023/4/SDM_Lab3/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT DISTINCT ?property
WHERE {
  ?property rdf:type owl:ObjectProperty ;
            rdfs:domain [ rdf:type owl:Restriction ;
                          owl:onProperty ?property_domain ;
                          owl:someValuesFrom ex:author
                        ] .
}
```

# Q3. Find all properties whose domain is either Conference or Journal
```
PREFIX ex: <http://www.semanticweb.org/danicantabella/ontologies/2023/4/SDM_Lab3/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT DISTINCT ?property
WHERE {
  {?property rdf:type owl:ObjectProperty ;
            rdfs:domain [ rdf:type owl:Restriction ;
                          owl:onProperty ?property_domain ;
                          owl:someValuesFrom ex:conference
                        ] .
    }
    UNION
    {?property rdf:type owl:ObjectProperty ;
            rdfs:domain [ rdf:type owl:Restriction ;
                          owl:onProperty ?property_domain ;
                          owl:someValuesFrom ex:journal
                        ] . 
    }
}
```

# Q4. Find all the papers written by a given author that where published in database conferences.
```
PREFIX ex: <http://www.semanticweb.org/danicantabella/ontologies/2023/4/SDM_Lab3/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?papers ?proceedings ?conference
WHERE {
    ?author ex:name_human "Firman Suryadi".
    ?author ex:writes ?papers.
    ?papers ex:includedInProceeding ?proceedings.
    ?proceedings ex:fromConference ?conference.
    ?conference ex:conferenceRelatedTo ex:database
}
```
