import time


# Displays "GET A JOB" as ascii-art
# @param speed: how fast to build up the startup-message, in seconds
def title_ascii_art(speed):
    print("//===   ||====  =======         //\\\\             ||  //===\\\\  ||==\\\\")
    time.sleep(speed)
    print("||      ||         ||          //  \\\\            ||  ||   ||  ||  ||")
    time.sleep(speed)
    print("|| ===  ||===      ||         //====\\\\           ||  ||   ||  ||==<")
    time.sleep(speed)
    print("||  ||  ||         ||        //      \\\\      ||  //  ||   ||  ||  ||")
    time.sleep(speed)
    print("\\\\==//  ||====     ||       //        \\\\     \\\\===   \\\\===//  ||==//")
    time.sleep(speed)
    print("")
    time.sleep(speed)
    print("Welcome to get a job. Here you try to get your job of choice by learning new skills in different fields of study.")

title_ascii_art(0.15)
