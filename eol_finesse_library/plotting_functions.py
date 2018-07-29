import numpy as np
import matplotlib
import ipympl
# matplotlib.use("agg")
import matplotlib.pyplot as plt

matplotlib.interactive(True)


def plot_powers(outputs, title=' power for each mode', save_plot=False):
    for pref, plot_name in {'adt': 'Transmitted', 'adr': 'Reflected'}.items():
        fig, ax = plt.subplots(2, 1, figsize=(10, 6))
        matplotlib.rcParams['font.size'] = 12
        suptitle = plot_name + title

        for name, out in outputs.items():
            # --- HOMs plotting
            # plt.plot(outTF.x, Pdt,label = 'Pdt')
            ax[0].plot(out.x, np.abs(out[pref + '00']) ** 2,
                       label=name + ' Carrier 00')
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
            a.legend(loc=0, fontsize='x-small')
            a.set_ylabel(' Power [W]')
            a.grid()
            # a.set_xticks(np.arange(out.x[0], out.x[-1] + 45, 45))
        ax[-1].set_xlabel(' Mirror phase detuning [Deg]')
        fig.suptitle(suptitle)
        if save_plot:
            fig.savefig(suptitle + ".png")


def plot_phases(outputs, title=' phases for each mode', save_plot=False):
    for pref, plot_name in {'adt': 'Transmitted', 'adr': 'Reflected'}.items():
        fig, ax = plt.subplots(2, 1, figsize=(10, 6))
        matplotlib.rcParams['font.size'] = 12
        suptitle = plot_name + title

        for name, out in outputs.items():
            # --- HOMs plotting
            # plt.plot(outTF.x, Pdt,label = 'Pdt')
            ax[0].plot(out.x, np.angle(out[pref + '00']) ** 2,
                       label=name + '00')
            ax[0].plot(out.x, np.angle(out[pref + 'SB+00']) ** 2,
                       label=name + '+SB00')
            ax[0].plot(out.x, np.angle(out[pref + 'SB-00']) ** 2,
                       label=name + '-SB00')

            # ax[0].plot(out.x, np.angle(out[pref + '10'])**2, label = '10')
            # ax[0].plot(out.x, np.angle(out[pref + '01'])**2, label = '01')
            # ax[0].plot(out.x, np.angle(out[pref + 'SB+10'])**2,
            #            label = '+SB10')
            # ax[0].plot(out.x, np.angle(out[pref + 'SB+01'])**2,
            #            label = '+SB01')
            # ax[0].plot(out.x, np.angle(out[pref + 'SB-10'])**2,
            #            label = '-SB10')
            # ax[0].plot(out.x, np.angle(out[pref + 'SB-01'])**2,
            #            label = '-SB01')

            # ax[0].plot(out.x, np.angle(out[pref + '11'])**2, label = '11')
            ax[1].plot(out.x, np.angle(out[pref + '20']) ** 2,
                       label=name + '20')
            ax[1].plot(out.x, np.angle(out[pref + '02']) ** 2,
                       label=name + '02')

            # ---- +SB
            ax[1].plot(out.x, np.angle(out[pref + 'SB+20']) ** 2,
                       label=name + '+SB20')
            ax[1].plot(out.x, np.angle(out[pref + 'SB+02']) ** 2,
                       label=name + '+SB02')
            # ax[1].plot(out.x, np.angle(out[pref + 'SB+11'])**2,
            #             label = name + '+SB11')

            # ---- -SB
            ax[1].plot(out.x, np.angle(out[pref + 'SB-20']) ** 2,
                       label=name + '-SB20')
            ax[1].plot(out.x, np.angle(out[pref + 'SB-02']) ** 2,
                       label=name + '-SB02')
            # ax[1].plot(out.x, np.angle(out[pref + 'SB-1'])**2,
            #            label = name + '-SB11')
        for a in ax:
            a.legend(loc=0, fontsize='x-small')
            a.set_ylabel(' Phase [rad]')
            a.grid()
            # a.set_xticks(np.arange(out.x[0], out.x[-1] + 45, 45))
        ax[-1].set_xlabel(' Mirror phase detuning [Deg]')
        fig.suptitle(suptitle)
        if save_plot:
            fig.savefig(suptitle + ".png")


