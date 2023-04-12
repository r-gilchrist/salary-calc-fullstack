import { getDateFromInput } from "./date.js";
const grossInput = document.getElementById("gross-input");
const pensionInput = document.getElementById("pension-input");
const studentInput = document.getElementById("student-input");
export function getRequestBody() {
    return {
        reference_salary: getInputAmount(grossInput),
        pension_contribution: getInputAmount(pensionInput),
        student_loan_type: getDropDownOption(studentInput),
        date: getDateFromInput()
    };
}
function getInputAmount(element) {
    if (element == null)
        return 0;
    let amount = Number(element.value);
    if (isNaN(amount))
        return 0;
    return amount;
}
function getDropDownOption(element) {
    if (element == null)
        return "";
    return element.value;
}
