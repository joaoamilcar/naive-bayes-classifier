from customCsv import parse_to_array
from task import extract_attributes, random_select_evidences
from classifier import NaiveBayes


dataset = parse_to_array('jogarTenis.data')
attributes = extract_attributes(dataset)
nb = NaiveBayes(dataset, attributes)

print('=== Example ===')
random_evidences = random_select_evidences(dataset, attributes) # e.g.: ['Ensolarado', 'Fria', 'Forte']
nb_dictionary = nb.run(random_evidences)
probabilities = nb.probabilities_by_normalization(nb_dictionary)

print('')
nb.generate_model()