def plot_pdh(outputs, suptitle='PDH error signal', save_plot=False):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    matplotlib.rcParams['font.size'] = 12
    for name, out in outputs.items():
        ax.plot(out.x, out['inphase'], label=f'{name} Inphase')
        ax.plot(out.x, out['quadrature'], label=f'{name} Quadrature')
    ax.legend(loc=0, fontsize='small')
    ax.set_ylabel(' Demodulated Power [W * V ??]')
    ax.set_xlabel(' Mirror phase detuning [Deg]')
    ax.set_xticks(np.arange(out.x[0], out.x[-1] + 45, 45))
    ax.grid()
    fig.suptitle(suptitle)
    if save_plot:
        fig.savefig(suptitle + ".png")
    return fig, ax


def plot_lens_sweep(outputs, suptitle=' error signal', save_plot=False):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    matplotlib.rcParams['font.size'] = 12
    for name, out in outputs.items():
        ax.plot(out.x, out['inphase'], label=f'{name} Inphase')
        ax.plot(out.x, out['quadrature'], label=f'{name} Quadrature')
    ax.legend(loc=0, fontsize='small')
    ax.set_ylabel(' Demodulated Power [W * V ??]')
    ax.set_xlabel(' 1/focal [1/m]')
    # ax.set_xticks(np.arange(out.x[0], out.x[-1] + 45, 45))
    ax.grid()
    fig.suptitle(suptitle)
    if save_plot:
        fig.savefig(suptitle + ".png")
    return fig, ax


def plot_total_powers(outputs, suptitle='Total Powers', save_plot=False):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    matplotlib.rcParams['font.size'] = 16
    for name, out in outputs.items():
        ax.plot(out.x, out['PDr'], label=name + ' Refl')
        ax.plot(out.x, out['PDt'], label=name + ' Tra')
        # ax.plot(out.x, out['PDout2'], label=name + ' reverse_tra')
        ax.plot(out.x, out['PDinput_refl'], label=name + ' input_backrefl')
        ax.plot(out.x, out['PDend_tra1'], label=name + ' end_mirror_tra')
        # ax.plot(out.x, out['PDend_tra2'], label=name + ' end_mirror_tra_2')

    ax.set_ylabel(' Power [W]')
    ax.set_xlabel('Mirror phase detuning [Deg]')
    ax.set_xticks(np.arange(out.x[0], out.x[-1] + 45, 45))
    ax.legend(loc=0, fontsize='x-small')
    ax.grid()
    fig.suptitle(suptitle)
    if save_plot:
        fig.savefig(suptitle + ".png")
    return fig, ax


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
    return fig, ax


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
    return fig, ax


def plot_trans_refl(outputs, suptitle="Zero and Second order measured powers",
                    save_plot=False):
    fig, ax = plt.subplots(2, 1, figsize=(10, 6))
    matplotlib.rcParams['font.size'] = 16
    minorlocator = matplotlib.ticker.AutoMinorLocator(2)
    for name, out in outputs.items():
        ax[0].set_ylabel("Transmitted Power [W]")
        ax[1].set_ylabel("Reflected Power [W}")

        ax[0].plot(out.x, out['PDt'], label='Total ' + name + ' Tra')
        ax[1].plot(out.x, out['PDr'], label='Total ' + name + ' Refl')

        for i, pref in enumerate(['adt', 'adr']):
            ax[i].yaxis.set_minor_locator(minorlocator)
            ax[i].set_ylim([0, 0.65])

            ax[i].plot(out.x, np.abs(out[pref + '00']) ** 2,
                       label=name + ' Carrier 00')
            ax[i].plot(out.x, np.abs(out[pref + 'SB+02']) ** 2,
                       label=name + ' +SB 02')
            ax[i].plot(out.x, np.abs(out[pref + 'SB+20']) ** 2,
                       label=name + ' +SB 20')
            ax[i].plot(out.x, np.abs(out[pref + 'SB-02']) ** 2,
                       label=name + ' -SB 02')
            ax[i].plot(out.x, np.abs(out[pref + 'SB-20']) ** 2,
                       label=name + ' -SB 20')
            ax[i].set_ylabel(' Power [W]')
            ax[i].legend(loc=0, fontsize='xx-small')
            ax[i].grid(True, which='major', axis='both')
            ax[i].grid(True, which='minor', axis='y')
            ax[i].set_xticks(np.arange(out.x[0], out.x[-1] + 45, 45))

    ax[-1].set_xlabel('Mirror phase detuning [Deg]')
    ax[-1].set_xticks(np.arange(out.x[0], out.x[-1] + 45, 45))

    fig.suptitle(suptitle)
    if save_plot:
        fig.savefig(suptitle + ".png", dpi=400)
    return fig, ax


