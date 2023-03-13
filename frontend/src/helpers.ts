export function getInputAmount(element: HTMLInputElement | null) {
  if (element == null) return 0;
  let amount = Number(element.value);
  if (isNaN(amount)) return 0;
  return amount;
}

export function getDropDownOption(element: HTMLSelectElement | null): string {
  if (element == null) return "";
  return element.value;
}

export function updateOutputField(element: HTMLParagraphElement | null, amount: number) {
  if (element == null) return;
  element.textContent = `£${(amount / 12).toFixed(2)}`;
}
