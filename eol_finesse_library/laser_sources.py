

def modulated_laser(l_par, m_par, modes_dictionary=None,
                    output_node='n_source_out',
                    print_code=False):
    """Generates the kat script for a simple modulated laser source

    Args:
        l_par (LaserParams): laser parameters class instance
        m_par (ModulatorParams): modulator parameters class instance
        modes_dictionary (dict of dicts): dictionary with tem modes
            settings for the laser source. i.e
            {'0 0': {'pwr': 0.7, 'phase': 180},
            '0 1': {'pwr': 0.3, 'phase': -90}}
        output_node(str): name of the source output node
        print_code (bool): whether or not to print the resulting code

    Returns:
        string: kat code for this laser source, can  be attached to other
        pieces to form the kat code for the whole system"""

    kat_code = f"""
    #------------------> Modulated Laser source <-----------------------
    l i1 {l_par.power} {l_par.freq} {l_par.phase} nin1       # input laser 

    s s_i1 0.01 nin1 n_EOM_in            # space between laser and eom

    mod eom1 {m_par.freq} {m_par.midx} {m_par.order} {m_par.mode} {m_par.phase} n_EOM_in {output_node}
    """

    if modes_dictionary:
        kat_code += "# ------- l1 tem modes -------------"
        for mode, settings in modes_dictionary.items():
            kat_code += (
                "tem i1 {mode} {settings['pwr']} {settings['phase']}\n")

    if print_code:
        print(kat_code)

    return kat_code + "\n"


def shifted_lasers(l1_par, l2_par, l3_par,
                   l1_modes_dictionary=None,
                   l2_modes_dictionary=None,
                   l3_modes_dictionary=None,
                   output_node='n_source_out',
                   print_code=False):
    """Generates the kat script for a triple combined laser source

    Args:
        l1_par(LaserParams): main laser parameters class instance
        l2_par(LaserParams): aux laser 1 parameters class instance :
        l3_par(LaserParams): aux laser 2 parameters class instance :
        l1_modes_dictionary(dict of dicts): dictionary with tem
            settings for the main laser source. i.e
            {'0 0': {'pwr': 0.7, 'phase': 180},
            '0 1': {'pwr': 0.3, 'phase': -90}}
        l2_modes_dictionary(dict of dicts): dictionary with tem
            settings for the aux 1 laser source. (see example above)
        l3_modes_dictionary(dict of dicts): dictionary with tem
            settings for the aux 2 laser source. (see example above)
        output_node(str): name of the source output node
        print_code (bool): whether or not to print the resulting code

        Returns:
        string: kat code for this laser source, can  be attached to other
        pieces to form the kat code for the whole system"""

    kat_code = f"""
    #--------------> Laser 1 <--------------------
    l i1 {l1_par.power} {l1_par.freq} {l1_par.phase} nin1    # main laser
    s sBS1 0.01 nin1 nBS1_in"""
    if l1_modes_dictionary:
        kat_code += "# ------- l1 tem modes -------------"
        for mode, settings in l1_modes_dictionary.items():
            kat_code += (
                f"tem i1 {mode} {settings['pwr']} {settings['phase']}\n")

    kat_code += f"""    
    #--------------> Laser 2 <--------------------
    l i2 {l2_par.power} {l2_par.freq} {l2_par.phase} nin2    # sideband laser 1
    s sBS2 0.01 nin2 nBS2_in"""
    if l2_modes_dictionary:
        kat_code += "# ------- l2 tem modes -------------"
        for mode, settings in l2_modes_dictionary.items():
            kat_code += (
                f"tem i2 {mode} {settings['pwr']} {settings['phase']}\n")

    kat_code += f"""    
    #--------------> Laser 3 <--------------------
    l i3 {l3_par.power} {l3_par.freq} {l3_par.phase} nin3    # sideband laser 2
    s sBS3 0.01 nin3 nBS2_4"""
    if l3_modes_dictionary:
        kat_code += "# ------- l3 tem modes -------------"
        for mode, settings in l3_modes_dictionary.items():
            kat_code += (
                f"tem i3 {mode} {settings['pwr']} {settings['phase']}\n")

    kat_code += f"""
    #----------------------------> Beam Splitter 1 <--------------------------
    bs BS1 0.5 0.5 0 0 nBS1_in nBS1_2 {output_node} nBS1_4 
    #----------------------------> Beam Splitter 2 <--------------------------
    bs BS2 0.5 0.5 0 0 nBS2_in nBS2_2 nBS2_3 nBS2_4 
    #----------------------------> BS length connections <--------------------
    s sBS21 0.1 nBS1_4 nBS2_2
    """

    if print_code:
        print(kat_code)

    return kat_code + "\n"
