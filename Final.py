game = str(input("Which size do you want to play? [3x3] = 3x3; [5x5] = 5x5; [7x7] = 7x7   "))
while True:
    match game:
        case "3x3":
            import 3x3
            3x3.version_3x3()
        case "5x5":
            import 5x5
            5x5.version_5x5()
        case "7x7":
            import 7x7
            7x7.version_7x7()
