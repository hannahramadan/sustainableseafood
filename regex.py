import re

alias = "<a href=\"\/species-aliases\/black-cod\" typeof=\"skos:Concept\" property=\"rdfs:label skos:prefLabel\" datatype=\"\">Black cod<\/a>, <a href=\"\/species-aliases\/butterfish\" typeof=\"skos:Concept\" property=\"rdfs:label skos:prefLabel\" datatype=\"\">Butterfish<\/a>, <a href=\"\/species-aliases\/skil\" typeof=\"skos:Concept\" property=\"rdfs:label skos:prefLabel\" datatype=\"\">Skil<\/a>, <a href=\"\/species-aliases\/beshow\" typeof=\"skos:Concept\" property=\"rdfs:label skos:prefLabel\" datatype=\"\">Beshow<\/a>, <a href=\"\/species-aliases\/coalfish\" typeof=\"skos:Concept\" property=\"rdfs:label skos:prefLabel\" datatype=\"\">Coalfish<\/a>"

pattern = "<a href.*?>"


remove_ahref = re.sub("<a href.*?>", "", alias)

remove_atag = re.sub("<..a>", "", remove_ahref)

print(remove_atag)

x = remove_atag.split(", ")
print(x)


# for item in remove_ahref:
    

# "\">
# <\/a>

# .+ for name

# res = re.findall(remove_ahref, alias)

# for match in res:
#     print(match)

