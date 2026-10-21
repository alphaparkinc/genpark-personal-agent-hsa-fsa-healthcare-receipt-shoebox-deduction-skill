# -*- coding: utf-8 -*-
"""HSA/FSA Healthcare Receipt Shoebox Deduction Auditor for GenPark Personal Agent."""
import json
from typing import Dict, Any

class HSAFSAHealthcareReceiptShoeboxAuditor:
    @staticmethod
    def audit_irc213d_expense_eligibility(expense_description: str, amount_usd: float, has_physician_letter_of_medical_necessity: bool = False) -> Dict[str, Any]:
        desc = expense_description.lower()
        if any(k in desc for k in ["dental", "vision", "prescription", "mri", "co-pay", "therapy", "glasses"]):
            qualified = True; requires_lmn = False
        elif any(k in desc for k in ["massage", "gym", "supplements", "ergonomic"]):
            qualified = has_physician_letter_of_medical_necessity; requires_lmn = True
        else:
            qualified = False; requires_lmn = False
        return {"expense": expense_description, "amount_usd": amount_usd, "is_qualified_213d": qualified, "requires_letter_of_medical_necessity": requires_lmn, "audit_status": "TAX_FREE_WITHDRAWAL_APPROVED" if qualified else "REJECTED_OR_NEEDS_LMN"}

    @staticmethod
    def simulate_hsa_shoebox_compound_growth(reimbursable_receipts_usd: float, compounding_years: int, annual_roi_pct: float = 7.5) -> Dict[str, Any]:
        future_val = round(reimbursable_receipts_usd * ((1.0 + (annual_roi_pct / 100.0)) ** compounding_years), 2)
        growth_gains = round(future_val - reimbursable_receipts_usd, 2)
        return {"receipt_basis_usd": reimbursable_receipts_usd, "deferral_years": compounding_years, "future_compound_value_usd": future_val, "tax_free_investment_gain_usd": growth_gains, "shoebox_strategy_verdict": f"Deferring reimbursement yields ${growth_gains:,.2f} tax-free capital."}
