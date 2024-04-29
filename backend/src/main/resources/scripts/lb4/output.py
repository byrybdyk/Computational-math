def print_linear(answers):
    fi = "fi ="
    ei = "ei ="
    for num in answers[2]:
        fi += f" {num},"
    for num in answers[3]:
        ei += f" {num},"
    pi = "Pi ="
    for num in answers[5]:
        pi += f" {num},"
    pirson = answers[4]
    print(f"{answers[1]}\n{fi}\nPirson = {pirson}\nS = {answers[0]}\n{ei}\n{pi}")
