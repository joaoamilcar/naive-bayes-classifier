class NaiveBayes:


    def __init__(self, dataset, attributes):
        self.dataset = dataset
        self.attributes = attributes
        self.classes = self.get_classes()

    # a posteriori probability of a hypothesis: the probability of a hypothesis (event) after evidences are observed
    # @param hypothesis: a sample class from the decision attribute
    # @param evidences: one or more sample cases from different ordinary attributes
    def p_hypothesis_evidences(self, hypothesis, evidences):
        # we can ignore p_evidences(evidences) because we only need to “relatively” compare the value to other class
        return (self.p_evidences_hypothesis(evidences, hypothesis) * self.p_hypothesis(hypothesis)) #/ self.p_evidences(evidences)

    # a priori probability of a hypothesis: the probability of a hypothesis (event) before evidences are observed
    def p_hypothesis(self, hypothesis):
        hSuccess = 0
        hFail = 0

        for register in self.dataset:
            if register[len(register) - 1] == hypothesis:
                hSuccess += 1
            else:
                hFail += 1

        total = hSuccess + hFail

        return hSuccess / total

    # the probability that there is the evidence when hypothesis is succeeded
    def p_evidences_hypothesis(self, evidences, hypothesis):
        result = 1

        for e in evidences:
            attributeColumn = self.find_attribute_column_by_evidence(e)
            hSuccess = 0
            eFrequency = 0

            for register in self.dataset:
                if register[len(register) - 1] == hypothesis:
                    hSuccess += 1

                    if register[attributeColumn] == e:
                        eFrequency += 1

            result *= self.laplace_smoothing(attributeColumn, eFrequency, hSuccess)
            # result *= eFrequency / hSuccess

        return result

    # the probability of evidences occuring
    def p_evidences(self, evidences):
        pass

    # estimation technique for solving 'zero-frequency' problem
    def laplace_smoothing(self, attributeColumn, eFrequency, hSuccess):
        u = self.count_evidences_by_attribute_column(attributeColumn)
        p_evidence =  1 / u # by assuming that all evidences are equally distributed

        result = (eFrequency + u * p_evidence) / (hSuccess + u)

        return result

    def run(self, evidences):
        nb_dict = {}

        for c in self.classes:
            nb_dict[c] = self.p_hypothesis_evidences(c, evidences)

        return nb_dict

    @staticmethod
    def probabilities_by_normalization(nb_dict):
        denominator = 0

        for key, value in nb_dict.items():
            denominator += value

        for key, value in nb_dict.items():
            print('Class', key, ': P(C) =', value / denominator)

    def generate_model(self):
        print('=== Classifier model (full training set) ===')
        print('Naive Bayes (simple)')
        print('')

        for c in self.classes:
            print('Class', c, ': P(C) =', self.p_hypothesis(c))
            print('')

            for a in self.attributes[1 : len(self.attributes) - 1]:
                evidences = self.get_evidences_by_attribute(a)

                print('Attribute', a)
                print(evidences)

                for e in evidences:
                    print(self.p_evidences_hypothesis([e], c), end=" ")

                print('')

            print('')

    def get_classes(self):
        classes = set()

        for register in self.dataset:
            classes.add(register[len(register) - 1])

        return classes

    def get_evidences_by_attribute(self, attribute):
        evidences = set()
        attributeColumn = self.attributes.index(attribute)

        for register in self.dataset:
            evidences.add(register[attributeColumn])

        return evidences

    def count_evidences_by_attribute_column(self, attributeColumn):
        evidences = set()

        for register in self.dataset:
            evidences.add(register[attributeColumn])

        return len(evidences)

    def find_attribute_column_by_evidence(self, evidence):
        for register in self.dataset:
            for position in range(1, len(register) - 1):
                if register[position] == evidence:
                    return position
