uppercase = 'A-Z'
number = '0-9'
lowercase = 'a-z'
specialCharacter = '-!¡@#$%^&*()_+{}[]:;<>,.¿?~\\/='

statusFinal = 'q59'

transitions = {
    'q0': {uppercase: 'q1', lowercase: 'q2', number: 'q3', specialCharacter: 'q4'},
    'q1': {uppercase: 'q1', lowercase: 'q40', number: 'q41', specialCharacter: 'q44'},
    'q2': {uppercase: 'q11', lowercase: 'q2', number: 'q12', specialCharacter: 'q10'},
    'q3': {uppercase: 'q8', lowercase: 'q13', number: 'q3', specialCharacter: 'q9'},
    'q4': {uppercase: 'q5', lowercase: 'q6', number: 'q7', specialCharacter: 'q4'},
    'q5': {uppercase: 'q5', lowercase: 'q29', number: 'q28', specialCharacter: 'q5'},
    'q6': {uppercase: 'q32', lowercase: 'q6', number: 'q33', specialCharacter: 'q6'},
    'q7': {uppercase: 'q36', lowercase: 'q37', number: 'q7', specialCharacter: 'q7'},
    'q8': {uppercase: 'q8', lowercase: 'q51', number: 'q8', specialCharacter: 'q50'},
    'q9': {uppercase: 'q57', lowercase: 'q56', number: 'q9', specialCharacter: 'q9'},
    'q10': {uppercase: 'q31', lowercase: 'q10', number: 'q14', specialCharacter: 'q10'},
    'q11': {uppercase: 'q11', lowercase: 'q11', number: 'q18', specialCharacter: 'q17'},
    'q12': {uppercase: 'q22', lowercase: 'q12', number: 'q12', specialCharacter: 'q21'},
    'q13': {uppercase: 'q53', lowercase: 'q13', number: 'q13', specialCharacter: 'q54'},
    'q14': {uppercase: 'q59', lowercase: 'q14', number: 'q14', specialCharacter: 'q14'},
    'q17': {uppercase: 'q17', lowercase: 'q17', number: 'q59', specialCharacter: 'q17'},
    'q18': {uppercase: 'q18', lowercase: 'q18', number: 'q18', specialCharacter: 'q59'},
    'q21': {uppercase: 'q59', lowercase: 'q21', number: 'q21', specialCharacter: 'q21'},
    'q22': {uppercase: 'q22', lowercase: 'q22', number: 'q22', specialCharacter: 'q59'},
    'q28': {uppercase: 'q28', lowercase: 'q59', number: 'q28', specialCharacter: 'q28'},
    'q29': {uppercase: 'q29', lowercase: 'q29', number: 'q59', specialCharacter: 'q29'},
    'q31': {uppercase: 'q31', lowercase: 'q31', number: 'q59', specialCharacter: 'q31'},
    'q32': {uppercase: 'q32', lowercase: 'q32', number: 'q59', specialCharacter: 'q32'},
    'q33': {uppercase: 'q59', lowercase: 'q33', number: 'q33', specialCharacter: 'q33'},
    'q36': {uppercase: 'q36', lowercase: 'q59', number: 'q36', specialCharacter: 'q36'},
    'q37': {uppercase: 'q59', lowercase: 'q37', number: 'q37', specialCharacter: 'q37'},
    'q40': {uppercase: 'q40', lowercase: 'q40', number: 'q45', specialCharacter: 'q43'},
    'q41': {uppercase: 'q41', lowercase: 'q49', number: 'q41', specialCharacter: 'q42'},
    'q42': {uppercase: 'q42', lowercase: 'q59', number: 'q42', specialCharacter: 'q42'},
    'q43': {uppercase: 'q43', lowercase: 'q43', number: 'q59', specialCharacter: 'q43'},
    'q44': {uppercase: 'q44', lowercase: 'q46', number: 'q47', specialCharacter: 'q44'},
    'q45': {uppercase: 'q45', lowercase: 'q45', number: 'q45', specialCharacter: 'q59'},
    'q46': {uppercase: 'q46', lowercase: 'q46', number: 'q59', specialCharacter: 'q46'},
    'q47': {uppercase: 'q47', lowercase: 'q59', number: 'q47', specialCharacter: 'q47'},
    'q49': {uppercase: 'q49', lowercase: 'q49', number: 'q49', specialCharacter: 'q59'},
    'q50': {uppercase: 'q50', lowercase: 'q59', number: 'q50', specialCharacter: 'q50'},
    'q51': {uppercase: 'q51', lowercase: 'q51', number: 'q51', specialCharacter: 'q59'},
    'q53': {uppercase: 'q53', lowercase: 'q53', number: 'q53', specialCharacter: 'q59'},
    'q54': {uppercase: 'q59', lowercase: 'q54', number: 'q54', specialCharacter: 'q54'},
    'q56': {uppercase: 'q59', lowercase: 'q56', number: 'q56', specialCharacter: 'q56'},
    'q57': {uppercase: 'q57', lowercase: 'q57', number: 'q57', specialCharacter: 'q57'},
    'q59': {uppercase: 'q59', lowercase: 'q59', number: 'q59', specialCharacter: 'q59'}
}


def validateAlphabet(character):
    inputChain = ''
    if character.isupper():
        inputChain = uppercase
    elif character.islower():
        inputChain = lowercase
    elif character.isdigit():
        inputChain = number
    elif character in specialCharacter:
        inputChain = specialCharacter
    return inputChain


def accepted(chain):
    status = 'q0'
    for character in chain:
        inputChain = validateAlphabet(character)
        print("chain: " + inputChain)
        if inputChain in transitions[status]:
            status = transitions[status][inputChain]
            print("status: " + status)
            print(transitions[status])
        else:
            return False  # El caracter no es válido.
    return status in {statusFinal}


testInput = 0
while testInput == 0:
    password = input('Ingresa una contraseña segura : ')
    if accepted(password):
        print('\t La cadena es aceptada.')
    else:
        print('\t La cadena no es aceptada.')
