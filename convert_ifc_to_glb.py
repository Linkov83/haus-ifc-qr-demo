"""Convert the original Haus IFC geometry to a genuine GLB mesh, preserving GlobalIds as node names.
Install on Windows: py -m pip install ifcopenshell trimesh numpy
Run: py convert_ifc_to_glb.py
Output: model.glb (upload it to your GitHub repository root)
"""
from pathlib import Path
import sys
import numpy as np
import trimesh
import ifcopenshell
import ifcopenshell.geom

base=Path(__file__).resolve().parent
source=base/'AC20-FZK-Haus.ifc'
out=base/'model.glb'
if not source.exists():sys.exit('Cannot find AC20-FZK-Haus.ifc next to this script.')
model=ifcopenshell.open(str(source))
settings=ifcopenshell.geom.settings()
settings.set(settings.USE_WORLD_COORDS,True)
# Use IFC geometry engine, not arbitrary primitive representations.
scene=trimesh.Scene()
converted=failed=0
for element in model.by_type('IfcProduct'):
    if not getattr(element,'Representation',None) or not getattr(element,'GlobalId',None):continue
    try:
        shape=ifcopenshell.geom.create_shape(settings,element)
        verts=np.asarray(shape.geometry.verts,dtype=np.float64).reshape(-1,3)
        faces=np.asarray(shape.geometry.faces,dtype=np.int64).reshape(-1,3)
        if not len(faces) or not len(verts):continue
        # IFC geometry engine produces coordinates in metres with default settings.
        mesh=trimesh.Trimesh(vertices=verts,faces=faces,process=False)
        if not mesh.is_empty:
            scene.add_geometry(mesh,node_name=f'{element.is_a()}_{element.GlobalId}_{element.id()}',geom_name=f'geom_{element.id()}')
            converted+=1
    except Exception as exc:
        failed+=1
        if failed<=12:print('Skipped',element.is_a(),element.id(),str(exc)[:120])
if not converted:sys.exit('No geometry converted. Check IfcOpenShell installation and input model.')
out.write_bytes(scene.export(file_type='glb'))
print(f'Converted {converted} IFC entities; skipped {failed}. Output {out.name}, {out.stat().st_size:,} bytes')
