export default function static_path(path: string): string {
  return document.getElementById("static-prefix").innerText + path;
}
