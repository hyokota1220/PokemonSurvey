#Python Practice
#Pokemon Survey

def question1(char, bul, squ):
    
    temp = 0
    
    while temp != 1:
        print("\nQuestion No.1: What is your favorite color?\n")
        print("\t1. Red    2. Green    3. Blue\n")
        ans2 = int(input("Your Choice: "))

        #Selecting
        if ans2 == 1:
            char += 1
            temp = 1
        elif ans2 == 2:
            bul += 1
            temp = 1
        elif ans2 == 3:
            squ += 1
            temp = 1
        else:
            print("\nYou need to choose from 1-3")

    return char, bul, squ

def question2(char, bul, squ):
    
    temp = 0
    
    while temp != 1:
        print("\nQuestion No.2: What is your favorite number?\n")
        print("\t1. One    2. Two    3. Three\n")
        ans2 = int(input("Your Choice: "))

        #Selecting
        if ans2 == 1:
            char += 1
            temp = 1
        elif ans2 == 2:
            bul += 1
            temp = 1
        elif ans2 == 3:
            squ += 1
            temp = 1
        else:
            print("\nYou need to choose from 1-3")

    return char, bul, squ

def question3(char, bul, squ):
    
    temp = 0
    
    while temp != 1:
        print("\nQuestion No.3: Which place would you spend rest of your life?\n")
        print("\t1. Hot Island    2. Beach Mansion    3. Tree House\n")
        ans2 = int(input("Your Choice: "))

        #Selecting
        if ans2 == 1:
            char += 1
            temp = 1
        elif ans2 == 2:
            bul += 1
            temp = 1
        elif ans2 == 3:
            squ += 1
            temp = 1
        else:
            print("\nYou need to choose from 1-3")

    return char, bul, squ

def question4(char, bul, squ):
    
    temp = 0
    
    while temp != 1:
        print("\nQuestion No.4: What is your favorite season?\n")
        print("\t1. Summer    2. Winter    3. Fall or Spring\n")
        ans2 = int(input("Your Choice: "))

        #Selecting
        if ans2 == 1:
            char += 1
            temp = 1
        elif ans2 == 2:
            bul += 1
            temp = 1
        elif ans2 == 3:
            squ += 1
            temp = 1
        else:
            print("\nYou need to choose from 1-3")

    return char, bul, squ

def question5(char, bul, squ):
    
    temp = 0
    
    while temp != 1:
        print("\nQuestion No.5: What is your favorite food?\n")
        print("\t1. BBQ    2. Ramen    3. Salad\n")
        ans2 = int(input("Your Choice: "))

        #Selecting
        if ans2 == 1:
            char += 1
            temp = 1
        elif ans2 == 2:
            bul += 1
            temp = 1
        elif ans2 == 3:
            squ += 1
            temp = 1
        else:
            print("\nYou need to choose from 1-3")

    return char, bul, squ

def calculatePoints(char, bul, squ):
    print("\nScore for possible pokemons\n")
    print("\nCharmander =", char, "\n")
    print("\nBulbasaur =", bul, "\n")
    print("\nSquirtle =", squ, "\n")

    if (char > bul and char > squ) or (char > bul and char < squ) or (bul > char and bul > squ) or (bul > char and bul < squ) or (squ > char and squ > bul) or (squ > char and squ < bul) or char == bul or char == squ or bul == squ:
            if (char > bul and char > squ):
                print("\nYou're Charmander!!!\n\n")
                printCharmander()
            elif (char > bul and char < squ):
                print("\nYou're Squirtle!!!\n\n")
                printSquirtle()
            elif (bul > char and bul > squ):
                print("\nYou're Bulbasaur!!!\n\n")
                printBulbasaur()
            elif (bul > char and bul < squ):
                print("\nYou're are Squirlte!!!\n\n")
                printSquirtle()
            elif (squ > char and squ > bul):
                print("\nYou're Squirlte!!!\n\n")
                printSquirtle()
            elif (squ > char and squ < bul):
                print("\nYou're Bulbasaur")
                printBulbasaur()
            elif char == bul:
                print("\nYou're Charmander and Bulbasaur!!!\n\n")
                printCharmander()
                printBulbasaur()
            elif char == squ:
                print("\nYou're are Charmander and Squirlte!!!\n\n")
                printCharmander()
                printSquirtle()
            elif bul == squ:
                print("\nYou're Bulbasaur and Squirlte!!!\n\n")
                printBulbasaur()
                printSquirtle()

    return

def printCharmander():
    print("              _.--""`-.. ")
    print("            ,'          `. ")
    print("          ,'          __  `. ")
    print("         /|          ' __   \ ")
    print("        , |           / |.   . ")
    print("        |,'          !_.'|   | ")
    print("      ,'             '   |   | ")
    print("     /              |`--'|   | ")
    print("    |                `---'   | ")
    print("     .   ,                   |                       ,'. ")
    print("      ._     '           _'  |                    , ' \ ` ")
    print("  `.. `.`-...___,...---""    |       __,.        ,`'   L,| ")
    print("  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \ ")
    print("-:..     `. `-..--_.,.<       `'      / ''.        '-/ |   . ")
    print("  `,         ""''     `.              ,'         |   |  ',, ")
    print("    `.      '            '            /          '    |'. |/ ")
    print("      `.   |              \       _,-'           |       '' ")
    print("        `._'               \   ''\                .      | ")
    print("           |                '     \                `._  ,' ")
    print("           |                 '     \                 .'| ")
    print("           |                 .      \                | | ")
    print("           |                 |       L              ,' | ")
    print("           `                 |       |             /   ' ")
    print("            \                |       |           ,'   / ")
    print("          ,' \               |  _.._ ,-..___,..-'    ,' ")
    print("         /     .             .      `!             ,j' ")
    print("        /       `.          /        .           .'/ ")
    print("       .          `.       /         |        _.'.' ")
    print("        `.          7`'---'          |------''_.' ")
    print("       _,.`,_     _'                ,''-----'' ")
    print("   _,-_    '       `.     .'      ,\ ")
    print("   -' /`.         _,'     | _  _  _.| ")
    print("    '--'---""''''        `' '! |! / ")
    print("                            `" " -' mh\n\n\n")

    return

