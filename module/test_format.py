

query_string = "MATCH (p1{EntityId: '%s'}),(p2{EntityId: '%s'}),p=shortestpath((p1)-[*..10]-(p2)) RETURN p"

start_entity = "CPS_businessMod4"

entity = "CPS_sysFun3"

cql = query_string % (start_entity, entity)
print(cql)