#--- GeoIPS environment has satpy

from satpy import Scene
from glob import glob
import matplotlib.pyplot as plt

#--- Plotting HRIT format example
filenames_hrit = glob("seviri_sample_hrit_local_tailor/*202101010045*")

scene_hrit = Scene(reader="seviri_l1b_hrit", filenames=filenames_hrit)

scene_hrit.load(['VIS006', 'IR_108'])
img_hrit = scene_hrit['IR_108']
# print(img_hrit)

#--- Spatial resolution
dx = img_hrit.x.diff("x").mean().item()
dy = img_hrit.y.diff("y").mean().item()
print(f"dx = {dx}")
print(f"dy = {dy}")

scene_hrit.save_dataset('IR_108', filename="IR_108_hrit.png")

#--- Plotting native format example
filenames_nat = ["seviri_sample_nat_unzipped/MSG4-SEVI-MSG15-0100-NA-20210101005743.653000000Z-NA.nat"]

scene_nat = Scene(reader="seviri_l1b_native", filenames=filenames_nat)

scene_nat.load(['VIS006', 'IR_108'])
img_nat = scene_nat['IR_108']
# print(img_nat)

#--- Spatial resolution
dx = img_nat.x.diff("x").mean().item()
dy = img_nat.y.diff("y").mean().item()
print(f"dx = {dx}")
print(f"dy = {dy}")

scene_nat.save_dataset('IR_108', filename="IR_108_nat.png")