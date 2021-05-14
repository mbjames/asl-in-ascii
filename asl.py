import asl_images
import menu
import banner


def back():
    menu.back_menu()

    answer = input("\n > ").lower()

    if answer == "y":
        start()

    elif answer == "n":
        exit()

    else:
        menu.invalid()

        back()


def start():
    banner.print_banner()

    menu.main_menu()

    answer = input("\n > ").lower()

    if answer == "quit":
        exit()

    elif answer == "a":
        asl_images.letter_a()

        back()

    elif answer == "b":
        asl_images.letter_b()

        back()

    elif answer == "c":
        asl_images.letter_c()

        back()

    elif answer == "d":
        asl_images.letter_d()

        back()

    elif answer == "e":
        asl_images.letter_e()

        back()

    elif answer == "f":
        asl_images.letter_f()

        back()

    elif answer == "g":
        asl_images.letter_g()

        back()

    elif answer == "h":
        asl_images.letter_h()

        back()

    elif answer == "i":
        asl_images.letter_i()

        back()

    elif answer == "j":
        asl_images.letter_j()

        back()

    elif answer == "k":
        asl_images.letter_k()

        back()

    elif answer == "l":
        asl_images.letter_l()

        back()

    elif answer == "m":
        asl_images.letter_m()

        back()

    elif answer == "n":
        asl_images.letter_n()

        back()

    elif answer == "o":
        asl_images.letter_o()

        back()

    elif answer == "p":
        asl_images.letter_p()

        back()

    elif answer == "q":
        asl_images.letter_q()

        back()

    elif answer == "r":
        asl_images.letter_r()

        back()

    elif answer == "s":
        asl_images.letter_s()

        back()

    elif answer == "t":
        asl_images.letter_t()

        back()

    elif answer == "u":
        asl_images.letter_u()

        back()

    elif answer == "v":
        asl_images.letter_v()

        back()

    elif answer == "w":
        asl_images.letter_w()

        back()

    elif answer == "x":
        asl_images.letter_x()

        back()

    elif answer == "y":
        asl_images.letter_y()

        back()

    elif answer == "z":
        asl_images.letter_z()

        back()

    else:
        menu.invalid()

        start()


start()