def plot_matching_sweeps(lens_sw, z_sw, zr_sw,
                         lens_match=0, z_match=0, zr_match=0.1,
                         suptitle=' Horror signal',
                         save_plot=False):
    fig, ax = plt.subplots(3, 1, figsize=(12, 9))
    matplotlib.rcParams['font.size'] = 12
    for name, out in lens_sw.items():
        ax[0].plot(out.x, out['inphase'], label=f'{name} Inphase')
        ax[0].plot(out.x, out['quadrature'], label=f'{name} Quadrature')
        ax[0].set_xlabel(' 1/focal [1/m]')
        ax[0].vlines(lens_match, -0.12, 0.12, label="cavity modes")
    for name, out in z_sw.items():
        ax[1].plot(out.x, out['inphase'], label=f'{name} Inphase')
        ax[1].plot(out.x, out['quadrature'], label=f'{name} Quadrature')
        ax[1].set_xlabel(' z + z_match [m]')
        ax[1].vlines(z_match, -0.12, 0.12, label="cavity modes")
    for name, out in zr_sw.items():
        ax[2].plot(out.x, out['inphase'], label=f'{name} Inphase')
        ax[2].plot(out.x, out['quadrature'], label=f'{name} Quadrature')
        ax[2].set_xlabel(' zr [m]')
        ax[2].vlines(zr_match, -0.12, 0.12, label="cavity modes")

    for a in ax:
        a.legend(loc=0, fontsize='small')
        a.set_ylabel(' Err [Watts kinda]')
        a.set_ylim([-0.12, 0.12])
        a.grid()

    fig.suptitle(suptitle)
    fig.subplots_adjust(hspace=0.5)
    if save_plot:
        fig.savefig(suptitle + ".png")
    return fig, ax


def plot_matching_sweeps_diffs(lens_sw, z_sw, zr_sw,
                               lens_match=0, z_match=0, zr_match=0.1,
                               suptitle=' Horror signal derivatives',
                               save_plot=False):
    fig, ax = plt.subplots(3, 1, figsize=(12, 9))
    matplotlib.rcParams['font.size'] = 12
    for name, out in lens_sw.items():
        ax[0].plot(out.x, np.gradient(out['inphase'], out.x),
                   label=f'{name} Inphase derivative')
        ax[0].plot(out.x, np.gradient(out['quadrature'], out.x),
                   label=f'{name} Quadrature derivative')
        ax[0].set_xlabel(' 1/focal [1/m]')
        ax[0].vlines(lens_match, -0.07, 0.07, label="cavity modes")
    for name, out in z_sw.items():
        ax[1].plot(out.x, np.gradient(out['inphase'], out.x),
                   label=f'{name} Inphase derivative')
        ax[1].plot(out.x, np.gradient(out['quadrature'], out.x),
                   label=f'{name} Quadrature derivative')
        ax[1].set_xlabel(' z + z_match [m]')
        ax[1].vlines(z_match, -0.07, 0.07, label="cavity modes")
    for name, out in zr_sw.items():
        ax[2].plot(out.x, np.gradient(out['inphase'], out.x),
                   label=f'{name} Inphase derivative')
        ax[2].plot(out.x, np.gradient(out['quadrature'], out.x),
                   label=f'{name} Quadrature derivative')
        ax[2].set_xlabel(' zr [m]')
        ax[2].vlines(zr_match, -0.07, 0.07, label="cavity modes")

    for a in ax:
        a.legend(loc=0, fontsize='small')
        # a.set_ylabel(' ???')
        a.set_ylim([-0.07, 0.07])
        a.grid()

    fig.suptitle(suptitle)
    fig.subplots_adjust(hspace=0.6)
    if save_plot:
        fig.savefig(suptitle + ".png")
    return fig, ax


