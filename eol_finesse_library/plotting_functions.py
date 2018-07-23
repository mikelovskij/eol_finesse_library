import numpy as np
import matplotlib
import ipympl
#matplotlib.use("agg")
import matplotlib.pyplot as plt

matplotlib.interactive(True)


def plot_powers(outputs):
    for pref, title in {'adt': 'Transmitted', 'adr': 'Reflected'}.items():
        fig, ax = plt.subplots(2, 1, figsize=(10, 6))
        matplotlib.rcParams['font.size'] = 12
        # plt.plot(outTF.x, Pdt, outTF.x, Pt00, outTF.x,
        #         Pt10, outTF.x, Pt01,label = 'ddd')

        for name, out in outputs.items():
            # --- HOMs plotting
            # plt.plot(outTF.x, Pdt,label = 'Pdt')
            ax[0].plot(out.x, np.abs(out[pref + '00']) ** 2, label=name + '00')
            ax[0].plot(out.x, np.abs(out[pref + 'SB+00']) ** 2,
                       label=name + '+SB00')
            ax[0].plot(out.x, np.abs(out[pref + 'SB-00']) ** 2,
                       label=name + '-SB00')

            # ax[0].plot(out.x, np.abs(out[pref + '10'])**2, label = '10')
            # ax[0].plot(out.x, np.abs(out[pref + '01'])**2, label = '01')
            # ax[0].plot(out.x, np.abs(out[pref + 'SB+10'])**2,
            #            label = '+SB10')
            # ax[0].plot(out.x, np.abs(out[pref + 'SB+01'])**2,
            #            label = '+SB01')
            # ax[0].plot(out.x, np.abs(out[pref + 'SB-10'])**2,
            #            label = '-SB10')
            # ax[0].plot(out.x, np.abs(out[pref + 'SB-01'])**2,
            #            label = '-SB01')


            # ax[0].plot(out.x, np.abs(out[pref + '11'])**2, label = '11')
            ax[1].plot(out.x, np.abs(out[pref + '20']) ** 2, label=name + '20')
            ax[1].plot(out.x, np.abs(out[pref + '02']) ** 2, label=name + '02')


            # ---- +SB
            ax[1].plot(out.x, np.abs(out[pref + 'SB+20']) ** 2,
                       label=name + '+SB20')
            ax[1].plot(out.x, np.abs(out[pref + 'SB+02']) ** 2,
                       label=name + '+SB02')
            # ax[1].plot(out.x, np.abs(out[pref + 'SB+11'])**2,
            #             label = name + '+SB11')

            # ---- -SB
            ax[1].plot(out.x, np.abs(out[pref + 'SB-20']) ** 2,
                       label=name + '-SB20')
            ax[1].plot(out.x, np.abs(out[pref + 'SB-02']) ** 2,
                       label=name + '-SB02')
            # ax[1].plot(out.x, np.abs(out[pref + 'SB-1'])**2,
            #            label = name + '-SB11')
        for a in ax:
            a.legend(loc=0, fontsize='small')
            a.set_ylabel(' Power [W]')
            a.grid()
            a.set_xticks(np.arange(out.x[0], out.x[-1] + 45, 45))
        ax[-1].set_xlabel(' Phase [Deg]')
        fig.suptitle(title + ' power')


def plot_pdh(outputs, suptitle='PDH error signal', save_plot=False):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    matplotlib.rcParams['font.size'] = 12
    for name, out in outputs.items():
        ax.plot(out.x, out['inphase'], label=f'{name} Inphase')
        ax.plot(out.x, out['quadrature'], label=f'{name} Quadrature')
    ax.legend(loc=0, fontsize='small')
    ax.set_ylabel(' Power [W]')
    ax.set_xlabel(' Phase [Deg]')
    ax.set_xticks(np.arange(out.x[0], out.x[-1] + 45, 45))
    ax.grid()
    fig.suptitle(suptitle)
    if save_plot:
        fig.savefig(suptitle + ".png")


def plot_total_powers(outputs):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    matplotlib.rcParams['font.size'] = 16
    for name, out in outputs.items():
        ax.plot(out.x, out['PDr'], label=name + ' Refl')
        ax.plot(out.x, out['PDt'], label=name + ' Tra')
        ax.plot(out.x, out['PDout2'], label=name + ' out2')
        ax.plot(out.x, out['PDinput_refl'], label=name + ' input_backrefl')
        ax.plot(out.x, out['PDend_tra1'], label=name + ' end_mirror_tra_1')
        ax.plot(out.x, out['PDend_tra2'], label=name + ' end_mirror_tra_2')

    ax.set_ylabel(' Power [W]')
    ax.set_xlabel('Phase [Deg]')
    ax.set_xticks(np.arange(out.x[0], out.x[-1] + 45, 45))
    ax.legend(loc=0, fontsize='small')
    ax.grid()



def plot_tf(outputs):
    fig, ax = plt.subplots(2, 1, figsize=(11, 7))
    matplotlib.rcParams['font.size'] = 16
    for name, out in outputs.items():
        ax[0].semilogx(out.x, np.abs(out['inphase']),
                       label=name + ' Inphase')
        ax[0].semilogx(out.x, np.abs(out['quadrature']),
                       label=name + ' Quadrature')
        ax[1].semilogx(out.x, np.angle(out['inphase']),
                       label=name + ' Inphase')
        ax[1].semilogx(out.x, np.angle(out['quadrature']),
                       label=name + ' Quadrature')
    ax[0].set_ylabel('TF magnitude [W/rad]')
    ax[1].set_ylabel('TF phase [rad]')
    for a in ax:
        a.legend(loc=0, fontsize='small')
        a.grid()
    ax[-1].set_xlabel(' Frequency [Hz]')
    fig.suptitle("PDH Error signal Frequency Response")


def plot_phi_tuning(outputs):
    fig, ax = plt.subplots(1, 1, figsize=(11, 8))
    matplotlib.rcParams['font.size'] = 16
    ax2 = ax.twinx()
    for name, out in outputs.items():
        ax.plot(out.x, np.abs(out['sweeper']), label=name + ' Magnitude')

        ax2.plot(out.x, np.angle(out['sweeper']), label=name + ' Phase',
                 linestyle='--')
    ax.set_ylabel('TF magnitude [W/rad]')
    ax2.set_ylabel('TF phase [rad]')

    # a.grid()
    ax.legend(loc=0, fontsize=8)
    ax.grid(axis='x')
    ax2.legend(loc=1, fontsize=8)
    ax.set_xlabel('  Demodulator phase[deg]')
    fig.suptitle("PDH demodulation phase tuning")
