export default function media_path(path: string): string {
  return document.getElementById("media-prefix").innerText + path;
}
