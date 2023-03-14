const dateYearInput = document.getElementById("date-year-input") as HTMLInputElement | null;
const dateMonthInput = document.getElementById("date-month-input") as HTMLInputElement | null;

export type UserDate = {
  year: number;
  month: number;
};

const date = new Date();

export function setDefaultDate() {
  setDefaultYear();
  setDefaultMonth();
}

export function getDateFromInput(): UserDate {
  return {
    year: getYearFromInput(),
    month: getMonthFromInput(),
  };
}

function setDefaultYear() {
  if (dateYearInput == null) return;
  dateYearInput.value = String(date.getFullYear());
}

function setDefaultMonth() {
  if (dateMonthInput == null) return;
  dateMonthInput.value = String(date.getMonth() + 1);
}

function getYearFromInput(): number {
  if (dateYearInput == null) return date.getFullYear();
  let year = Number(dateYearInput.value);
  if (isNaN(year)) return date.getFullYear();
  return year;
}

function getMonthFromInput(): number {
  if (dateMonthInput == null) return date.getMonth();
  let month = Number(dateMonthInput.value);
  if (isNaN(month)) return date.getMonth();
  return month;
}
