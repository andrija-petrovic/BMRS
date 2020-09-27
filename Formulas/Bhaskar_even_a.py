"""Bhaskar: even-numbered 'a' is turned to 'b'. Insert a final 'c' if word is even, otherwise insert a 'd'. """

def personal_setup(self):
    self.labels_list = list('abcd#%')
    self.copyset = [1,2]
    self.labels_are_input=True


def personal_predicate_setup(self):
    return


def personal_features(self):
    return

def personal_Output_Formula(self, copy, label, domain_element):
    pred = self.input_to_functions['pred'].get(domain_element)
    succ = self.input_to_functions['succ'].get(domain_element)

    if copy is 1 and label is 'a':
        if self.input_to_labels['a'].get(domain_element):
            if pred is 0:
                return True
            else:
                return self.get_output_value(1, 'b', pred)
        else:
            return False
    if copy is 1 and label is 'b':
        if self.input_to_labels['a'].get(domain_element):
            return self.get_output_value(1, 'a', pred)
        else:
            return False
    if copy == 1 and label == 'c':
        if domain_element == len(self.word) - 1:
            return self.get_output_value(1, 'b', pred)
        else:
            return False
    if copy == 1 and label == 'd':
        if domain_element == len(self.word) - 1:
            return self.get_output_value(1, 'a', pred)
        else:
            return False
    if copy == 2 and label == 'b':
        if self.input_to_labels['a'].get(domain_element):
            return self.get_output_value(1, 'a', pred)
        else:
            return False
    if copy == 2 and label in ['a','c','d']: return False

def personal_Predicate_Formula(self,predicate,domain_element):
    return