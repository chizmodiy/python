"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can a ghost be eaten?
    """
    if power_pellet_active == True and touching_ghost == True:
        return True
    else:
        return False
    


def score(touching_power_pellet, touching_dot):
    if touching_power_pellet == True or touching_dot == True:
        return True
    else:
        return False


def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """
    if touching_ghost == True and power_pellet_active ==False:
        return True
    else:
        return False
    


def win(has_eaten_all_dots, has_power_pellet, touching_ghost):
    """Визначає, чи виграв Пакмен.

    :param has_eaten_all_dots: bool - чи з'їдені всі крапки.
    :param has_power_pellet: bool - чи активна супер-сила.
    :param touching_ghost: bool - чи торкається Пакмен привида.
    :return: bool - чи виграв гравець.
    """
    
    # Пакмен програє, якщо торкається привида І не має супер-сили.
    lost = touching_ghost and not has_power_pellet
    
    # Виграш можливий тільки якщо з'їдені всі крапки І гравець не програв.
    return has_eaten_all_dots and not lost
