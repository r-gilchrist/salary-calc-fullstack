const dateYearInput = document.getElementById("date-year-input") as HTMLInputElement | null;
const dateMonthInput = document.getElementById("date-month-input") as HTMLInputElement | null;

const date = new Date();

export function set_date() {
  set_year();
  set_month();
}

function set_year() {
  if (dateYearInput == null) return;
  dateYearInput.value = String(date.getFullYear());
}

function set_month() {
  if (dateMonthInput == null) return;
  dateMonthInput.value = String(date.getMonth() + 1);
}
