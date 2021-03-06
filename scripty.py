def main():
    tarot_deck = {
    0:"""
    $$$$$$$$\ $$\                       $$$$$$$$\                  $$\ 
    \__$$  __|$$ |                      $$  _____|                 $$ |
       $$ |   $$$$$$$\   $$$$$$\        $$ |    $$$$$$\   $$$$$$\  $$ |
       $$ |   $$  __$$\ $$  __$$\       $$$$$\ $$  __$$\ $$  __$$\ $$ |
       $$ |   $$ |  $$ |$$$$$$$$ |      $$  __|$$ /  $$ |$$ /  $$ |$$ |
       $$ |   $$ |  $$ |$$   ____|      $$ |   $$ |  $$ |$$ |  $$ |$$ |
       $$ |   $$ |  $$ |\$$$$$$$\       $$ |   \$$$$$$  |\$$$$$$  |$$ |
       \__|   \__|  \__| \_______|      \__|    \______/  \______/ \__|
    """,
    1:"""                                                   
    _/_/_/_/_/  _/                      _/      _/                      _/            _/                     
       _/      _/_/_/      _/_/        _/_/  _/_/    _/_/_/    _/_/_/        _/_/_/        _/_/_/  _/_/_/    
      _/      _/    _/  _/_/_/_/      _/  _/  _/  _/    _/  _/    _/  _/  _/        _/  _/    _/  _/    _/   
     _/      _/    _/  _/            _/      _/  _/    _/  _/    _/  _/  _/        _/  _/    _/  _/    _/    
    _/      _/    _/    _/_/_/      _/      _/    _/_/_/    _/_/_/  _/    _/_/_/  _/    _/_/_/  _/    _/     
                                                               _/                                            
                                                          _/_/
    """,
    2:"""
    ___ _  _ ____    _  _ _ ____ _  _    ___  ____ _ ____ ____ ___ ____ ____ ____ 
     |  |__| |___    |__| | | __ |__|    |__] |__/ | |___ [__   |  |___ [__  [__  
     |  |  | |___    |  | | |__] |  |    |    |  \ | |___ ___]  |  |___ ___] ___]                                                                           
    """,
    3:"""
    ,--,--'.        .-,--.                           
    `- |   |-. ,-.   `\__  ,-,-. ,-. ,-. ,-. ,-. ,-. 
     , |   | | |-'    /    | | | | | |   |-' `-. `-. 
     `-'   ' ' `-'   '`--' ' ' ' |-' '   `-' `-' `-' 
                                 |                   
                                 '                   
    """,
    4:"""
    ,--,--'.        .-,--.                           
    `- |   |-. ,-.   `\__  ,-,-. ,-. ,-. ,-. ,-. ,-. 
     , |   | | |-'    /    | | | | | |-' |   | | |   
     `-'   ' ' `-'   '`--' ' ' ' |-' `-' '   `-' '   
                                 |                    
                                 '                   
    """,
    5:"""
    ""8""              8   8                                                    
      8   e   e eeee   8   8 e  eeee eeeee  eeeee eeeee e   e eeeee eeeee eeeee 
      8e  8   8 8      8eee8 8  8    8   8  8  88 8   8 8   8 8   8 8   8   8   
      88  8eee8 8eee   88  8 8e 8eee 8eee8e 8   8 8eee8 8eee8 8eee8 8e  8   8e  
      88  88  8 88     88  8 88 88   88   8 8   8 88    88  8 88  8 88  8   88  
      88  88  8 88ee   88  8 88 88ee 88   8 8eee8 88    88  8 88  8 88  8   88                                                                          
    """,
    6:"""
      _______ __             ___                                 
     |       |  |--.-----.  |   |  .-----.--.--.-----.----.-----.
     |.|   | |     |  -__|  |.  |  |  _  |  |  |  -__|   _|__ --|
     `-|.  |-|__|__|_____|  |.  |__|_____|\___/|_____|__| |_____|
       |:  |                |:  1   |                            
       |::.|                |::.. . |                            
       `---'                `-------'                                                                                     
    """,
    7:"""
         _____________            ______________               _____      _____ 
         ___  __/__  /______      __  ____/__  /_______ __________(_)_______  /_
         __  /  __  __ \  _ \     _  /    __  __ \  __ `/_  ___/_  /_  __ \  __/
         _  /   _  / / /  __/     / /___  _  / / / /_/ /_  /   _  / / /_/ / /_  
         /_/    /_/ /_/\___/      \____/  /_/ /_/\__,_/ /_/    /_/  \____/\__/  
                                                                                    
    """,
    8:"""
             _______.___________..______       _______ .__   __.   _______ .___________. __    __  
            /       |           ||   _  \     |   ____||  \ |  |  /  _____||           ||  |  |  | 
           |   (----`---|  |----`|  |_)  |    |  |__   |   \|  | |  |  __  `---|  |----`|  |__|  | 
            \   \       |  |     |      /     |   __|  |  . `  | |  | |_ |     |  |     |   __   | 
        .----)   |      |  |     |  |\  \----.|  |____ |  |\   | |  |__| |     |  |     |  |  |  | 
        |_______/       |__|     | _| `._____||_______||__| \__|  \______|     |__|     |__|  |__|
    """,
    9:"""
          _______ __             ___ ___                     __ __   
         |       |  |--.-----.  |   Y   .-----.----.--------|__|  |_ 
         |.|   | |     |  -__|  |.  1   |  -__|   _|        |  |   _|
         `-|.  |-|__|__|_____|  |.  _   |_____|__| |__|__|__|__|____|
           |:  |                |:  |   |                            
           |::.|                |::.|:. |                            
           `---'                `--- ---'
    """,
    10:"""
    8   8  8                                      8\"\"\"\"                                    
    8   8  8 e   e eeee eeee e       eeeee eeee   8     eeeee eeeee eeeee e   e eeeee eeee 
    8e  8  8 8   8 8    8    8       8  88 8      8eeee 8  88 8   8   8   8   8 8   8 8    
    88  8  8 8eee8 8eee 8eee 8e      8   8 8eee   88    8   8 8eee8e  8e  8e  8 8e  8 8eee 
    88  8  8 88  8 88   88   88      8   8 88     88    8   8 88   8  88  88  8 88  8 88   
    88ee8ee8 88  8 88ee 88ee 88eee   8eee8 88     88    8eee8 88   8  88  88ee8 88  8 88ee                                                                                    
    """,
    11:"""
        __ __ __  __  ______ __   ___  ____
        || || || (( \ | || | ||  //   ||   
        || || ||  \\\\    ||   || ((    ||== 
     |__|| \\\\_// \_))   ||   ||  \\\\__ ||___
                                       
    """,
    12:"""
     ______ __  __  ____    __  __  ___  __  __   ___   ____ ____      ___  ___  ___  __  __
     | || | ||  || ||       ||  || // \\\\ ||\ ||  // \\\\ ||    || \\\\     ||\\\\//|| // \\\\ ||\ ||
       ||   ||==|| ||==     ||==|| ||=|| ||\\\\|| (( ___ ||==  ||  ))    || \/ || ||=|| ||\\\\||
       ||   ||  || ||___    ||  || || || || \||  \\\\_|| ||___ ||_//     ||    || || || || \||
                                                                                        
    """,
    13:"""
     _ .-') _     ('-.   ('-.     .-') _    ('-. .-. 
    ( (  OO) )  _(  OO) ( OO ).-.(  OO) )  ( OO )  / 
     \     .'_ (,------./ . --. //     '._ ,--. ,--. 
     ,`'--..._) |  .---'| \-.  \ |'--...__)|  | |  | 
     |  |  \  ' |  |  .-'-'  |  |'--.  .--'|   .|  | 
     |  |   ' |(|  '--.\| |_.'  |   |  |   |       | 
     |  |   / : |  .--' |  .-.  |   |  |   |  .-.  | 
     |  '--'  / |  `---.|  | |  |   |  |   |  | |  | 
     `-------'  `------'`--' `--'   `--'   `--' `--' 
    """,
    14:"""
    ___ ____ _  _ ___  ____ ____ ____ _  _ ____ ____ 
     |  |___ |\/| |__] |___ |__/ |__| |\ | |    |___ 
     |  |___ |  | |    |___ |  \ |  | | \| |___ |___                                                  
    """,
    15:"""
                         (                         
      *   )    )         )\ )                  (   
    ` )  /( ( /(    (   (()/(     (    )   (   )\  
     ( )(_)))\())  ))\   /(_))   ))\  /((  )\ ((_) 
    (_(_())((_)\  /((_) (_))_   /((_)(_))\((_) _   
    |_   _|| |(_)(_))    |   \ (_))  _)((_)(_)| |  
      | |  | ' \ / -_)   | |) |/ -_) \ V / | || |  
      |_|  |_||_|\___|   |___/ \___|  \_/  |_||_|                                             
    """,
    16:"""
     ______ __  __  ____    ______   ___   __    __  ____ ____ 
     | || | ||  || ||       | || |  // \\\\  ||    || ||    || \\\\
       ||   ||==|| ||==       ||   ((   )) \\\\ /\ // ||==  ||_//
       ||   ||  || ||___      ||    \\\\_//   \V/\V/  ||___ || \\\\                                                           
    """,
    17:"""
                                                                                
    _/_/_/_/_/  _/                        _/_/_/    _/                          
       _/      _/_/_/      _/_/        _/        _/_/_/_/    _/_/_/  _/  _/_/   
      _/      _/    _/  _/_/_/_/        _/_/      _/      _/    _/  _/_/        
     _/      _/    _/  _/                  _/    _/      _/    _/  _/           
    _/      _/    _/    _/_/_/      _/_/_/        _/_/    _/_/_/  _/            
                                                                            
                                                                            
    """,
    18:"""
     _______  __   __  _______    __   __  _______  _______  __    _ 
    |       ||  | |  ||       |  |  |_|  ||       ||       ||  |  | |
    |_     _||  |_|  ||    ___|  |       ||   _   ||   _   ||   |_| |
      |   |  |       ||   |___   |       ||  | |  ||  | |  ||       |
      |   |  |       ||    ___|  |       ||  |_|  ||  |_|  ||  _    |
      |   |  |   _   ||   |___   | ||_|| ||       ||       || | |   |
      |___|  |__| |__||_______|  |_|   |_||_______||_______||_|  |__|
    """,
    19:"""
     ______  __                  ____                       
    /\__  _\/\ \                /\  _`\                     
    \/_/\ \/\ \ \___      __    \ \,\L\_\  __  __    ___    
       \ \ \ \ \  _ `\  /'__`\   \/_\__ \ /\ \/\ \ /' _ `\  
        \ \ \ \ \ \ \ \/\  __/     /\ \L\ \ \ \_\ \/\ \/\ \ 
         \ \_\ \ \_\ \_\ \____\    \ `\____\ \____/\ \_\ \_\\
          \/_/  \/_/\/_/\/____/     \/_____/\/___/  \/_/\/_/                                                    
    """,
    20:"""
           __   __    __   _______   _______ .___  ___.  _______ .__   __. .___________.
          |  | |  |  |  | |       \ /  _____||   \/   | |   ____||  \ |  | |           |
          |  | |  |  |  | |  .--.  |  |  __  |  \  /  | |  |__   |   \|  | `---|  |----`
    .--.  |  | |  |  |  | |  |  |  |  | |_ | |  |\/|  | |   __|  |  . `  |     |  |     
    |  `--'  | |  `--'  | |  '--'  |  |__| | |  |  |  | |  |____ |  |\   |     |  |     
     \______/   \______/  |_______/ \______| |__|  |__| |_______||__| \__|     |__|                                                                             
    """,
    21:"""
                        ___           ___                    ___           ___           ___                                 
                       /\  \         /\__\                  /\  \         /\  \         /\  \                       _____    
          ___          \:\  \       /:/ _/_                _\:\  \       /::\  \       /::\  \                     /::\  \   
         /\__\          \:\  \     /:/ /\__\              /\ \:\  \     /:/\:\  \     /:/\:\__\                   /:/\:\  \  
        /:/  /      ___ /::\  \   /:/ /:/ _/_            _\:\ \:\  \   /:/  \:\  \   /:/ /:/  /    ___     ___   /:/  \:\__\ 
       /:/__/      /\  /:/\:\__\ /:/_/:/ /\__\          /\ \:\ \:\__\ /:/__/ \:\__\ /:/_/:/__/___ /\  \   /\__\ /:/__/ \:|__|
      /::\  \      \:\/:/  \/__/ \:\/:/ /:/  /          \:\ \:\/:/  / \:\  \ /:/  / \:\/:::::/  / \:\  \ /:/  / \:\  \ /:/  /
     /:/\:\  \      \::/__/       \::/_/:/  /            \:\ \::/  /   \:\  /:/  /   \::/~~/~~~~   \:\  /:/  /   \:\  /:/  / 
     \/__\:\  \      \:\  \        \:\/:/  /              \:\/:/  /     \:\/:/  /     \:\~~\        \:\/:/  /     \:\/:/  /  
          \:\__\      \:\__\        \::/  /                \::/  /       \::/  /       \:\__\        \::/  /       \::/  /   
           \/__/       \/__/         \/__/                  \/__/         \/__/         \/__/         \/__/         \/__/    
    """
    }
    
    def card_picker():
        card_selection = []
        while True:
            card1 = int(input("Pick a number between 0 and 21 for your past: "))
            if card1 < 0 or card1 > 21:
                print("That number is not between 0 and 21, try again")
                continue
            else:
                card_selection.append(tarot_deck[card1])
                break

        while True:
            card2 = int(input("Pick another number between 0 and 21 for your present: "))
            if tarot_deck[card2] in card_selection:
                print("you already picked that card, try again")
                continue
            elif card2 < 0 or card2 > 21:
                print("That number is not between 0 and 21, try again")
                continue
            else:
                card_selection.append(tarot_deck[card2])
                break
        
        while True:
            card3 = int(input("Pick another number between 0 and 21 for your future: "))
            if tarot_deck[card3] in card_selection:
                print("you already picked that card, try again")
                continue
            elif card3 < 0 or card3 > 21:
                print("That number is not between 0 and 21, try again")
                continue
            else:
                card_selection.append(tarot_deck[card3])
                break
        return card_selection


    while True:
        print(
            """
            +-----------------------------------------------------------------------------------------------------------------+
            |                                                                                                                 |
            | @@@@@@@   @@@@@@   @@@@@@@    @@@@@@   @@@@@@@     @@@@@@@   @@@@@@@@   @@@@@@   @@@@@@@   @@@@@@@@  @@@@@@@    |
            | @@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@   |
            |   @@!    @@!  @@@  @@!  @@@  @@!  @@@    @@!       @@!  @@@  @@!       @@!  @@@  @@!  @@@  @@!       @@!  @@@   |
            |   !@!    !@!  @!@  !@!  @!@  !@!  @!@    !@!       !@!  @!@  !@!       !@!  @!@  !@!  @!@  !@!       !@!  @!@   |
            |   @!!    @!@!@!@!  @!@!!@!   @!@  !@!    @!!       @!@!!@!   @!!!:!    @!@!@!@!  @!@  !@!  @!!!:!    @!@!!@!    |
            |   !!!    !!!@!!!!  !!@!@!    !@!  !!!    !!!       !!@!@!    !!!!!:    !!!@!!!!  !@!  !!!  !!!!!:    !!@!@!     |
            |   !!:    !!:  !!!  !!: :!!   !!:  !!!    !!:       !!: :!!   !!:       !!:  !!!  !!:  !!!  !!:       !!: :!!    |
            |   :!:    :!:  !:!  :!:  !:!  :!:  !:!    :!:       :!:  !:!  :!:       :!:  !:!  :!:  !:!  :!:       :!:  !:!   |
            |    ::    ::   :::  ::   :::  ::::: ::     ::       ::   :::   :: ::::  ::   :::   :::: ::   :: ::::  ::   :::   |
            |    :      :   : :   :   : :   : :  :      :         :   : :  : :: ::    :   : :  :: :  :   : :: ::    :   : :   |
            |                                                                                                                 |
            +-----------------------------------------------------------------------------------------------------------------+
            """
        )        
        user_selection = card_picker()
        
        print("\n")

        print("your past is... {} \n".format(user_selection[0]))
        print("your present is... {} \n".format(user_selection[1]))
        print("your future is... {} \n".format(user_selection[2]))
        
        play_again = input("Play Again?(y/n): ")
        if play_again.lower() == "y":
            continue
        elif play_again.lower() == "n":
            break
        else:
            print("I didn't understand that. I think you need to play again.")

if __name__ == "__main__":
    main()