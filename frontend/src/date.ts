const dateInput = document.getElementById("date-input") as HTMLInputElement | null;

export function set_date() {
    if (dateInput == null) return;
    dateInput.valueAsDate = new Date();
}