from vina import Vina
#create docking object
dock = Vina(sf_name='vina',seed=-1280817548,verbosity=2)
receptor = './receptor.pdbqt'
ligand = './ZINC57663637.pdbqt'
output = './ZINC57663637_vina_out.pdbqt'

dock.set_receptor(receptor)
center =  [5.061, 2.751, 17.703]
box_size = [15, 15, 15]
dock.compute_vina_maps(center=center, box_size=box_size)
dock.set_ligand_from_file(ligand)
dock.dock()
pose = dock.poses(n_poses=1)
#dock.write_poses(output,overwrite=True)
