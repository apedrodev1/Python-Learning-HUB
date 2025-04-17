def validate_quantity(value):
    try:
        quantity = int(value)
        if quantity > 0:
            return quantity
    except ValueError:
        pass  # Não faz nada, deixa seguir para retornar None
    return None


def validate_calculation_type(value):
    try:
        value = value.strip()
        if value in ["0", "1"]:
            return value
    except Exception:
        pass
    return None



def validate_grade(value):
    try:
        grade = float(value)
        if 0 <= grade <= 10:
            return grade
        else:
            return None
    except ValueError:
        return None
    


def validate_weights(weights_input):
    try:
        weights = [float(w) for w in weights_input.split()]
        if all(0 <= w <= 10 for w in weights):  # Verifica se todos os pesos estão entre 0 e 10
            return weights
        return None
    except ValueError:
        return None




def validate_names(name):
     cleaned = name.strip().capitalize()
     if cleaned.replace(" ", "").isalpha(): #funcao editada
         return cleaned
     else:
         return None

