# Haus QR / IFC research prototype

Static HTML research demo using the `AC20-FZK-Haus.ifc` room **Bad** and IFC GlobalId `0e_hbkIQ5DMQlIJ$2V3j_m`. Equipment and maintenance history are simulated. There is no server/database or real-time model parsing.

## Publish to GitHub Pages

1. Create a new **public** GitHub repository, for example `haus-ifc-qr-demo`.
2. Upload **index.html** and **.nojekyll** into its root and commit.
3. Go to **Settings → Pages**. Set **Deploy from a branch**, branch **main**, folder **/(root)**, and save.
4. Open the published address shown in GitHub Pages settings and verify it works on mobile.
5. Your LightBurn QR payload must be the **exact verified URL** followed by `?room=HOUSE-ROOM-BAD-001` (unless the page URL already has a `?`). The deployed page itself shows/copies the correct full QR URL.
6. Test the QR from a phone on a different network before making the final metal plaque.

If your GitHub account name is `USERNAME`, and repository is `haus-ifc-qr-demo`, the typical URL format is `https://USERNAME.github.io/haus-ifc-qr-demo/?room=HOUSE-ROOM-BAD-001`. This is a pattern, **not a verified deployment address**.

## Demonstration

Scan your metal QR label → open the website → room resolves to IFC model ID → click **Simulate replacement** to preserve the retired equipment's events → click **Inject invalid link** to see the integrity check fail → **Reset**. Refresh resets the simulated state.

**Research limitation:** The prototype's IFC link is pre-extracted and embedded, and its integrity checks use browser memory; future research will integrate IFC parsing, persistent data, model versioning and reproducible testing.
