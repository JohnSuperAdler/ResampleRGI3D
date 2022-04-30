import numpy as np
#from scipy import RegularGridInterpolator
from scipy.interpolate import RegularGridInterpolator

def ResampleRGI3D(input_mx, resize_to, dtype='float64'):
    a, b, c = np.shape(input_mx)
    p, q, r = resize_to
    z_grid = np.linspace(0, p - 1, a)
    y_grid = np.linspace(0, q - 1, b)
    x_grid = np.linspace(0, r - 1, c)
    RGI = RegularGridInterpolator((z_grid, y_grid, x_grid), input_mx)
    z_grid_t2 = np.arange(p)
    y_grid_t2 = np.arange(q)
    x_grid_t2 = np.arange(r)
    meshgrid_para = np.meshgrid(y_grid_t2, z_grid_t2, x_grid_t2)
    RGI_mx = RGI((meshgrid_para[1], meshgrid_para[0], meshgrid_para[2])).astype(dtype)
    return RGI_mx