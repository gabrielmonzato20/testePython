import re


class CustomerValidate():

    def __init__(self,data):
        self.data = data
    def cpfValidate(self):
        cpf=self.data['cpf']
        if not isinstance(cpf, str):
            raise Exception("Invalid cpf")

            # Remove some unwanted characters
        cpf = re.sub("[^0-9]", '', cpf)

        # Verify if CPF number is equal
        if cpf == '00000000000' or cpf == '11111111111' \
                or cpf == '22222222222' or cpf == '33333333333' \
                or cpf == '44444444444' or cpf == '55555555555' \
                or cpf == '66666666666' or cpf == '77777777777' \
                or cpf == '88888888888' or cpf == '99999999999':
            raise Exception("Invalid cpf")
        # Checks if string has 11 characters
        if len(cpf) != 11:
            raise Exception("Invalid cpf")
        sum = 0
        weight = 10

        """ Calculating the first cpf check digit. """
        for n in range(9):
            sum = sum + int(cpf[n]) * weight

            # Decrement weight
            weight = weight - 1

        verifyingDigit = 11 - sum % 11

        if verifyingDigit > 9:
            firstVerifyingDigit = 0
        else:
            firstVerifyingDigit = verifyingDigit

        """ Calculating the second check digit of cpf. """
        sum = 0
        weight = 11
        for n in range(10):
            sum = sum + int(cpf[n]) * weight

            # Decrement weight
            weight = weight - 1

        verifyingDigit = 11 - sum % 11

        if verifyingDigit > 9:
            secondVerifyingDigit = 0
        else:
            secondVerifyingDigit = verifyingDigit

        if cpf[-2:] == "%s%s" % (firstVerifyingDigit, secondVerifyingDigit):
            return True
        raise Exception("Invalid cpf")
    def start(self):
        self.cpfValidate()