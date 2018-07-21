class LaserParams:
    """ Container for the Finesse parameters of a laser input light

        This class is used as input attribute in some of the methods used to
        generate .kat scripts.
    """
    def __init__(self, power=1, freq=0, phase=0):
        """Generates the ModulatorParams instance with the required attributes.

        For more info on the attributes see the Finesse reference syntax at
        http://www.gwoptics.org/finesse/reference/

        Args:
            power(float, int or string):
            freq(float, int or string):
            phase(float, int or string):
        """
        self.power = power
        self.freq = freq
        self.phase = phase


class ModulatorParams:
    """ Container for the Finesse parameters of an Electro-Optic Modulator

        his class is used as input attribute in some of the methods used to
        generate .kat scripts.
    """

    def __init__(self, freq, mod_index=0.3, order=1, mode="pm", phase=0):
        """Generates the ModulatorParams instance with the required attributes.

        For more info on the attributes see the Finesse reference syntax at
        http://www.gwoptics.org/finesse/reference/

        Args:
            freq(float, int or string):
            mod_index(float, int or string):
            order(float, int or string):
            mode(string):
            phase(float, int or string):
        """
        self.freq = freq
        self.midx = mod_index
        self.order = order
        self.mode = mode
        self.phase = phase
