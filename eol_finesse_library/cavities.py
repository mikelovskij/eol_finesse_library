import numpy as np


def angle_finder(l):
    """Finds the angles of a triangle given the sides lengths

    Uses the cosine law:
        cos[alpha] = (b**2 + c**2 - a**2) / (2 * b * c)

    Args:
        l(list of floats): lengths of the triangle sides

    Returns:
        list of floats: angles are listed in order of their opposing side
            (i.e. a[0] is the angle opposed to the side with length l[0],
            therefore between the sides with lengths l[1] and l[2])"""

    a = []
    for i in range(3):
        a.append(np.arccos((l[i - 1] ** 2 + l[i - 2] ** 2 - l[i] ** 2) / (
                    2 * l[i - 1] * l[i - 2])) * 360 / (2 * np.pi))
    return a


def triangular_cavity_builder(cav_lengths, curv_radii, reflectivities,
                              in_node="c_in",
                              tra_node="c_tra",
                              ref_node="ref_node",
                              print_code=False):
    """ Builds the kat code for a triangular cavity given some parameters.


        As a convention, the beam splitters and the angles are numbered after
        their opposing side.


                                bs_end
                             (R[0],  Rc[0])
                               /       \
                              /         \
                             /           \
                            s_c_2        s_c_1
                           (l[2])         (l[1])
                          /                 \
                         /                   \
                        /                     \
                    bs_out-----s_c_bot------bs_in --- ref_node
             (R[1],  Rc[1])     (l[0])      (R[2],  Rc[2])
                     /                           \
                    /                             \
                tra_node                       in_node

    Args:
        cav_lengths(list of floats): length of the sides of a cavity in meters.
            See drawing.
        curv_radii(list of floats): curvature radii of the beam_splitters
         in meters
        reflectivities(list of floats): reflectivities of the beam_splitters
        in_node(str): name of the input node located on the node 1 of bs_in
        tra_node: name of the transmission node located on the node 2 of bs_out
        ref_node: name of the reflection node located on the node 2 of bs_in
        print_code: whether or not to print the resulting code

    Returns:
        str: kat code of the triangular cavity."""

    reflectivities = np.asarray(reflectivities)
    cavity_angles = angle_finder(cav_lengths)
    print("Cavity angles:")
    print("{c[0]:.3f}°, {c[1]:.3f}°, {c[2]:.3f}°".format(c=cavity_angles))
    bs_angles = np.asarray(cavity_angles) / 2

    kat_code = """
    #-------------------------> Triangular Cavity <---------------------------
    
    # -------- cavity mirrors/beamsplitters ----------
    bs bs_in  {R[2]:.4f} {T[2]:.4f}  0  {a[2]:.3f}  {in_node}     {ref_node}    b_in_3   b_in_4   # cavity "input" left base beam splitter
    bs bs_out {R[1]:.4f} {T[1]:.4f}  0  {a[1]:.3f}  b_out_1  {tra_node}    b_out_3  b_out_4  # cavity "output" right base beam splitter
    bs bs_end {R[0]:.4f} {T[0]:.4f}  0  {a[0]:.3f}  b_end_1  b_end_2  b_end_3  b_end_4     # cavity end mirror
    
    
    # ------------ in-cavity spaces ---------------
    s  s_c_bot {l[0]:.4f}  b_out_3 b_in_4                          # cavity short "bottom / base" side
    s  s_c_1   {l[1]:.4f}  b_in_3  b_end_2                         # cavity long left side
    s  s_c_2   {l[2]:.4f}  b_end_1 b_out_4                         # cavity long right side
    
    
    # ------------ curvature radii -------------
    attr bs_end  Rc {Rc[0]}
    attr bs_in   Rc {Rc[2]}  
    attr bs_out  Rc {Rc[1]}  # come funzia la convenz dei segni negli RC dei bs?
    
    
    # cavity parameters and modes tracing
    cav cav1 bs_in b_in_3 bs_in b_in_4
    cp cav1 x finesse
    cp cav1 x w0
    cp cav1 x z
    cp cav1 x fsr
    trace 6
    """.format(l=cav_lengths, Rc=curv_radii, a=bs_angles,
               R=reflectivities, T=(1 - reflectivities),
               in_node=in_node, tra_node=tra_node, ref_node=ref_node)

    if print_code:
        print(kat_code)
    return kat_code
