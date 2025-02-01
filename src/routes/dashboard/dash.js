export function rotateElement(event, element) {
  // Get mouse position
  const x = event.clientX;
  const y = event.clientY;

  // Find the middle
  const middleX = window.innerWidth / 2;
  const middleY = window.innerHeight / 2;

  // Get offset from the middle as a percentage
  const offsetX = ((x - middleX) / middleX) * 45;
  const offsetY = ((y - middleY) / middleY) * 45;

  // Set rotation
  element.style.setProperty("--rotateX", offsetX + "deg");
  element.style.setProperty("--rotateY", -1 * offsetY + "deg");
}