def printBulbasaur():
    print("                                           /")
    print("                        _,.------....___,.' ',.-.")
    print("                     ,-'          _,.--'        |")
    print("                   ,'         _.-'              .")
    print("                  /   ,     ,'                   `")
    print("                 .   /     /                     ``.")
    print("                 |  |     .                       \.\ ")
    print("       ____      |___._.  |       __               \ `.")
    print("     .'    `---""       ``'-.--'''`  \               .  \ ")
    print("    .  ,            __               `              |   .")
    print("    `,'         ,-''  .               \             |    L")
    print("   ,'          '    _.'                -._          /    |")
    print("  ,`-.    ,'.   `--'                      >.      ,'     |")
    print(" . .'\'   `-'       __    ,  ,-.         /  `.__.-      ,'")
    print(" ||:, .           ,'  ;  /  / \ `        `.    .      .'/")
    print(" j|:D  \          `--'  ' ,'_  . .         `.__, \   , /")
    print("/ L:_  |                 .  '' :_;                `.'.'")
    print(".    ""'                  '""''                    V")
    print(" `.                                 .    `.   _,..  `")
    print("   `,_   .    .                _,-'/    .. `,'   __  `")
    print("    ) \`._        ___....----''  ,'   .'  \ |   '  \  .")
    print("   /   `. '`-.--'''         _,' ,'     `---' |    `./  |")
    print("  .   _  `''--.._____..--'   ,             '         |")
    print("  | .' `. '-.                /-.           /          ,")
    print("  | `._.'    `,_            ;  /         ,'          .")
    print(" .'          /| `-.        . ,'         ,           ,")
    print(" '-.__ __ _,','    '`-..___;-...__   ,.'\ ____.___.'")
    print(" `'^--'..'   '-`-^-''--    `-^-'`.''""''`.,^.`.--' mh\n\n\n")

    return

def printSquirtle():
    print("               _,........__")
    print("            ,-'            '`-.")
    print("          ,'                   `-.")
    print("        ,'                        \ ")
    print("      ,'                           .")
    print("      .'\               ,"".       `")
    print("     ._.'|             / |  `       \ ")
    print("     |   |            `-.'  ||       `.")
    print("     |   |            '-._,'||       | \ ")
    print("     .`.,'             `..,'.'       , |`-.")
    print("     l                       .'`.  _/  |   `.")
    print("     `-.._'-   ,          _ _'   -' \  .     `")
    print("`.'""''-.`-...,---------','         `. `....__.")
    print(".'        `'-..___      __,'\          \  \     \ ")
    print("\_ .          |   `''''    `.           . \     \ ")
    print("  `.          |              `.          |  .     L")
    print("    `.        |`--...________.'.        j   |     |")
    print("      `._    .'      |          `.     .|   ,     |")
    print("         `--,\       .            `7""' |  ,      |")
    print("            ` `      `            /     |  |      |    _,-'""'`-.")
    print("             \ `.     .          /      |  '      |  ,'          `.")
    print("              \  v.__  .        '       .   \    /| /              \ ")
    print("               \/    `''\ ''''''`.       \   \  /.''                | ")
    print("                `        .        `._ ___,j.  `/ .-       ,---.     |")
    print("                ,`-.      \         .'     `.  |/        j     `    | ")
    print("               /    `.     \       /         \ /         |     /    j")
    print("              |       `-.   7-.._ .          |'          '         /")
    print("              |          `./_    `|          |            .     _,'")
    print("              `.           / `----|          |-............`---'")
    print("                \          \      |          |")
    print("               ,'           )     `.         |")
    print("                7____,,..--'      /          |")
    print("                                  `---.__,--.'mh\n\n\n")

    return 

print("\n-------------------------------------------------------------------------------------")
print("\n\t\tAnswer these questions and see what pokemon you are\n\n")
print("\n\t                                  ,'\ ")
print("\t    _.----.        ____         ,'  _\   ___    ___     ____")
print("\t_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.")
print("\t\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
print("\t \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
print("\t   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
print("\t    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
print("\t     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
print("\t      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
print("\t       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
print("\t        \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
print("\t                                `'                            '-._|\n")
print("--------------------------------------------------------------------------------------\n")
ans1 = input("Press S to start or Q to quit: ")

if ans1 == 'S' or ans1 == 's':
    ans2 = 'S'
    while ans2 != 'N':
        char = 0
        bul = 0
        squ = 0

        #Question 1
        char, bul, squ = question1(char, bul, squ)

        #Question 2
        char, bul, squ = question2(char, bul, squ)

        #Question 3
        char, bul, squ = question3(char, bul, squ)

        #Question 4
        char, bul, squ = question4(char, bul, squ)

        #Question 5
        char, bul, squ = question5(char, bul, squ)

    
        calculatePoints(char, bul, squ)

        ans2 = input("Would you like to continue? Y/N: ")
    
    print("\n--------------------------------------------------------------------")
    print("\n\t\t\tShutting down...\n")
    print("--------------------------------------------------------------------\n")

elif answer1 == 'Q' or answer1 == 'q':
    print("\n--------------------------------------------------------------------")
    print("\n\t\t\tShutting down...\n")
    print("--------------------------------------------------------------------\n")

else:
    print("Invalid")

