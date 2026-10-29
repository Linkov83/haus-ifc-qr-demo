# IFC Maintenance – Haus demonstration

This is an early Master's thesis prototype for Computing in Construction at Metropolia.

The original `AC20-FZK-Haus.ifc` model and an extraction of its seven `IfcSpace` entities are included. A fixed QR identifier opens the sample room `Bad` on a webpage. The replacement history and integrity checks use **simulated data**, not a live maintenance system.

The 3D panel loads `model.glb`, a triangulated export of the original IFC geometry. It does **not** draw a fictional house. Until `model.glb` has been generated and uploaded, the panel will display an honest conversion-required message. The IFC model and room data remain accessible.

## Generate the real 3D building mesh

On a Windows computer with Python installed, extract this project folder, open a terminal in the folder and run:

```powershell
py -m pip install ifcopenshell trimesh numpy
py convert_ifc_to_glb.py
```

This creates `model.glb` from the IFC model using IfcOpenShell. Upload `model.glb` to the **root** of this GitHub repository alongside `index.html` and `ifc-data.json`. Refresh GitHub Pages. Use the 3D viewer to rotate and zoom the model. Space highlighting works if the source IFC contains renderable `IfcSpace` geometry.

To deploy initially, upload `index.html`, `ifc-data.json`, `AC20-FZK-Haus.ifc`, `.nojekyll` and this README to GitHub Pages. The converter and notes can also live in the repository. **Do not upload the ZIP itself**; upload the files inside the archive.

The QR URL remains unchanged: `https://linkov83.github.io/haus-ifc-qr-demo/?room=HOUSE-ROOM-BAD-001`.

The current research question is whether stable location identity, time-bounded equipment assignments and link-integrity checks can preserve traceable history when an asset changes. More research is needed to verify reliability and IFC model revisions.
