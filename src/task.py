import random


def extract_attributes(array):
    attributes = array[0]
    array.pop(0)

    return attributes


def random_select_evidences(dataset, attributes):
    sample_attributes = random_select_attributes(attributes)
    sample_evidences = []

    for a in sample_attributes:
        attribute_position = attributes.index(a)
        evidences_by_attribute = set()

        for register in dataset:
            evidences_by_attribute.add(register[attribute_position])

        s = random.sample(evidences_by_attribute, 1)
        sample_evidences.extend(s)

    print('Attributes:', sample_attributes)
    print('Evidences:', sample_evidences)

    return sample_evidences


def random_select_attributes(attributes):
    amount = random.randint(1, len(attributes) - 2)
    sample_attributes = []

    s = random.sample(attributes[1: len(attributes) - 1], amount)  # 'amount' attributes without replacement
    sample_attributes.extend(s)

    return sample_attributes