def plot_beam_params(out_dict, suptitle="some beam parameters",
                     z_dict=None, zr_dict=None, save_plot=False):
    if z_dict is None:
        z_dict = {'l_in_z': 'l_in_z', 'l_out_z': 'l_out_z'}
    if zr_dict is None:
        zr_dict = {'l_in_zr': 'l_in_zr', 'l_out_zr': 'l_out_zr'}
    fig, ax = plt.subplots(2, 1, figsize=(12, 9))
    matplotlib.rcParams['font.size'] = 12
    for name, out in out_dict.items():
        for sens_name, sens in z_dict.items():
            ax[0].plot(out.x, out[sens], label=name + ' ' + sens_name)
        for sens_name, sens in zr_dict.items():
            ax[1].plot(out.x, out[sens], label=name + ' ' + sens_name)
    for a in ax:
        a.grid()
        a.legend()

    ax[-1].set_xlabel('inverse focal [1/m]')
    fig.suptitle(suptitle)
    fig.subplots_adjust(hspace=0.6)
    if save_plot:
        fig.savefig(suptitle + ".png")
    return fig, ax


def plot_trans_refl_2(outputs,
                      suptitle="Zero and Second order measured powers",
                      save_plot=False):
    fig, ax = plt.subplots(2, 1, figsize=(10, 6))
    matplotlib.rcParams['font.size'] = 16
    minorlocator = matplotlib.ticker.AutoMinorLocator(2)
    for name, out in outputs.items():
        ax[0].set_ylabel("Transmitted Power [W]")
        ax[1].set_ylabel("Reflected Power [W}")

        ax[0].semilogy(out.x, out['PDt'], label='Total ' + name + ' Tra',
                       color='C9')
        ax[1].semilogy(out.x, out['PDr'], label='Total ' + name + ' Refl',
                       color='C9')

        for i, pref in enumerate(['adt', 'adr']):
            ax[i].yaxis.set_minor_locator(minorlocator)
            ax[i].set_ylim([0, 0.65])

            ax[i].semilogy(out.x, np.abs(out[pref + '00']) ** 2,
                           label=name + ' Carrier 00')

            ax[i].semilogy(out.x, np.abs(out[pref + '20']) ** 2,
                           label=name + ' Carrier 20')

            ax[i].semilogy(out.x, np.abs(out[pref + '02']) ** 2,
                           label=name + ' Carrier 02')
            ax[i].semilogy(out.x, np.abs(out[pref + 'SB+02']) ** 2,
                           label=name + ' +SB 02')
            ax[i].semilogy(out.x, np.abs(out[pref + 'SB+20']) ** 2,
                           label=name + ' +SB 20')
            ax[i].semilogy(out.x, np.abs(out[pref + 'SB-02']) ** 2,
                           label=name + ' -SB 02')
            ax[i].semilogy(out.x, np.abs(out[pref + 'SB-20']) ** 2,
                           label=name + ' -SB 20')
            ax[i].set_ylabel(' Power [W]')
            ax[i].legend(loc=0, fontsize='xx-small')
            ax[i].grid(True, which='major', axis='both')
            ax[i].grid(True, which='minor', axis='y')
    ax[-1].set_xlabel('Mirror phase detuning [Deg]')

    fig.suptitle(suptitle)
    if save_plot:
        fig.savefig(suptitle + ".png", dpi=400)
    return fig, ax


def plot_trans_refl_phase_2(outputs,
                            suptitle="Zero and Second order measured pahses",
                            save_plot=False):
    fig, ax = plt.subplots(2, 1, figsize=(10, 6))
    matplotlib.rcParams['font.size'] = 16
    minorlocator = matplotlib.ticker.AutoMinorLocator(2)
    for name, out in outputs.items():
        ax[0].set_ylabel("Transmitted Phase [W]")
        ax[1].set_ylabel("Reflected Phase [W}")

        # ax[0].plot(out.x, out['PDt'], label='Total ' + name + ' Tra')
        # ax[1].plot(out.x, out['PDr'], label='Total ' + name + ' Refl')

        for i, pref in enumerate(['adt', 'adr']):
            ax[i].yaxis.set_minor_locator(minorlocator)
            # ax[i].set_ylim([0, 0.65])

            ax[i].plot(out.x,  np.unwrap(np.angle(out[pref + '00'])),
                       label=name + ' Carrier 00')

            ax[i].plot(out.x,  np.unwrap(np.angle(out[pref + '20'])),
                       label=name + ' Carrier 20')

            ax[i].plot(out.x,  np.unwrap(np.angle(out[pref + '02'])),
                       label=name + ' Carrier 02')
            ax[i].plot(out.x,  np.unwrap(np.angle(out[pref + 'SB+02'])),
                       label=name + ' +SB 02')
            ax[i].plot(out.x,  np.unwrap(np.angle(out[pref + 'SB+20'])),
                       label=name + ' +SB 20')
            ax[i].plot(out.x,  np.unwrap(np.angle(out[pref + 'SB-02'])),
                       label=name + ' -SB 02')
            ax[i].plot(out.x,  np.unwrap(np.angle(out[pref + 'SB-20'])),
                       label=name + ' -SB 20')
            ax[i].set_ylabel(' Power [W]')
            ax[i].legend(loc=0, fontsize='xx-small')
            ax[i].grid(True, which='major', axis='both')
            ax[i].grid(True, which='minor', axis='y')

    fig.suptitle(suptitle)
    if save_plot:
        fig.savefig(suptitle + ".png", dpi=400)
    return fig, ax


