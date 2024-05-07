def print_linear(answers):
    fi = "fi ="
    ei = "ei ="
    for num in answers[3]:
        fi += f" {num},"
    for num in answers[4]:
        ei += f" {num},"
    pi = "Pi ="
    for num in answers[6]:
        pi += f" {num},"
    pirson = answers[5]
    print(
        f"Linear\n{answers[2]}\n{fi}\nPirson = {pirson}\nS = {answers[1]}\nS2 = {answers[0]}\n{ei}\n{pi}"
    )


def print_sqr(answers):
    fi = "fi ="
    ei = "ei ="
    for num in answers[3]:
        fi += f" {num},"
    for num in answers[4]:
        ei += f" {num},"
    pi = "Pi ="
    for num in answers[5]:
        pi += f" {num},"
    print(
        f"Quadratic\n{answers[2]}\n{fi}\n\nS = {answers[1]}\nS2 = {answers[0]}\n{ei}\n{pi}"
    )


def print_qubic(answers):
    fi = "fi ="
    ei = "ei ="
    for num in answers[3]:
        fi += f" {num},"
    for num in answers[4]:
        ei += f" {num},"
    print(f"Qubic\n{answers[2]}\n{fi}\nS = {answers[1]}\nS2 = {answers[0]}\n{ei}")


def print_log(answers):
    fi = "fi ="
    ei = "ei ="
    for num in answers[3]:
        fi += f" {num},"
    for num in answers[4]:
        ei += f" {num},"
    pi = "Pi ="
    for num in answers[6]:
        pi += f" {num},"
    pirson = answers[5]
    print(
        f"Logarithmic\n{answers[2]}\n{fi}\nPirson = {pirson}\nS = {answers[1]}\nS2 = {answers[0]}\n{ei}\n{pi}"
    )


def print_exp(answers):
    fi = "fi ="
    ei = "ei ="
    for num in answers[3]:
        fi += f" {num},"
    for num in answers[4]:
        ei += f" {num},"
    pi = "Pi ="
    for num in answers[6]:
        pi += f" {num},"
    pirson = answers[5]
    print(
        f"Exp\n{answers[2]}\n{fi}\nPirson = {pirson}\nS = {answers[1]}\nS2 = {answers[0]}\n{ei}\n{pi}"
    )


def print_gradual(answers):
    fi = "fi ="
    ei = "ei ="
    for num in answers[3]:
        fi += f" {num},"
    for num in answers[4]:
        ei += f" {num},"
    pi = "Pi ="
    for num in answers[6]:
        pi += f" {num},"
    pirson = answers[5]
    print(
        f"Gradual\n{answers[2]}\n{fi}\nPirson = {pirson}\nS = {answers[1]}\nS2 = {answers[0]}\n{ei}\n{pi}"
    )


def find_best_method(answers):
    min = 99999
    for answer in answers:
        try:
            if answer[0] < min:
                min = answer[0]
            print(answer[2], end="zz")
        except TypeError:
            continue
    print("space")
    for answer in answers:
        try:
            if answer[0] == min:
                print(f"Best quation is {answer[2]} with S2 = {answer[0]}")
                break
        except TypeError:
            continue
