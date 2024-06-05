import os


def try_to_convert_to_int(number):
    try:
        number_float = float(number)
        if number_float.is_integer():
            return int(number_float)
        else:
            return number_float
    except ValueError:
        return float(number)


def inpit_pairs_selection():
    while True:
        try:
            print("Choose the quation:")
            input_selection = int(
                input("1) Hand input \n2) From function\n3) File input\n")
            )
            if input_selection in range(1, 4):
                break
            print("Invalid command")
            continue
        except ValueError:
            print("Incorrect value entered")
            continue
    switch_command = {
        1: pairs_input_hand,
        2: pairs_from_function,
        3: pairs_input_file,
    }
    pairs, x = switch_command.get(input_selection, exit)()
    return pairs, x


def pairs_from_function():
    quation = choose_quation()
    a = choose_left_interval()
    b = choose_right_interval(a)
    n = choose_n()
    x = choose_x(a, b)

    stp = (b - a) / (n - 1)
    points = [(a + i * stp, fun(quation, a + i * stp)) for i in range(n)]
    return points, x


def fun(quation, x):
    if quation == 1:
        return x**2 - 3 * x + 2
    elif quation == 2:
        return x**3 + 2 * x**2 - 5
    else:
        return x


def pairs_input_hand():
    pairs = []
    i = 1
    while i <= 12:
        try:
            temp = (
                input(f"Enter pair {i} x and y. For stop enter end:\n")
                .strip()
                .replace(",", ".")
                .split(" ")
            )
            if temp == ["end"] and i >= 3:
                i += 1
                break
            elif temp == ["end"] and i < 3:
                print("Minimum 3 pairs, please add more")
                i += 1
                continue
            x, y = map(float, temp)
            i += 1

        except ValueError:
            print("Incorrect value entered")
            continue
        pair = [x, y]
        pairs.append(pair)
    print(f"Entered {i-1} pairs")
    a = min([dot[0] for dot in pairs])
    b = max([dot[0] for dot in pairs])
    x = choose_x(a, b)
    return pairs, x


def choose_left_interval():
    while True:
        try:
            interval = input("Enter the left boundary of the interval: ").replace(
                ",", "."
            )
            interval = int(interval)
            return try_to_convert_to_int(interval)

        except ValueError:
            try:
                interval = try_to_convert_to_int(interval)
                return interval
            except ValueError:
                print("Incorrect number entered")
            continue

        except UnboundLocalError:
            print("Incorrect number entered")
            continue


def choose_right_interval(a):
    while True:
        try:
            interval = input("Enter the right boundary of the interval: ").replace(
                ",", "."
            )
            if float(interval) - float(a) - 0.00001 < 0:
                print("The right boundary must be greater than the left boundary!")
                continue
            interval = int(interval)
            return try_to_convert_to_int(interval)

        except ValueError:
            try:
                interval = try_to_convert_to_int(interval)
                return interval
            except ValueError:
                print("Incorrect number entered")
            continue

        except UnboundLocalError:
            print("Incorrect number entered")
            continue


def choose_x(a, b):
    while True:
        try:
            interval = input("Enter the x value: ").replace(",", ".")
            interval = int(interval)
            if a <= interval <= b:
                return try_to_convert_to_int(interval)
            else:
                print(f"x must be in interval from {a} to {b}")
                continue

        except ValueError:
            try:
                interval = try_to_convert_to_int(interval)
                return interval
            except ValueError:
                print("Incorrect number entered")
            continue

        except UnboundLocalError:
            print("Incorrect number entered")
            continue


def choose_n():
    while True:
        try:
            interval = input("Enter the N value: ").replace(",", ".")
            interval = int(interval)
            return try_to_convert_to_int(interval)

        except ValueError:
            print("Incorrect number entered")
            continue

        except UnboundLocalError:
            print("Incorrect number entered")
            continue


def choose_quation():
    while True:
        try:
            print("Choose the quation:")
            input_quation = int(input("1) x^2 - 3x + 2 \n2) x^3 + 2x^2 - 5\n3) x\n"))
            if input_quation in range(1, 4):
                break
            print("Invalid command")
            continue
        except ValueError:
            print("Incorrect value entered")
            continue
    return input_quation


def pairs_input_file():
    current_working_directory = os.path.dirname(__file__)
    file_name = input("Enter the relative path to your file\n")
    print()
    file_path = os.path.join(current_working_directory, file_name)
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if len(lines) >= 4 and len(lines) <= 13:
        pairs = []
        for line in lines:
            try:
                if line == lines[0]:
                    main_x = try_to_convert_to_int(line.replace(",", "."))
                    continue
                var = line.replace(",", ".").split(" ")
                x, y = map(float, var)
                x = try_to_convert_to_int(x)
                y = try_to_convert_to_int(y)
                pair = [x, y]
                pairs.append(pair)
            except ValueError:
                print("Incorrect data in the specified file")
                exit()

            except UnboundLocalError:
                print("Incorrect data in the specified file")
                exit()
            continue

    else:
        print("Uncorrect count of lines in the specified file")
        exit()
    if min([dot[0] for dot in pairs]) <= main_x <= max([dot[0] for dot in pairs]):
        print(f"Readed x={main_x}")
        print(f"Readed {len(pairs)} pairs")
        for pair in pairs:
            print(f"pair[{pair[0]}, {pair[1]}]")
        print("\n\n")
        return pairs, main_x
    else:
        print("Incorrect X in the specified file")
        exit()
