# %%
ontology = {
    "Dog": {"is_a": "Mammal", "eats": "Food", "has": "Owner"},
    "Mammal": {"is_a": "Animal"},
}

def get_relations(entity):
    return ontology.get(entity, "No data found")

print(get_relations("Dog"))

# %%
print("hello")
# %%