def plot_overview(outputs,
                  suptitle="Lens sweep overview",
                  save_plot=False):
    fig, ax = plt.subplots(3, 1, figsize=(12, 8))
    matplotlib.rcParams['font.size'] = 16
    minorlocator = matplotlib.ticker.AutoMinorLocator(2)
    for name, out in outputs.items():
        ax[0].set_ylabel("Err signal ")
        ax[1].set_ylabel("Reflected Powers [W}")
        ax[2].set_ylabel("Reflected Phases [W}")
        pref = 'adr'
        ax[0].plot(out.x, out['inphase'], label=f'{name} Inphase')
        ax[0].plot(out.x, out['quadrature'], label=f'{name} Quadrature')
        # ax[0].plot(out.x, out['PDt'], label='Total ' + name + ' Tra')
        ax[1].plot(out.x, out['PDr'], label='Total ' + name + ' Refl',
                   color='C9')

        ax[1].yaxis.set_minor_locator(minorlocator)
        # ax[i].set_ylim([0, 0.65])

        ax[1].semilogy(out.x, np.abs(out[pref + '00']) ** 2,
                       label=name + ' Carrier 00')

        ax[1].semilogy(out.x, np.abs(out[pref + '20']) ** 2,
                       label=name + ' Carrier 20')

        ax[1].semilogy(out.x, np.abs(out[pref + '02']) ** 2,
                       label=name + ' Carrier 02')
        ax[1].semilogy(out.x, np.abs(out[pref + 'SB+02']) ** 2,
                       label=name + ' +SB 02')
        ax[1].semilogy(out.x, np.abs(out[pref + 'SB+20']) ** 2,
                       label=name + ' +SB 20')
        ax[1].semilogy(out.x, np.abs(out[pref + 'SB-02']) ** 2,
                       label=name + ' -SB 02')
        ax[1].semilogy(out.x, np.abs(out[pref + 'SB-20']) ** 2,
                       label=name + ' -SB 20')

        ax[2].yaxis.set_minor_locator(minorlocator)
        # ax[i].set_ylim([0, 0.65])

        ax[2].plot(out.x,  np.unwrap(np.angle(out[pref + '00'])),
                   label=name + ' Carrier 00')

        ax[2].plot(out.x,  np.unwrap(np.angle(out[pref + '20'])),
                   label=name + ' Carrier 20')

        ax[2].plot(out.x,  np.unwrap(np.angle(out[pref + '02'])),
                   label=name + ' Carrier 02')
        ax[2].plot(out.x,  np.unwrap(np.angle(out[pref + 'SB+02'])),
                   label=name + ' +SB 02')
        ax[2].plot(out.x,  np.unwrap(np.angle(out[pref + 'SB+20'])),
                   label=name + ' +SB 20')
        ax[2].plot(out.x,  np.unwrap(np.angle(out[pref + 'SB-02'])),
                   label=name + ' -SB 02')
        ax[2].plot(out.x,  np.unwrap(np.angle(out[pref + 'SB-20'])),
                   label=name + ' -SB 20')

        for a in ax:
            a.legend(loc=0, fontsize='xx-small')
            a.grid(True, which='major', axis='both')
            a.grid(True, which='minor', axis='y')
    fig.subplots_adjust(hspace=0.5)
    fig.suptitle(suptitle)
    if save_plot:
        fig.savefig(suptitle + ".png", dpi=400)
    return fig, ax
