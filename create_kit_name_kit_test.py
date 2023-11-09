def get_kit_body(name):
    kit_body = {
        "name": name,

    }
    return kit_body


def get_new_user_token():

    pass


def test_positive_assert_1():
    # Escenario 1: El número permitido de caracteres (1)
    kit_body = get_kit_body("a")

def test_positive_assert_2():
    # Escenario 2: El número permitido de caracteres (511)
    kit_body = get_kit_body('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')

def test_negative_assert_3():
    # Escenario 3: El número de caracteres es menor que la cantidad permitida (0)
    kit_body = get_kit_body("")

def test_negative_assert_4():
    # Escenario 4: El número de caracteres es mayor que la cantidad permitida (512)
    kit_body = get_kit_body('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD')

def test_negative_assert_5():
    # Escenario 5: Se permiten caracteres especiales
    kit_body = get_kit_body("*%@,")

def test_negative_assert_6():
    # Escenario 6: Se permiten espacios
    kit_body = get_kit_body('A Aaa')

def test_negative_assert_7():
    # Esceneario 7: Se permiten números
    kit_body = get_kit_body(123)

def test_negative_assert_8():
    # Escenario 8: El parámetro no se pasa en la solicitud
    kit_body = get_kit_body(None)

def test_negative_assert_9():
    # Escenario 9: Se ha pasado un tipo de parámetro diferente (número)
    kit_body = get_kit_body(123)


    if __name__ == '__main__':
        print('pass')


