const grossInput = document.getElementById("gross-input") as HTMLInputElement | null;
const pensionInput = document.getElementById("pension-input") as HTMLInputElement | null;
const studentInput = document.getElementById("student-input") as HTMLSelectElement | null;

export type RequestBody = {
  reference_salary: number;
  pension_contribution: number;
  student_loan_type: string;
};

export function getRequestBody(): RequestBody {
  return {
    reference_salary: getInputAmount(grossInput),
    pension_contribution: getInputAmount(pensionInput),
    student_loan_type: getDropDownOption(studentInput),
  };
}

function getInputAmount(element: HTMLInputElement | null) {
  if (element == null) return 0;
  let amount = Number(element.value);
  if (isNaN(amount)) return 0;
  return amount;
}

function getDropDownOption(element: HTMLSelectElement | null): string {
  if (element == null) return "";
  return element.value;
}
