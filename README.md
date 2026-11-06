# Silent sleigh player

Permanent URL: https://english-with-svetlana.github.io/ded_moroz_sany/

## Video and verification

Original (preserved locally): `Ded_Moroz_driving_horses_sleigh_264f613d_1080p.mp4`.
H.264 High, yuv420p, 1920×1080, 16:9, 24 fps, 188 frames,
7.833333 seconds of video. Original container: 7.850 seconds because its
AAC stereo 48 kHz audio extends slightly beyond the video.
Original size: 21,755,368 bytes (21.76 MB).

Optimized: `media/sleigh.ebea86de454537f4.mp4`.
H.264 High level 3.1, yuv420p, 1280×720, 16:9, 24 fps, 188 frames,
7.833333 seconds. Size: 6,878,177 bytes (6.88 MB), a 68.384% reduction.
No audio streams. All original video frames and timing retained; no loop edits.
Lossy compression and downscaling necessarily change pixels; sampled visual
comparison looked close. Mean SSIM versus the Lanczos-downscaled source: 0.97264.
This does not establish visually lossless quality during all motion.

Encoding command (FFmpeg available locally):

```sh
ffmpeg -i Ded_Moroz_driving_horses_sleigh_264f613d_1080p.mp4 \
  -map 0:v:0 -vf 'scale=1280:720:flags=lanczos' \
  -c:v libx264 -preset slow -crf 23 -pix_fmt yuv420p -an \
  -movflags +faststart /tmp/sleigh-new.mp4
```

Completed: ffprobe stream checks, full FFmpeg decode without errors, frame count
and duration checks, MP4 moov-before-mdat check, hashed filename verification,
artifact allowlist validation, YAML parsing and workflow structure assertions.
HTTP 200 and correct HTML/MP4 content types verified for player, iframe preview,
artifact player and both media paths.
No existing automated project test suite was present. Actionlint was unavailable.
YAML parsing used Ruby Psych (its YAML 1.1 interpretation of `on` was accounted for).
The workflow has not run on GitHub.

No browser was available: actual playback, autoplay, continuous loop transitions,
Safari, Chrome, mobile and live Genially remain untested. Browser power-saving
and autoplay policies may prevent playback. The source loop boundary may jump;
no footage was changed to conceal it. The page background is transparent; the
video itself is opaque. A non-16:9 iframe leaves transparent unused space so the
entire frame remains visible. Keep the Genially embed at 16:9.

## Local preview

The preview server was started on 127.0.0.1:8000.

- Player: http://127.0.0.1:8000/
- Small 640×360 responsive iframe: http://127.0.0.1:8000/iframe-preview.html
- Exact publish artifact: http://127.0.0.1:8000/_site/

Restart when needed from this project directory:

```sh
python3 scripts/build.py
python3 -m http.server 8000 --bind 127.0.0.1
```

## Manual GitHub setup and publication

No commit, push, deployment, authentication or account-setting changes were made.
The local project folder initially had no Git repository. To preserve any existing
remote history, use a fresh clone for the manual publication commands below.
These commands require an existing repository and normal Git authentication.
No authentication was attempted; no tokens were created or modified.

In repository **Settings → Pages → Build and deployment → Source**, manually
select **GitHub Actions**. Never select **Deploy from a branch / main / root**.
Do not generate the suggested Static HTML or Jekyll workflow. Use the supplied
`.github/workflows/pages.yml`. Ensure repository Actions are enabled and that
any github-pages environment restrictions permit deployment from main.

After reviewing and approving the files, run these commands yourself.
Pushing main triggers publication immediately.

```sh
cd '/Users/lana110/Desktop/ded_moroz_sany '
publish_checkout=$(mktemp -d /tmp/ded-moroz-publish.XXXXXX)
git clone https://github.com/English-with-Svetlana/ded_moroz_sany.git "$publish_checkout"
mkdir -p "$publish_checkout/.github/workflows" "$publish_checkout/scripts" "$publish_checkout/media"
cp index.html .nojekyll .gitignore README.md iframe-preview.html "$publish_checkout/"
cp .github/workflows/pages.yml "$publish_checkout/.github/workflows/"
cp scripts/build.py "$publish_checkout/scripts/"
cp media/sleigh.ebea86de454537f4.mp4 "$publish_checkout/media/"
cd "$publish_checkout"
git switch -C main
python3 scripts/build.py
git add index.html .nojekyll .gitignore README.md iframe-preview.html scripts/build.py .github/workflows/pages.yml media/sleigh.ebea86de454537f4.mp4
git diff --cached --stat
git commit -m "Prepare silent sleigh player and custom Pages deployment"
git push -u origin main
```

Stop if clone fails, or if the repository uses an unexpected default branch;
review its history before switching branches. Never force-push. If authentication
fails, use your existing Git credential manager or GitHub CLI sign-in yourself;
do not paste credentials into chat. Check the Actions run after pushing.

Only three files are published: index.html, .nojekyll, and the referenced hashed
MP4. Source footage, documentation, previews, scripts and obsolete videos are
excluded by scripts/build.py even if they exist in the repository.

## Genially iframe

Paste this into a responsive HTML embed. For a URL-only embed use the permanent
URL and set the embed to 16:9 (for example, 320×180).

```html
<div style="position:relative;width:100%;aspect-ratio:16/9;overflow:hidden;background:transparent">
  <iframe
    src="https://english-with-svetlana.github.io/ded_moroz_sany/"
    title="Sleigh video"
    allow="autoplay"
    scrolling="no"
    style="position:absolute;inset:0;display:block;width:100%;height:100%;border:0;background:transparent"
  ></iframe>
</div>
```

## Future videos

Keep the permanent URL unchanged. Preserve each new source, inspect its frame
rate, aspect ratio and dimensions, and encode without upscaling. The command
above is specific to this 1080p 16:9 source; adapt scaling for smaller replacements.
Keep the original frame rate and all video frames. Strip audio with -an.
Hash the final MP4 with SHA-256, use the first 16 hexadecimal characters as
`media/sleigh.HASH.mp4`, and update index.html to that filename. Rebuild and
verify with scripts/build.py, preview, then manually commit and push main.
New video bytes get a new URL, avoiding reuse of cached old media. The player
URL remains stable; normal HTML cache revalidation may still require a reload
or reopening an already-open Genially slide after deployment propagation.
