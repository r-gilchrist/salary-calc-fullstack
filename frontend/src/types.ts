export type RequestBody = {
  reference_salary: number;
  pension_contribution: number;
  student_loan_type: string;
};

export type ResponseBody = {
  reference_salary: number;
  income_tax: number;
  national_insurance: number;
  pension: number;
  student_loan: number;
  net_salary: number;
};
